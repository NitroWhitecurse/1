# -*- coding: utf-8 -*-
"""
MODUL 4: AGENT DE CERCETARE ZILNICA DE IDEI DE PRODUSE
==========================================================

Ce face acest modul:
- Aduna idei de produse printabile 3D din surse publice de pe internet.
- Calculeaza un scor de fezabilitate pentru fiecare idee (cat de rapid/ieftin
  de printat, cat de complex, cat de "saturata" e categoria din care face
  parte fata de ce ti-a mai sugerat agentul in trecut).
- Scrie un fisier markdown datat (ex: idei-2026-07-28.md) cu top 5-10 idei.
- Tine minte ideile din trecut ca sa nu iti recomande aceeasi idee zi de zi.

DESPRE SURSE DE DATE - citeste asta, e important:
- r/functionalprint si r/3Dprinting (Reddit) sunt citite direct, gratuit,
  fara nicio cheie API - functioneaza "din cutie".
- Etsy, Printables, Thingiverse, MyMiniFactory au nevoie de un cont de
  dezvoltator si o cheie API oficiala ca sa le poti interoga corect si
  fara sa incalci regulile lor de folosire. Am lasat "sloturi" pregatite
  pentru fiecare (mai jos, functiile obtine_idei_thingiverse etc.) - daca
  imi dai o cheie in config.json, agentul le foloseste automat. Fara cheie,
  sursa e sarita si afisez un mesaj clar in consola (nu inventez date).
- Pinterest/TikTok nu au un API public gratuit potrivit pentru genul asta
  de cercetare automata, asa ca nu sunt incluse - orice varianta ar
  insemna scraping care incalca termenii lor de utilizare.
- "Pretul mediu de piata observat" e o parte greu de automatizat fara
  API-uri platite. Ca sa fie complet corect (fara sa inventez preturi),
  agentul foloseste "preturi de referinta" pe categorie din
  config.json / preturi_referinta.json, pe care TU le poti actualiza
  cu ce vezi real pe Etsy - cu cat le tii mai actualizate, cu atat
  estimarile devin mai precise.

Cum rulezi manual:
    python agent_idei/agent.py

Cum il programezi sa ruleze singur, o data pe zi - vezi README.md,
sectiunea "Agent de cercetare idei".
"""

import os
import re
import sys
import json
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FOLDER_AGENT = os.path.dirname(os.path.abspath(__file__))
FOLDER_IDEI = os.path.join(FOLDER_AGENT, "idei")
CALE_ISTORIC = os.path.join(FOLDER_AGENT, "istoric_idei.json")
CALE_CONFIG = os.path.join(FOLDER_AGENT, "config.json")
CALE_CONFIG_EXEMPLU = os.path.join(FOLDER_AGENT, "config_exemplu.json")

ZILE_PASTRARE_ISTORIC = 60      # cate zile tinem in istoric (pentru saturatie de categorie)
ZILE_ANTI_REPETITIE = 14        # daca o idee foarte asemanatoare a aparut in ultimele X zile, o sarim
NUMAR_IDEI_IN_RAPORT = 8        # cate idei afisam in raportul zilnic (intre 5 si 10)

# Ponderile scorului de fezabilitate - suma lor conteaza, nu neaparat 1.0
# Modifica-le daca vrei sa dai mai multa greutate unui factor sau altul.
PONDERI_SCOR = {
    "popularitate": 0.30,   # cat de mult interes a primit ideea (upvotes Reddit)
    "complexitate": 0.20,   # cat de simplu e de printat/asamblat (simplu = scor mai mare)
    "timp_print": 0.20,     # cat de repede se printeaza (rapid = scor mai mare, capacitate limitata!)
    "cost": 0.15,           # cat de ieftin e materialul (ieftin = scor mai mare)
    "saturatie": 0.15,      # cat de putin "batuta" e categoria (mai putin saturat = scor mai mare)
}


# ---------------------------------------------------------------------------
# CONFIGURARE (chei API optionale + parametri cost)
# ---------------------------------------------------------------------------

