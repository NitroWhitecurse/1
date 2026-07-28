# Sistem local pentru afacere de imprimare 3D

Sistem 100% local (Python + SQLite, fara cloud) pentru gestionarea unei mici
afaceri de imprimare 3D: inventar materiale, calculator cost & marja, tracker
comenzi/productie, agent zilnic de idei de produse, si un dashboard simplu.

Toate datele sunt salvate local, intr-un singur fisier: `data/business.db`
(creat automat la prima rulare a oricarui modul). Nimic nu e trimis in cloud.

## Structura proiectului

```
1/
├── common/db.py              # conexiune comuna la baza de date SQLite
├── calculator/calculator.py  # MODUL 2 - cost & marja
├── inventar/inventar.py      # MODUL 1 - inventar materiale
├── comenzi/tracker.py        # MODUL 3 - tracker comenzi & productie
├── agent_idei/agent.py       # MODUL 4 - agent cercetare idei (rulare programata)
├── dashboard/                # MODUL 5 - dashboard HTML static
└── data/business.db          # baza de date (generata automat, nu e in git)
```

**Fiecare modul functioneaza independent** - poti rula orice script fara sa
fi rulat celelalte inainte. Daca un modul nu are inca date (ex: nu ai adaugat
niciun material), doar afiseaza liste goale, nu da eroare.

## Instalare

Ai nevoie de Python 3.8+ instalat. Pentru modulele 1, 2, 3 si 5 nu trebuie sa
instalezi nimic in plus. Pentru modulul 4 (agentul de idei), care se conecteaza
la internet, instaleaza o singura librarie:

```bash
pip install -r requirements.txt
```

---

## Cum pornesc fiecare parte

Ruleaza toate comenzile din folderul radacina al proiectului (`1/`).

### Modulul 1 - Inventar materiale
```bash
python inventar/inventar.py
```
Meniu cu optiuni: adaugi material nou, listezi stocul (cu alerte), scazi stoc
dupa un print finalizat, modifici pragul de reaprovizionare.

### Modulul 2 - Calculator cost & marja
```bash
python calculator/calculator.py
```
Introduci datele unui produs (greutate, timp print, material, etc.) si obtii
costul real + pretul recomandat pe Etsy / OLX / magazin propriu. Poti salva
produsul ca sablon reutilizabil.

### Modulul 3 - Tracker comenzi si productie
```bash
python comenzi/tracker.py
```
Creezi comenzi, le avansezi prin stari (Primita -> In slicing -> La imprimanta
-> Post-procesare -> Ambalare -> Expediata), inregistrezi esecuri de print, si
generezi raportul saptamanal (ore de printare vs capacitate, rata de esec,
venit vs cost).

Daca numele produsului dintr-o comanda noua se potriveste cu un produs salvat
in Modulul 2, costul si pretul se preiau automat - altfel le introduci manual.

### Modulul 4 - Agent de cercetare zilnica de idei
```bash
python agent_idei/agent.py
```
Vezi sectiunea dedicata mai jos.

### Modulul 5 - Dashboard
```bash
python dashboard/porneste_dashboard.py
```
Regenereaza pagina `dashboard/dashboard.html` cu datele curente si o deschide
automat in browser. Daca vrei doar sa regenerezi fisierul fara sa se deschida
singur browser-ul:
```bash
python dashboard/generate_dashboard.py
```
apoi deschizi manual `dashboard/dashboard.html` facand dublu-click pe el.

---

## Cum adaug un produs nou

1. Ruleaza `python calculator/calculator.py`.
2. Alege optiunea **1. Adauga produs nou**.
3. Completeaza greutatea, timpul de print, materialul, costul materialului,
   rata de esec estimata, timpul de post-procesare etc. (poti apasa Enter
   pentru valorile implicite afisate intre paranteze).
4. La final, raspunde "da" cand ti se cere sa salvezi produsul ca sablon.
5. Data viitoare cand creezi o comanda in Modulul 3 (tracker) cu acelasi nume
   de produs, costul si pretul se preiau automat din acest sablon.

Poti oricand actualiza un produs existent din meniul calculatorului, optiunea
**3. Recalculeaza / actualizeaza un produs existent**.

## Cum modific pragul de reaprovizionare

1. Ruleaza `python inventar/inventar.py`.
2. Alege optiunea **4. Modifica prag de reaprovizionare**.
3. Alege ID-ul materialului din lista afisata si introdu noul prag.

Pragul implicit la adaugarea unui material nou e 200 (grame sau mililitri,
in functie de material) - il poti schimba chiar la adaugare sau oricand dupa.

## Cum vad raportul zilnic de idei

Agentul scrie cate un fisier markdown datat in `agent_idei/idei/`, de exemplu:
```
agent_idei/idei/idei-2026-07-28.md
```
Il poti deschide cu orice editor de text sau vizualizator de markdown. De
asemenea, ultimele idei generate apar automat si in dashboard (Modulul 5).

### Cum programez agentul sa ruleze singur, o data pe zi

**Pe Linux / macOS (cron):**
```bash
crontab -e
```
Adauga o linie (inlocuieste `/calea/catre/1` cu calea reala catre proiect,
si ruleaza agentul dimineata la ora 8:00):
```
0 8 * * * cd /calea/catre/1 && /usr/bin/python3 agent_idei/agent.py >> agent_idei/agent.log 2>&1
```

**Pe Windows (Task Scheduler):**
1. Deschide "Task Scheduler" -> "Create Basic Task".
2. Trigger: Daily, la ora dorita.
3. Action: "Start a program" -> Program/script: `python`, Arguments:
   `agent_idei\agent.py`, Start in: calea catre folderul proiectului.

### Despre sursele de date ale agentului

- **r/functionalprint** si **r/3Dprinting** (Reddit) functioneaza direct, fara
  nicio cheie API.
- **Etsy, Thingiverse, MyMiniFactory** au nevoie de o cheie API gratuita/oficiala
  de la fiecare platforma. Copiaza `agent_idei/config_exemplu.json` in
  `agent_idei/config.json` si completeaza cheile pe care le obtii - fara ele,
  sursa respectiva e pur si simplu sarita (vezi mesajele din consola), nu
  inventam date.
- **Printables**, **Pinterest**, **TikTok** nu au un API public potrivit pentru
  acest tip de cercetare automata fara sa incalce termenii lor de utilizare,
  asa ca nu sunt incluse.
- **Pretul mediu de piata** e greu de automatizat fara API-uri platite -
  agentul foloseste preturi de referinta orientative pe categorie (in
  `agent_idei/agent.py`, dictionarul `PROFILE_CATEGORII`), pe care le poti
  ajusta cu preturi reale observate de tine pe Etsy, ca sa devina tot mai
  precise in timp.

---

## Note generale

- Toate scripturile sunt comentate in romana si scrise cat mai simplu, ca sa
  le poti modifica usor chiar daca nu ai experienta avansata in programare.
- Fiecare modul isi creeaza singur tabelele de care are nevoie in baza de date
  (`CREATE TABLE IF NOT EXISTS`), asa ca poti rula modulele in orice ordine.
- Daca vrei sa "resetezi" tot (sa stergi toate datele si sa incepi de la zero),
  sterge pur si simplu fisierul `data/business.db` - se recreeaza gol la
  urmatoarea rulare a oricarui modul.
- Marja de profit din Modulul 2 si Modulul 4 e calculata ca procent din
  **pretul de vanzare** (nu din cost): la o marja tinta de 40%, inseamna ca
  40% din pretul platit de client ramane profit, dupa scaderea costurilor si
  a comisioanelor canalului de vanzare.
