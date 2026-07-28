# -*- coding: utf-8 -*-
"""
MODUL 3: TRACKER COMENZI SI PRODUCTIE
========================================

Ce face acest modul:
- Tine evidenta comenzilor printr-un flux de stari:
    Primita -> In slicing -> La imprimanta (aleasa dintre cele 3) ->
    Post-procesare -> Ambalare -> Expediata
- Cronometreaza automat cat timp sta o comanda in fiecare stare (ca sa
  vezi unde se blocheaza productia: la slicing? la imprimanta? la ambalare?).
- Genereaza un raport saptamanal: ore de printare folosite fata de
  capacitatea teoretica (numar imprimante x ore/zi), rata reala de esec,
  si venit fata de cost estimat (material + electricitate).

Cum rulezi:
    python comenzi/tracker.py

Nu ai nevoie de nimic instalat - foloseste doar libraria standard Python.
"""

import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.db import get_connection, acum_iso

# Fluxul de stari, in ordine. O comanda avanseaza mereu la starea urmatoare din lista.
FLUX_STARI = ["Primita", "In slicing", "La imprimanta", "Post-procesare", "Ambalare", "Expediata"]

IMPRIMANTE_DISPONIBILE = ["FDM-1", "FDM-2", "Rasina-1"]

# Folosite pentru raportul saptamanal (capacitate teoretica de productie)
NUMAR_IMPRIMANTE = 3
ORE_LUCRU_PE_ZI = 8  # cate ore pe zi presupunem ca imprimantele pot lucra (modifica daca ai printare non-stop)


# ---------------------------------------------------------------------------
# BAZA DE DATE
# ---------------------------------------------------------------------------