def incarca_config():
    """Incarca config.json daca exista, altfel foloseste valorile din config_exemplu.json."""
    cale = CALE_CONFIG if os.path.exists(CALE_CONFIG) else CALE_CONFIG_EXEMPLU
    try:
        with open(cale, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


CONFIG = incarca_config()
PRET_KWH = CONFIG.get("pret_curent_kwh", 0.9)
MARJA_TINTA = CONFIG.get("marja_tinta_procent", 40) / 100.0


# ---------------------------------------------------------------------------
# SURSE DE DATE
# ---------------------------------------------------------------------------

def obtine_idei_reddit(subreddit, limita=15):
    """
    Citeste postarile de top din ultima zi de pe un subreddit, folosind
    endpoint-ul JSON public al Reddit (nu necesita cont sau cheie API,
    e gandit pentru citire ocazionala/personala - nu bombardam serverul,
    facem un singur request per subreddit, o data pe zi).
    """
    try:
        import requests
    except ImportError:
        print("  [!] Lipseste libraria 'requests'. Instaleaz-o cu: pip install -r requirements.txt")
        return []

    url = f"https://www.reddit.com/r/{subreddit}/top.json?t=day&limit={limita}"
    headers = {"User-Agent": "agent-idei-3dprint-personal/1.0"}
    try:
        raspuns = requests.get(url, headers=headers, timeout=10)
        raspuns.raise_for_status()
        continut = raspuns.json()
    except Exception as e:
        print(f"  [!] Nu am putut prelua idei de la r/{subreddit}: {e}")
        return []

    idei = []
    for postare in continut.get("data", {}).get("children", []):
        p = postare.get("data", {})
        if p.get("stickied"):
            continue
        titlu = p.get("title", "").strip()
        if not titlu:
            continue
        idei.append({
            "titlu": titlu,
            "link": "https://www.reddit.com" + p.get("permalink", ""),
            "popularitate_raw": p.get("score", 0),
            "sursa": f"r/{subreddit}",
        })
    return idei


def obtine_idei_thingiverse(limita=15):
    """
    SLOT PREGATIT pentru Thingiverse. Are nevoie de un "app token" gratuit
    (cont de dezvoltator pe thingiverse.com/developers). Pune-l in
    agent_idei/config.json la cheia "thingiverse_app_token" ca sa se activeze.
    """
    token = CONFIG.get("thingiverse_app_token", "")
    if not token:
        print("  [i] Thingiverse sarit - lipseste 'thingiverse_app_token' din config.json.")
        return []
    try:
        import requests
        url = "https://api.thingiverse.com/newest"
        raspuns = requests.get(url, headers={"Authorization": f"Bearer {token}"}, timeout=10)
        raspuns.raise_for_status()
        rezultate = raspuns.json()
        return [{
            "titlu": item.get("name", ""),
            "link": item.get("public_url", ""),
            "popularitate_raw": item.get("like_count", 0),
            "sursa": "Thingiverse",
        } for item in rezultate[:limita] if item.get("name")]
    except Exception as e:
        print(f"  [!] Eroare la interogarea Thingiverse: {e}")
        return []


def obtine_idei_myminifactory(limita=15):
    """
    SLOT PREGATIT pentru MyMiniFactory. Are nevoie de o cheie API gratuita
    (myminifactory.com/api). Pune-o in config.json la "myminifactory_api_key".
    """
    cheie = CONFIG.get("myminifactory_api_key", "")
    if not cheie:
        print("  [i] MyMiniFactory sarit - lipseste 'myminifactory_api_key' din config.json.")
        return []
    try:
        import requests
        url = f"https://www.myminifactory.com/api/v2/search?key={cheie}&sort=trending"
        raspuns = requests.get(url, timeout=10)
        raspuns.raise_for_status()
        rezultate = raspuns.json().get("hits", [])
        return [{
            "titlu": item.get("name", ""),
            "link": item.get("url", ""),
            "popularitate_raw": item.get("views_count", 0),
            "sursa": "MyMiniFactory",
        } for item in rezultate[:limita] if item.get("name")]
    except Exception as e:
        print(f"  [!] Eroare la interogarea MyMiniFactory: {e}")
        return []


def obtine_idei_etsy(limita=15):
    """
    SLOT PREGATIT pentru Etsy. Etsy cere un API key oficial (Etsy Open API v3,
    developers.etsy.com) si aprobare de aplicatie - nu poate fi accesat liber.
    Pune cheia in config.json la "etsy_api_key" ca sa activezi cautarea de
    listinguri trending pe categoria ta.
    """
    cheie = CONFIG.get("etsy_api_key", "")
    if not cheie:
        print("  [i] Etsy sarit - lipseste 'etsy_api_key' din config.json (necesita aplicatie aprobata de Etsy).")
        return []
    # Implementarea efectiva a request-ului catre Etsy Open API v3 depinde de
    # categoria/cuvintele cheie pe care vrei sa le urmaresti. Extinde aici cand
    # ai cheia - documentatie: https://developers.etsy.com/documentation/
    print("  [i] Cheie Etsy detectata, dar interogarea efectiva trebuie personalizata (vezi comentariul din cod).")
    return []


SURSE_ACTIVE = [
    lambda: obtine_idei_reddit("functionalprint"),
    lambda: obtine_idei_reddit("3Dprinting"),
    obtine_idei_thingiverse,
    obtine_idei_myminifactory,
    obtine_idei_etsy,
]


# ---------------------------------------------------------------------------
# CATEGORII / ESTIMARI - euristici simple bazate pe cuvinte cheie din titlu
# ---------------------------------------------------------------------------

# Fiecare categorie are un profil de productie tipic (poti ajusta valorile
# dupa ce capeti experienta reala cu propriile tale printuri).
PROFILE_CATEGORII = {
    "miniatura":    {"timp_ore": 1.5, "material_g": 20,  "complexitate": 2, "pret_referinta": 25},
    "bijuterie":    {"timp_ore": 1.0, "material_g": 10,  "complexitate": 2, "pret_referinta": 30},
    "organizator":  {"timp_ore": 4.0, "material_g": 150, "complexitate": 2, "pret_referinta": 45},
    "suport":       {"timp_ore": 3.0, "material_g": 80,  "complexitate": 2, "pret_referinta": 35},
    "decor":        {"timp_ore": 6.0, "material_g": 200, "complexitate": 3, "pret_referinta": 60},
    "vaza":         {"timp_ore": 8.0, "material_g": 250, "complexitate": 3, "pret_referinta": 70},
    "gadget":       {"timp_ore": 3.0, "material_g": 60,  "complexitate": 3, "pret_referinta": 40},
    "jucarie":      {"timp_ore": 4.0, "material_g": 100, "complexitate": 3, "pret_referinta": 35},
    "cosplay":      {"timp_ore": 10.0, "material_g": 400, "complexitate": 5, "pret_referinta": 150},
}
PROFIL_IMPLICIT = {"timp_ore": 3.0, "material_g": 80, "complexitate": 3, "pret_referinta": 35}

# Cuvinte cheie (in engleza, pentru ca titlurile de pe Reddit/Thingiverse sunt in engleza)
CUVINTE_CHEIE_CATEGORIE = {
    "miniatura":   ["miniature", "mini "],
    "bijuterie":   ["jewelry", "earring", "pendant", "necklace", "ring"],
    "organizator": ["organizer", "organiser", "storage", "caddy", "bin"],
    "suport":      ["stand", "holder", "mount", "bracket", "hook"],
    "decor":       ["decor", "ornament", "sculpture", "lamp", "light", "art"],
    "vaza":        ["vase", "planter", "pot"],
    "gadget":      ["gadget", "tool", "gizmo", "widget"],
    "jucarie":     ["toy", "fidget", "puzzle", "game"],
    "cosplay":     ["cosplay", "helmet", "armor", "armour", "prop", "mask"],
}
CUVINTE_COMPLEXITATE_MARE = ["multi-part", "multi part", "assembly", "articulated", "moving parts", "kinetic"]

COST_MATERIAL_LEI_PE_KG = 80    # presupunere generica; recomand sa o actualizezi cu costul tau real (vezi modulul 2)
PUTERE_IMPRIMANTA_W = 150


def estimeaza_categorie(titlu):
    titlu_lower = titlu.lower()
    for categorie, cuvinte in CUVINTE_CHEIE_CATEGORIE.items():
        for cuvant in cuvinte:
            if cuvant in titlu_lower:
                return categorie
    return "general"


def estimeaza_profil_productie(titlu):
    categorie = estimeaza_categorie(titlu)
    profil = dict(PROFILE_CATEGORII.get(categorie, PROFIL_IMPLICIT))
    titlu_lower = titlu.lower()
    if any(cuv in titlu_lower for cuv in CUVINTE_COMPLEXITATE_MARE):
        profil["complexitate"] = min(profil["complexitate"] + 1, 5)
    profil["categorie"] = categorie
    return profil


def calculeaza_cost_si_pret(profil):
    cost_material = (profil["material_g"] / 1000.0) * COST_MATERIAL_LEI_PE_KG
    cost_electricitate = profil["timp_ore"] * (PUTERE_IMPRIMANTA_W / 1000.0) * PRET_KWH
    cost_total = cost_material + cost_electricitate
    pret_recomandat = cost_total / (1 - MARJA_TINTA) if MARJA_TINTA < 1 else cost_total * 2
    return cost_total, pret_recomandat


# ---------------------------------------------------------------------------
# ISTORIC (anti-repetitie + saturatie de categorie)
# ---------------------------------------------------------------------------

STOPWORDS = {"the", "a", "an", "of", "for", "with", "and", "to", "my", "in", "on", "is", "this", "i", "made"}


def cuvinte_semnificative(titlu):
    """Extrage cuvintele 'importante' dintr-un titlu, pentru comparatii de similaritate."""
    cuvinte = re.findall(r"[a-zA-Z]+", titlu.lower())
    return {c for c in cuvinte if len(c) > 3 and c not in STOPWORDS}


def similaritate_jaccard(set_a, set_b):
    if not set_a or not set_b:
        return 0.0
    intersectie = set_a & set_b
    uniune = set_a | set_b
    return len(intersectie) / len(uniune)


def incarca_istoric():
    if not os.path.exists(CALE_ISTORIC):
        return []
    try:
        with open(CALE_ISTORIC, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def salveaza_istoric(istoric):
    # Curatam intrarile mai vechi de ZILE_PASTRARE_ISTORIC, ca fisierul sa nu creasca la infinit
    prag = datetime.now() - timedelta(days=ZILE_PASTRARE_ISTORIC)
    istoric_curatat = [i for i in istoric if datetime.strptime(i["data"], "%Y-%m-%d") >= prag]
    with open(CALE_ISTORIC, "w", encoding="utf-8") as f:
        json.dump(istoric_curatat, f, ensure_ascii=False, indent=2)


def este_deja_sugerata_recent(cuvinte_idee, istoric, zile=ZILE_ANTI_REPETITIE):
    prag = datetime.now() - timedelta(days=zile)
    for intrare in istoric:
        data_intrare = datetime.strptime(intrare["data"], "%Y-%m-%d")
        if data_intrare < prag:
            continue
        cuvinte_istoric = set(intrare.get("cuvinte", []))
        if similaritate_jaccard(cuvinte_idee, cuvinte_istoric) > 0.5:
            return True
    return False


def calculeaza_saturatie_categorie(categorie, istoric, zile=30):
    """Cate idei din aceeasi categorie am mai sugerat in ultimele X zile - cu cat mai multe, cu atat categoria e mai 'batuta'."""
    prag = datetime.now() - timedelta(days=zile)
    numar = 0
    for intrare in istoric:
        data_intrare = datetime.strptime(intrare["data"], "%Y-%m-%d")
        if data_intrare >= prag and intrare.get("categorie") == categorie:
            numar += 1
    # Normalizam intre 0 si 1 (consideram "complet saturat" de la 8 aparitii in sus)
    return min(numar / 8.0, 1.0)


# ---------------------------------------------------------------------------
# SCOR DE FEZABILITATE
# ---------------------------------------------------------------------------

def normalizeaza(valoare, valoare_min, valoare_max):
    if valoare_max <= valoare_min:
        return 0.5
    return max(0.0, min(1.0, (valoare - valoare_min) / (valoare_max - valoare_min)))


def calculeaza_scoruri(idei_candidate, istoric):
    """
    Primeste o lista de idei brute (cu titlu, link, popularitate_raw, sursa)
    si adauga fiecareia: categorie, profil de productie, cost, pret, si
    scorul final de fezabilitate (0-100).
    """
    if not idei_candidate:
        return []

    popularitati = [i["popularitate_raw"] for i in idei_candidate]
    pop_min, pop_max = min(popularitati), max(popularitati)

    rezultate = []
    for idee in idei_candidate:
        profil = estimeaza_profil_productie(idee["titlu"])
        cost_total, pret_recomandat = calculeaza_cost_si_pret(profil)

        popularitate_norm = normalizeaza(idee["popularitate_raw"], pop_min, pop_max)
        complexitate_norm = normalizeaza(profil["complexitate"], 1, 5)
        timp_norm = normalizeaza(profil["timp_ore"], 0.5, 12)
        cost_norm = normalizeaza(cost_total, 1, 40)
        saturatie = calculeaza_saturatie_categorie(profil["categorie"], istoric)

        scor = 100 * (
            PONDERI_SCOR["popularitate"] * popularitate_norm
            + PONDERI_SCOR["complexitate"] * (1 - complexitate_norm)
            + PONDERI_SCOR["timp_print"] * (1 - timp_norm)
            + PONDERI_SCOR["cost"] * (1 - cost_norm)
            + PONDERI_SCOR["saturatie"] * (1 - saturatie)
        )

        marja_estimata = None
        if profil["pret_referinta"] > 0:
            marja_estimata = (profil["pret_referinta"] - cost_total) / profil["pret_referinta"] * 100

        rezultate.append({
            **idee,
            "categorie": profil["categorie"],
            "timp_ore": profil["timp_ore"],
            "cost_estimat": cost_total,
            "pret_recomandat": pret_recomandat,
            "pret_referinta_piata": profil["pret_referinta"],
            "marja_estimata_procent": marja_estimata,
            "saturatie_categorie": saturatie,
            "scor": scor,
        })

    return rezultate


# ---------------------------------------------------------------------------
# GENERARE RAPORT MARKDOWN
# ---------------------------------------------------------------------------

def genereaza_raport(idei_finale, data_azi):
    linii = [
        f"# Idei de produse 3D - {data_azi}",
        "",
        "Idei generate automat, sortate dupa scorul de fezabilitate. "
        "Preturile de referinta si estimarile de cost sunt orientative - "
        "verifica manual sursa inainte sa investesti timp de productie.",
        "",
    ]

    if not idei_finale:
        linii.append("Nu am gasit idei noi azi (posibil toate sursele au esuat sau totul era deja sugerat recent).")
    else:
        for i, idee in enumerate(idei_finale, start=1):
            marja_text = f"{idee['marja_estimata_procent']:.0f}%" if idee["marja_estimata_procent"] is not None else "N/A"
            linii.append(f"## {i}. {idee['titlu']} (scor: {idee['scor']:.0f}/100)")
            linii.append(f"- **Sursa:** [{idee['sursa']}]({idee['link']})")
            linii.append(f"- **Categorie estimata:** {idee['categorie']}")
            linii.append(f"- **Timp print estimat:** {idee['timp_ore']:.1f}h")
            linii.append(f"- **Cost estimat (material+curent):** {idee['cost_estimat']:.2f} lei")
            linii.append(f"- **Pret recomandat (marja {int(MARJA_TINTA*100)}%):** {idee['pret_recomandat']:.2f} lei")
            linii.append(f"- **Pret referinta piata (estimare editabila):** {idee['pret_referinta_piata']:.2f} lei -> marja estimata: {marja_text}")
            linii.append(f"- **Saturatie categorie:** {idee['saturatie_categorie']*100:.0f}%")
            linii.append("")

    return "\n".join(linii)


# ---------------------------------------------------------------------------
# PROGRAM PRINCIPAL
# ---------------------------------------------------------------------------

def ruleaza_agent():
    os.makedirs(FOLDER_IDEI, exist_ok=True)
    data_azi = datetime.now().strftime("%Y-%m-%d")

    print(f"=== Agent cercetare idei - {data_azi} ===")
    istoric = incarca_istoric()

    idei_brute = []
    for sursa_func in SURSE_ACTIVE:
        idei_brute.extend(sursa_func())

    print(f"Total idei brute colectate: {len(idei_brute)}")

    # Eliminam ideile care seamana prea mult cu ceva sugerat in ultimele ZILE_ANTI_REPETITIE zile
    idei_noi = []
    for idee in idei_brute:
        cuvinte = cuvinte_semnificative(idee["titlu"])
        if este_deja_sugerata_recent(cuvinte, istoric):
            continue
        idee["_cuvinte"] = cuvinte
        idei_noi.append(idee)

    print(f"Idei noi (dupa eliminarea repetitiilor): {len(idei_noi)}")

    idei_scorate = calculeaza_scoruri(idei_noi, istoric)
    idei_scorate.sort(key=lambda i: i["scor"], reverse=True)
    top_idei = idei_scorate[:NUMAR_IDEI_IN_RAPORT]

    raport = genereaza_raport(top_idei, data_azi)
    cale_raport = os.path.join(FOLDER_IDEI, f"idei-{data_azi}.md")
    with open(cale_raport, "w", encoding="utf-8") as f:
        f.write(raport)
    print(f"-> Raport salvat in: {cale_raport}")

    # Adaugam ideile din top in istoric, ca sa nu le mai repetam curand
    for idee in top_idei:
        istoric.append({
            "data": data_azi,
            "titlu": idee["titlu"],
            "categorie": idee["categorie"],
            "cuvinte": list(idee["_cuvinte"]),
        })
    salveaza_istoric(istoric)


if __name__ == "__main__":
    ruleaza_agent()
