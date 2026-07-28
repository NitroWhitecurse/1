# -*- coding: utf-8 -*-
"""
MODUL 2: CALCULATOR COST & MARJA
==================================

Ce face acest modul:
- Calculeaza cat te costa REAL un produs printat 3D (material, curent,
  reprint-uri din cauza esecurilor, manopera de post-procesare).
- Iti spune ce pret sa ceri, tinand cont de marja de profit pe care o vrei,
  separat pentru Etsy, OLX si magazin propriu (fiecare are costuri diferite).
- Salveaza fiecare calcul ca "sablon" (produs), ca sa nu mai introduci
  datele de la zero data viitoare - le poti actualiza oricand.

Cum rulezi:
    python calculator/calculator.py

Nu ai nevoie de nimic instalat - foloseste doar libraria standard Python.
"""

import os
import sys

# Ne asiguram ca putem importa "common/db.py" indiferent de unde rulam scriptul
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.db import get_connection, acum_iso


# ---------------------------------------------------------------------------
# SETARI IMPLICITE (le poti schimba aici daca vrei alte valori "default")
# ---------------------------------------------------------------------------

PRET_CURENT_IMPLICIT = 0.9        # lei / kWh
MARJA_TINTA_IMPLICITA = 40.0      # % profit tinta pe pretul de vanzare
PUTERE_IMPLICITA_FDM_W = 150      # wati - imprimanta FDM in timpul printarii
PUTERE_IMPLICITA_RASINA_W = 200   # wati - imprimanta rasina + lampi UV curatare

# Comisioane canale de vanzare.
# ATENTIE: acestea sunt valori orientative - verifica-le periodic pe site-urile
# reale, taxele se mai schimba.
ETSY_COMISION_PROCENT = 6.5       # comision Etsy per transactie
ETSY_PROCESARE_PLATA_PROCENT = 4.0  # comision procesare plata (Etsy Payments)
ETSY_TAXA_FIXA_LISTARE = 1.0     # lei - taxa de listare anunt (~0.20 USD)
OLX_COMISION_PROCENT = 0.0        # OLX nu ia comision la anunturi normale
COST_LIVRARE_MAGAZIN_IMPLICIT = 15.0  # lei - cost livrare estimat, magazin propriu


# ---------------------------------------------------------------------------
# BAZA DE DATE
# ---------------------------------------------------------------------------

def init_tabele(conn):
    """Creeaza tabelul de produse/sabloane daca nu exista deja."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS produse (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nume TEXT UNIQUE NOT NULL,
            greutate_g REAL NOT NULL,
            timp_print_ore REAL NOT NULL,
            tip_material TEXT NOT NULL,
            cost_material_per_kg REAL NOT NULL,
            putere_imprimanta_w REAL NOT NULL,
            pret_curent_kwh REAL NOT NULL,
            rata_esec_procent REAL NOT NULL,
            timp_postprocesare_min REAL NOT NULL,
            cost_manopera_ora REAL NOT NULL,
            marja_tinta_procent REAL NOT NULL,
            cost_livrare_magazin REAL NOT NULL,
            cost_total REAL,
            pret_etsy REAL,
            pret_olx REAL,
            pret_magazin REAL,
            data_creare TEXT,
            data_actualizare TEXT
        );
    """)
    conn.commit()


# ---------------------------------------------------------------------------
# LOGICA DE CALCUL (aici e "creierul" modulului)
# ---------------------------------------------------------------------------

def calculeaza_cost_total(date):
    """
    Primeste un dictionar cu datele produsului si returneaza un dictionar
    cu toate componentele de cost, plus costul total per unitate.

    Formula pe scurt:
      1. cost material = (greutate_g / 1000) * cost_per_kg
      2. cost electricitate = ore_print * (putere_w / 1000) * pret_kwh
      3. (material + electricitate) se impart la (1 - rata_esec%) ca sa
         "platim" statistic si reprint-urile esuate. Ex: la 10% esec,
         ai nevoie in medie de 1 / 0.9 = 1.11 incercari pentru 1 bucata buna.
      4. cost manopera = (minute_postprocesare / 60) * cost_pe_ora
      5. cost total = cost_print_efectiv (pas 3) + cost manopera
    """
    cost_material = (date["greutate_g"] / 1000.0) * date["cost_material_per_kg"]
    cost_electricitate = date["timp_print_ore"] * (date["putere_imprimanta_w"] / 1000.0) * date["pret_curent_kwh"]

    rata_esec = date["rata_esec_procent"] / 100.0
    if rata_esec >= 1:
        rata_esec = 0.95  # protectie: nu putem imparti la zero/negativ (100% esec ar insemna cost infinit)
    factor_reprint = 1.0 / (1.0 - rata_esec)

    cost_print_efectiv = (cost_material + cost_electricitate) * factor_reprint
    cost_manopera = (date["timp_postprocesare_min"] / 60.0) * date["cost_manopera_ora"]

    cost_total = cost_print_efectiv + cost_manopera

    return {
        "cost_material": cost_material,
        "cost_electricitate": cost_electricitate,
        "factor_reprint": factor_reprint,
        "cost_print_efectiv": cost_print_efectiv,
        "cost_manopera": cost_manopera,
        "cost_total": cost_total,
    }