def init_tabele(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS comenzi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client TEXT,
            produs_nume TEXT NOT NULL,
            cantitate INTEGER NOT NULL DEFAULT 1,
            canal TEXT,                          -- Etsy / OLX / Magazin propriu
            stare TEXT NOT NULL,
            imprimanta_folosita TEXT,
            numar_esecuri INTEGER NOT NULL DEFAULT 0,
            cost_estimat_unitate REAL DEFAULT 0,  -- material + electricitate, per bucata
            pret_vanzare_unitate REAL DEFAULT 0,
            data_creare TEXT,
            data_ultima_schimbare TEXT
        );
    """)
    # Istoricul tranzitiilor de stare - aici se calculeaza timpul petrecut in fiecare etapa
    conn.execute("""
        CREATE TABLE IF NOT EXISTS istoric_stari (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comanda_id INTEGER NOT NULL,
            stare TEXT NOT NULL,
            imprimanta_folosita TEXT,
            data_intrare TEXT NOT NULL,
            data_iesire TEXT,
            durata_ore REAL,
            FOREIGN KEY (comanda_id) REFERENCES comenzi(id)
        );
    """)
    conn.commit()


def parseaza_data(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------------------------------
# FUNCTII AJUTATOARE INPUT
# ---------------------------------------------------------------------------

def citeste_numar(mesaj, implicit=None):
    while True:
        text = input(mesaj).strip().replace(",", ".")
        if text == "" and implicit is not None:
            return implicit
        try:
            return float(text)
        except ValueError:
            print("  -> Te rog introdu un numar valid.")


def citeste_text(mesaj, implicit=None):
    text = input(mesaj).strip()
    if text == "" and implicit is not None:
        return implicit
    return text


def cauta_produs_in_calculator(conn, nume_produs):
    """
    Incearca sa gaseasca produsul in tabelul 'produse' creat de modulul 2
    (calculator/calculator.py), ca sa preia automat costul si pretul.
    Daca tabelul sau produsul nu exista (modulul 2 nu a fost rulat inca),
    returneaza None fara sa dea eroare - modulele sunt independente.
    """
    try:
        return conn.execute("SELECT * FROM produse WHERE nume = ?", (nume_produs,)).fetchone()
    except Exception:
        return None


# ---------------------------------------------------------------------------
# ACTIUNI DE MENIU
# ---------------------------------------------------------------------------

def actiune_comanda_noua(conn):
    print("\n--- Comanda noua ---")
    client = citeste_text("Client (nume/username): ")
    produs_nume = citeste_text("Nume produs: ")
    cantitate = int(citeste_numar("Cantitate [1]: ", 1))
    canal = citeste_text("Canal (Etsy/OLX/Magazin propriu): ", "Etsy")

    produs_calculator = cauta_produs_in_calculator(conn, produs_nume)
    if produs_calculator:
        print(f"  -> Am gasit '{produs_nume}' in Calculatorul de cost (modulul 2). Preiau automat costul si pretul.")
        cost_estimat = produs_calculator["cost_total"]
        harta_pret = {
            "etsy": produs_calculator["pret_etsy"],
            "olx": produs_calculator["pret_olx"],
            "magazin propriu": produs_calculator["pret_magazin"],
            "magazin": produs_calculator["pret_magazin"],
        }
        pret_vanzare = harta_pret.get(canal.strip().lower(), produs_calculator["pret_olx"])
    else:
        cost_estimat = citeste_numar("Cost estimat material+electricitate / bucata (lei) [0]: ", 0.0)
        pret_vanzare = citeste_numar("Pret de vanzare / bucata (lei) [0]: ", 0.0)

    acum = acum_iso()
    stare_initiala = FLUX_STARI[0]
    cursor = conn.execute("""
        INSERT INTO comenzi (client, produs_nume, cantitate, canal, stare, cost_estimat_unitate,
                              pret_vanzare_unitate, data_creare, data_ultima_schimbare)
        VALUES (?,?,?,?,?,?,?,?,?)
    """, (client, produs_nume, cantitate, canal, stare_initiala, cost_estimat, pret_vanzare, acum, acum))
    comanda_id = cursor.lastrowid

    conn.execute("""
        INSERT INTO istoric_stari (comanda_id, stare, data_intrare) VALUES (?,?,?)
    """, (comanda_id, stare_initiala, acum))
    conn.commit()
    print(f"-> Comanda #{comanda_id} creata, stare: '{stare_initiala}'.")


def actiune_avanseaza_stare(conn):
    print("\n--- Avanseaza comanda la urmatoarea stare ---")
    listeaza_comenzi_active(conn, doar_afisare=True)
    comanda_id = int(citeste_numar("ID comanda de avansat: "))
    comanda = conn.execute("SELECT * FROM comenzi WHERE id=?", (comanda_id,)).fetchone()
    if not comanda:
        print("Nu am gasit aceasta comanda.")
        return

    if comanda["stare"] == FLUX_STARI[-1]:
        print(f"Comanda #{comanda_id} este deja '{FLUX_STARI[-1]}' - nu mai poate avansa.")
        return

    indice_curent = FLUX_STARI.index(comanda["stare"])
    stare_noua = FLUX_STARI[indice_curent + 1]
    acum = acum_iso()

    # Inchidem starea curenta din istoric si calculam durata petrecuta in ea
    rand_deschis = conn.execute(
        "SELECT * FROM istoric_stari WHERE comanda_id=? AND data_iesire IS NULL ORDER BY id DESC LIMIT 1",
        (comanda_id,)
    ).fetchone()
    if rand_deschis:
        durata_ore = (parseaza_data(acum) - parseaza_data(rand_deschis["data_intrare"])).total_seconds() / 3600.0
        conn.execute("UPDATE istoric_stari SET data_iesire=?, durata_ore=? WHERE id=?",
                     (acum, durata_ore, rand_deschis["id"]))

    imprimanta_folosita = comanda["imprimanta_folosita"]
    if stare_noua == "La imprimanta":
        print(f"Imprimante disponibile: {', '.join(IMPRIMANTE_DISPONIBILE)}")
        imprimanta_folosita = citeste_text("Ce imprimanta foloseste? ", IMPRIMANTE_DISPONIBILE[0])

    conn.execute("UPDATE comenzi SET stare=?, imprimanta_folosita=?, data_ultima_schimbare=? WHERE id=?",
                 (stare_noua, imprimanta_folosita, acum, comanda_id))
    conn.execute("""
        INSERT INTO istoric_stari (comanda_id, stare, imprimanta_folosita, data_intrare) VALUES (?,?,?,?)
    """, (comanda_id, stare_noua, imprimanta_folosita if stare_noua == "La imprimanta" else None, acum))
    conn.commit()
    print(f"-> Comanda #{comanda_id} este acum in starea '{stare_noua}'.")


def actiune_inregistreaza_esec(conn):
    print("\n--- Inregistreaza esec de print (reprint) ---")
    listeaza_comenzi_active(conn, doar_afisare=True)
    comanda_id = int(citeste_numar("ID comanda cu print esuat: "))
    comanda = conn.execute("SELECT * FROM comenzi WHERE id=?", (comanda_id,)).fetchone()
    if not comanda:
        print("Nu am gasit aceasta comanda.")
        return
    conn.execute("UPDATE comenzi SET numar_esecuri = numar_esecuri + 1 WHERE id=?", (comanda_id,))
    conn.commit()
    print(f"-> Am notat un esec pentru comanda #{comanda_id}. Nu uita sa reiei printul (comanda ramane in starea curenta).")


def listeaza_comenzi_active(conn, doar_afisare=False):
    randuri = conn.execute("SELECT * FROM comenzi WHERE stare != ? ORDER BY id", (FLUX_STARI[-1],)).fetchall()
    if not randuri:
        print("\nNu exista comenzi active (toate sunt expediate sau nu exista comenzi).")
        return
    acum = datetime.now()
    print(f"\n{'ID':<4}{'Client':<15}{'Produs':<22}{'Stare':<16}{'Timp in stare':<15}{'Esecuri':<8}")
    print("-" * 82)
    for r in randuri:
        rand_deschis = conn.execute(
            "SELECT * FROM istoric_stari WHERE comanda_id=? AND data_iesire IS NULL ORDER BY id DESC LIMIT 1",
            (r["id"],)
        ).fetchone()
        timp_in_stare = "-"
        if rand_deschis:
            ore = (acum - parseaza_data(rand_deschis["data_intrare"])).total_seconds() / 3600.0
            timp_in_stare = f"{ore:.1f}h"
        print(f"{r['id']:<4}{(r['client'] or ''):<15}{r['produs_nume']:<22}{r['stare']:<16}{timp_in_stare:<15}{r['numar_esecuri']:<8}")


def actiune_raport_saptamanal(conn):
    print("\n=========== RAPORT SAPTAMANAL (ultimele 7 zile) ===========")
    acum = datetime.now()
    acum_sapt = acum - timedelta(days=7)

    # --- 1. Ore de printare folosite vs capacitate teoretica ---
    randuri_print = conn.execute(
        "SELECT * FROM istoric_stari WHERE stare = 'La imprimanta' AND data_intrare >= ?",
        (acum_sapt.strftime("%Y-%m-%d %H:%M:%S"),)
    ).fetchall()
    ore_folosite = 0.0
    for r in randuri_print:
        if r["durata_ore"] is not None:
            ore_folosite += r["durata_ore"]
        else:
            # Starea e inca deschisa (printul e in desfasurare acum) - numaram pana in prezent
            ore_folosite += (acum - parseaza_data(r["data_intrare"])).total_seconds() / 3600.0

    capacitate_teoretica = NUMAR_IMPRIMANTE * ORE_LUCRU_PE_ZI * 7
    procent_utilizare = (ore_folosite / capacitate_teoretica * 100) if capacitate_teoretica else 0

    print(f"\nOre de printare folosite:     {ore_folosite:.1f}h")
    print(f"Capacitate teoretica (7 zile): {capacitate_teoretica:.0f}h  ({NUMAR_IMPRIMANTE} imprimante x {ORE_LUCRU_PE_ZI}h/zi x 7 zile)")
    print(f"Grad de utilizare:            {procent_utilizare:.0f}%")

    # --- 2. Rata reala de esec ---
    comenzi_perioada = conn.execute(
        "SELECT * FROM comenzi WHERE data_creare >= ? OR data_ultima_schimbare >= ?",
        (acum_sapt.strftime("%Y-%m-%d %H:%M:%S"), acum_sapt.strftime("%Y-%m-%d %H:%M:%S"))
    ).fetchall()
    total_esecuri = sum(r["numar_esecuri"] for r in comenzi_perioada)
    total_comenzi_active_perioada = len(comenzi_perioada)
    rata_esec = (total_esecuri / (total_esecuri + total_comenzi_active_perioada) * 100) if (total_esecuri + total_comenzi_active_perioada) else 0
    print(f"\nEsecuri de print inregistrate: {total_esecuri}")
    print(f"Rata reala de esec (estimare): {rata_esec:.1f}%")

    # --- 3. Venit vs cost (comenzi expediate in ultima saptamana) ---
    comenzi_expediate = conn.execute(
        "SELECT * FROM comenzi WHERE stare = ? AND data_ultima_schimbare >= ?",
        (FLUX_STARI[-1], acum_sapt.strftime("%Y-%m-%d %H:%M:%S"))
    ).fetchall()
    venit_total = sum(r["pret_vanzare_unitate"] * r["cantitate"] for r in comenzi_expediate)
    cost_total = sum(r["cost_estimat_unitate"] * r["cantitate"] for r in comenzi_expediate)
    profit = venit_total - cost_total

    print(f"\nComenzi expediate in ultima saptamana: {len(comenzi_expediate)}")
    print(f"Venit total:  {venit_total:.2f} lei")
    print(f"Cost total (material+electricitate estimat): {cost_total:.2f} lei")
    print(f"Profit estimat: {profit:.2f} lei")
    print("\n(Nota: costul aici include doar material+electricitate - manopera de post-procesare")
    print(" o gasesti detaliata per produs in modulul 2, Calculator cost & marja.)")


def meniu_principal():
    conn = get_connection()
    init_tabele(conn)

    while True:
        print("\n================ TRACKER COMENZI SI PRODUCTIE ================")
        print("1. Comanda noua")
        print("2. Avanseaza comanda la urmatoarea stare")
        print("3. Inregistreaza esec de print (reprint)")
        print("4. Listeaza comenzi active")
        print("5. Raport saptamanal (capacitate, esecuri, venit/cost)")
        print("0. Iesire")
        optiune = input("Alege o optiune: ").strip()

        if optiune == "1":
            actiune_comanda_noua(conn)
        elif optiune == "2":
            actiune_avanseaza_stare(conn)
        elif optiune == "3":
            actiune_inregistreaza_esec(conn)
        elif optiune == "4":
            listeaza_comenzi_active(conn)
        elif optiune == "5":
            actiune_raport_saptamanal(conn)
        elif optiune == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida, incearca din nou.")

    conn.close()


if __name__ == "__main__":
    meniu_principal()