def pret_pentru_marja(cost_total, marja_procent, comision_procent=0.0, taxa_fixa=0.0):
    """
    Calculeaza pretul de vanzare P astfel incat, dupa scaderea comisionului
    canalului de vanzare si a taxelor fixe, profitul ramas sa fie exact
    marja_procent din PRETUL DE VANZARE (nu din cost).

    Deductie matematica:
        profit = P - cost_total - taxa_fixa - comision_procent * P
        vrem:   profit = marja_procent * P
        =>      P * (1 - comision_procent - marja_procent) = cost_total + taxa_fixa
        =>      P = (cost_total + taxa_fixa) / (1 - comision_procent - marja_procent)
    """
    marja = marja_procent / 100.0
    comision = comision_procent / 100.0
    numitor = 1.0 - marja - comision
    if numitor <= 0:
        # Marja ceruta + comisionul depasesc 100% - matematic imposibil.
        # Semnalam clar in loc sa dam un rezultat gresit (negativ).
        return None
    return (cost_total + taxa_fixa) / numitor


def calculeaza_toate_preturile(cost_total, marja_tinta_procent, cost_livrare_magazin):
    """Calculeaza pretul recomandat pe fiecare canal de vanzare."""
    comision_etsy_total = ETSY_COMISION_PROCENT + ETSY_PROCESARE_PLATA_PROCENT
    pret_etsy = pret_pentru_marja(cost_total, marja_tinta_procent, comision_etsy_total, ETSY_TAXA_FIXA_LISTARE)
    pret_olx = pret_pentru_marja(cost_total, marja_tinta_procent, OLX_COMISION_PROCENT, 0.0)
    pret_magazin = pret_pentru_marja(cost_total, marja_tinta_procent, 0.0, cost_livrare_magazin)
    return {
        "pret_etsy": pret_etsy,
        "pret_olx": pret_olx,
        "pret_magazin": pret_magazin,
    }


# ---------------------------------------------------------------------------
# FUNCTII AJUTATOARE PENTRU CITIRE DE LA TASTATURA
# ---------------------------------------------------------------------------

def citeste_numar(mesaj, implicit=None):
    """Citeste un numar de la tastatura; daca userul apasa Enter fara sa scrie
    nimic si exista o valoare implicita, o foloseste pe aceea."""
    while True:
        text = input(mesaj).strip().replace(",", ".")
        if text == "" and implicit is not None:
            return implicit
        try:
            return float(text)
        except ValueError:
            print("  -> Te rog introdu un numar valid (ex: 12.5).")


def citeste_text(mesaj, implicit=None):
    text = input(mesaj).strip()
    if text == "" and implicit is not None:
        return implicit
    return text


# ---------------------------------------------------------------------------
# ACTIUNI DE MENIU
# ---------------------------------------------------------------------------

def actiune_adauga_produs(conn):
    print("\n--- Produs nou: calcul cost & pret ---")
    nume = citeste_text("Nume produs (ex: 'Suport telefon articulat'): ")
    if not nume:
        print("Numele nu poate fi gol. Anulez.")
        return

    greutate_g = citeste_numar("Greutate print (g): ")
    timp_print_ore = citeste_numar("Timp print (ore): ")
    tip_material = citeste_text("Tip material (PLA/PETG/ABS/Rasina): ", "PLA")

    cost_material_per_kg = citeste_numar("Cost material (lei/kg sau lei/litru): ")

    putere_implicita = PUTERE_IMPLICITA_RASINA_W if tip_material.strip().lower() in ("rasina", "resin") else PUTERE_IMPLICITA_FDM_W
    putere_imprimanta_w = citeste_numar(
        f"Putere imprimanta in timpul printarii (W) [implicit {putere_implicita}]: ",
        putere_implicita,
    )

    pret_curent_kwh = citeste_numar(
        f"Pret curent electric (lei/kWh) [implicit {PRET_CURENT_IMPLICIT}]: ",
        PRET_CURENT_IMPLICIT,
    )

    rata_esec_procent = citeste_numar("Rata estimata de esec/reprint (%) [implicit 5]: ", 5.0)
    timp_postprocesare_min = citeste_numar("Timp post-procesare (minute) [implicit 0]: ", 0.0)
    cost_manopera_ora = citeste_numar("Cost manopera (lei/ora) [implicit 0]: ", 0.0)
    marja_tinta_procent = citeste_numar(
        f"Marja tinta de profit (%) [implicit {MARJA_TINTA_IMPLICITA}]: ",
        MARJA_TINTA_IMPLICITA,
    )
    cost_livrare_magazin = citeste_numar(
        f"Cost livrare pt. magazin propriu (lei) [implicit {COST_LIVRARE_MAGAZIN_IMPLICIT}]: ",
        COST_LIVRARE_MAGAZIN_IMPLICIT,
    )

    date = {
        "greutate_g": greutate_g,
        "timp_print_ore": timp_print_ore,
        "tip_material": tip_material,
        "cost_material_per_kg": cost_material_per_kg,
        "putere_imprimanta_w": putere_imprimanta_w,
        "pret_curent_kwh": pret_curent_kwh,
        "rata_esec_procent": rata_esec_procent,
        "timp_postprocesare_min": timp_postprocesare_min,
        "cost_manopera_ora": cost_manopera_ora,
    }

    rezultat_cost = calculeaza_cost_total(date)
    preturi = calculeaza_toate_preturile(rezultat_cost["cost_total"], marja_tinta_procent, cost_livrare_magazin)

    afiseaza_rezultat(nume, rezultat_cost, preturi, marja_tinta_procent)

    raspuns = citeste_text("\nSalvez acest produs ca sablon reutilizabil? (da/nu) [da]: ", "da")
    if raspuns.strip().lower() in ("da", "d", "y", "yes"):
        acum = acum_iso()
        conn.execute("""
            INSERT INTO produse (
                nume, greutate_g, timp_print_ore, tip_material, cost_material_per_kg,
                putere_imprimanta_w, pret_curent_kwh, rata_esec_procent,
                timp_postprocesare_min, cost_manopera_ora, marja_tinta_procent,
                cost_livrare_magazin, cost_total, pret_etsy, pret_olx, pret_magazin,
                data_creare, data_actualizare
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(nume) DO UPDATE SET
                greutate_g=excluded.greutate_g,
                timp_print_ore=excluded.timp_print_ore,
                tip_material=excluded.tip_material,
                cost_material_per_kg=excluded.cost_material_per_kg,
                putere_imprimanta_w=excluded.putere_imprimanta_w,
                pret_curent_kwh=excluded.pret_curent_kwh,
                rata_esec_procent=excluded.rata_esec_procent,
                timp_postprocesare_min=excluded.timp_postprocesare_min,
                cost_manopera_ora=excluded.cost_manopera_ora,
                marja_tinta_procent=excluded.marja_tinta_procent,
                cost_livrare_magazin=excluded.cost_livrare_magazin,
                cost_total=excluded.cost_total,
                pret_etsy=excluded.pret_etsy,
                pret_olx=excluded.pret_olx,
                pret_magazin=excluded.pret_magazin,
                data_actualizare=excluded.data_actualizare
        """, (
            nume, greutate_g, timp_print_ore, tip_material, cost_material_per_kg,
            putere_imprimanta_w, pret_curent_kwh, rata_esec_procent,
            timp_postprocesare_min, cost_manopera_ora, marja_tinta_procent,
            cost_livrare_magazin, rezultat_cost["cost_total"],
            preturi["pret_etsy"], preturi["pret_olx"], preturi["pret_magazin"],
            acum, acum,
        ))
        conn.commit()
        print(f"-> Salvat! Poti recalcula/actualiza oricand acest produs: '{nume}'.")


def afiseaza_rezultat(nume, rezultat_cost, preturi, marja_tinta_procent):
    print(f"\n=== Rezultat pentru: {nume} ===")
    print(f"  Cost material:            {rezultat_cost['cost_material']:.2f} lei")
    print(f"  Cost electricitate:       {rezultat_cost['cost_electricitate']:.2f} lei")
    print(f"  Factor reprint (esecuri): x{rezultat_cost['factor_reprint']:.3f}")
    print(f"  Cost print efectiv:       {rezultat_cost['cost_print_efectiv']:.2f} lei")
    print(f"  Cost manopera:            {rezultat_cost['cost_manopera']:.2f} lei")
    print(f"  ------------------------------------------")
    print(f"  COST TOTAL / unitate:     {rezultat_cost['cost_total']:.2f} lei")
    print(f"\n  Preturi sugerate (marja tinta {marja_tinta_procent:.0f}%):")

    for canal, pret in (("Etsy", preturi["pret_etsy"]), ("OLX", preturi["pret_olx"]), ("Magazin propriu", preturi["pret_magazin"])):
        if pret is None:
            print(f"    {canal:<16}: IMPOSIBIL - marja + comision depasesc 100%. Redu marja tinta.")
        else:
            print(f"    {canal:<16}: {pret:.2f} lei")


def actiune_listeaza_produse(conn):
    randuri = conn.execute("SELECT * FROM produse ORDER BY nume").fetchall()
    if not randuri:
        print("\nNu exista inca niciun produs salvat.")
        return
    print(f"\n{'Nume':<30}{'Cost total':>12}{'Etsy':>10}{'OLX':>10}{'Magazin':>10}")
    print("-" * 72)
    for r in randuri:
        print(f"{r['nume']:<30}{r['cost_total']:>10.2f} lei{r['pret_etsy']:>8.2f} lei{r['pret_olx']:>8.2f} lei{r['pret_magazin']:>8.2f} lei")


def actiune_recalculeaza_produs(conn):
    nume = citeste_text("\nNume produs existent de recalculat: ")
    r = conn.execute("SELECT * FROM produse WHERE nume = ?", (nume,)).fetchone()
    if not r:
        print("Nu am gasit un produs cu acest nume. Vezi lista cu optiunea 2.")
        return

    print("Apasa Enter ca sa pastrezi valoarea curenta afisata in paranteze.")
    date = {
        "greutate_g": citeste_numar(f"Greutate print (g) [{r['greutate_g']}]: ", r["greutate_g"]),
        "timp_print_ore": citeste_numar(f"Timp print (ore) [{r['timp_print_ore']}]: ", r["timp_print_ore"]),
        "tip_material": citeste_text(f"Tip material [{r['tip_material']}]: ", r["tip_material"]),
        "cost_material_per_kg": citeste_numar(f"Cost material (lei/kg) [{r['cost_material_per_kg']}]: ", r["cost_material_per_kg"]),
        "putere_imprimanta_w": citeste_numar(f"Putere imprimanta (W) [{r['putere_imprimanta_w']}]: ", r["putere_imprimanta_w"]),
        "pret_curent_kwh": citeste_numar(f"Pret curent (lei/kWh) [{r['pret_curent_kwh']}]: ", r["pret_curent_kwh"]),
        "rata_esec_procent": citeste_numar(f"Rata esec (%) [{r['rata_esec_procent']}]: ", r["rata_esec_procent"]),
        "timp_postprocesare_min": citeste_numar(f"Timp post-procesare (min) [{r['timp_postprocesare_min']}]: ", r["timp_postprocesare_min"]),
        "cost_manopera_ora": citeste_numar(f"Cost manopera (lei/ora) [{r['cost_manopera_ora']}]: ", r["cost_manopera_ora"]),
    }
    marja_tinta_procent = citeste_numar(f"Marja tinta (%) [{r['marja_tinta_procent']}]: ", r["marja_tinta_procent"])
    cost_livrare_magazin = citeste_numar(f"Cost livrare magazin (lei) [{r['cost_livrare_magazin']}]: ", r["cost_livrare_magazin"])

    rezultat_cost = calculeaza_cost_total(date)
    preturi = calculeaza_toate_preturile(rezultat_cost["cost_total"], marja_tinta_procent, cost_livrare_magazin)
    afiseaza_rezultat(nume, rezultat_cost, preturi, marja_tinta_procent)

    acum = acum_iso()
    conn.execute("""
        UPDATE produse SET
            greutate_g=?, timp_print_ore=?, tip_material=?, cost_material_per_kg=?,
            putere_imprimanta_w=?, pret_curent_kwh=?, rata_esec_procent=?,
            timp_postprocesare_min=?, cost_manopera_ora=?, marja_tinta_procent=?,
            cost_livrare_magazin=?, cost_total=?, pret_etsy=?, pret_olx=?, pret_magazin=?,
            data_actualizare=?
        WHERE nume=?
    """, (
        date["greutate_g"], date["timp_print_ore"], date["tip_material"], date["cost_material_per_kg"],
        date["putere_imprimanta_w"], date["pret_curent_kwh"], date["rata_esec_procent"],
        date["timp_postprocesare_min"], date["cost_manopera_ora"], marja_tinta_procent,
        cost_livrare_magazin, rezultat_cost["cost_total"],
        preturi["pret_etsy"], preturi["pret_olx"], preturi["pret_magazin"],
        acum, nume,
    ))
    conn.commit()
    print("-> Sablon actualizat.")


def meniu_principal():
    conn = get_connection()
    init_tabele(conn)

    while True:
        print("\n================ CALCULATOR COST & MARJA ================")
        print("1. Adauga produs nou (calculeaza cost + pret)")
        print("2. Listeaza produse salvate")
        print("3. Recalculeaza / actualizeaza un produs existent")
        print("0. Iesire")
        optiune = input("Alege o optiune: ").strip()

        if optiune == "1":
            actiune_adauga_produs(conn)
        elif optiune == "2":
            actiune_listeaza_produse(conn)
        elif optiune == "3":
            actiune_recalculeaza_produs(conn)
        elif optiune == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida, incearca din nou.")

    conn.close()


if __name__ == "__main__":
    meniu_principal()
