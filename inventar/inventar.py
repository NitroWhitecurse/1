# -*- coding: utf-8 -*-
"""
MODUL 1: INVENTAR MATERIALE
=============================

Ce face acest modul:
- Tine evidenta materialelor tale (PLA, PETG, ABS, Rasina): culoare,
  cat mai ai (grame sau mililitri), cat te-a costat, de la ce furnizor.
- Iti seteaza un prag minim per material si te avertizeaza in consola
  cand stocul scade sub acel prag ("trebuie sa comanzi").
- Dupa ce termini un print, scazi automat cantitatea folosita din stoc.

Cum rulezi:
    python inventar/inventar.py

Nu ai nevoie de nimic instalat - foloseste doar libraria standard Python.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.db import get_connection, acum_iso


# ---------------------------------------------------------------------------
# BAZA DE DATE
# ---------------------------------------------------------------------------

def init_tabele(conn):
    """Creeaza tabelele de inventar daca nu exista deja."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS materiale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tip TEXT NOT NULL,
            culoare TEXT,
            unitate TEXT NOT NULL,              -- 'g' sau 'ml'
            cantitate_ramasa REAL NOT NULL,
            cost_per_kg_litru REAL NOT NULL,
            furnizor TEXT,
            prag_minim REAL NOT NULL,
            data_adaugare TEXT
        );
    """)
    # Jurnal de miscari de stoc, util pentru istoric / verificare ("cine a consumat ce")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS miscari_stoc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            material_id INTEGER NOT NULL,
            tip_miscare TEXT NOT NULL,          -- 'adaugare' sau 'consum'
            cantitate REAL NOT NULL,
            motiv TEXT,
            data TEXT,
            FOREIGN KEY (material_id) REFERENCES materiale(id)
        );
    """)
    conn.commit()


def unitate_pentru_tip(tip):
    """PLA/PETG/ABS se masoara in grame; rasina in mililitri."""
    return "ml" if tip.strip().lower() in ("rasina", "resin") else "g"


# ---------------------------------------------------------------------------
# ALERTE DE REAPROVIZIONARE
# ---------------------------------------------------------------------------

def verifica_alerta(material_row):
    """Returneaza True daca materialul e sub pragul minim (trebuie comandat)."""
    return material_row["cantitate_ramasa"] <= material_row["prag_minim"]


def afiseaza_alerte(conn):
    """Afiseaza in consola toate materialele aflate sub pragul minim."""
    randuri = conn.execute("SELECT * FROM materiale").fetchall()
    alerte = [r for r in randuri if verifica_alerta(r)]
    if alerte:
        print("\n*** ALERTA REAPROVIZIONARE ***")
        for r in alerte:
            print(f"  - {r['tip']} {r['culoare'] or ''}: mai ai {r['cantitate_ramasa']:.0f}{r['unitate']} "
                  f"(prag minim {r['prag_minim']:.0f}{r['unitate']}) -> COMANDA la {r['furnizor'] or 'furnizorul obisnuit'}!")
    return alerte


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
            print("  -> Te rog introdu un numar valid (ex: 250).")


def citeste_text(mesaj, implicit=None):
    text = input(mesaj).strip()
    if text == "" and implicit is not None:
        return implicit
    return text


def alege_material(conn, mesaj="Alege ID-ul materialului: "):
    """Afiseaza lista de materiale numerotate si returneaza randul ales."""
    randuri = conn.execute("SELECT * FROM materiale ORDER BY tip, culoare").fetchall()
    if not randuri:
        print("Nu exista niciun material inregistrat inca. Adauga unul mai intai (optiunea 1).")
        return None
    print("\nMateriale disponibile:")
    for r in randuri:
        alerta = "  [SUB PRAG!]" if verifica_alerta(r) else ""
        print(f"  ID {r['id']:>3}: {r['tip']} {r['culoare'] or ''} - {r['cantitate_ramasa']:.0f}{r['unitate']} ramase{alerta}")
    id_ales = citeste_numar(mesaj)
    rand = conn.execute("SELECT * FROM materiale WHERE id = ?", (int(id_ales),)).fetchone()
    if not rand:
        print("ID invalid.")
        return None
    return rand


# ---------------------------------------------------------------------------
# ACTIUNI DE MENIU
# ---------------------------------------------------------------------------

def actiune_adauga_material(conn):
    print("\n--- Material nou / alimentare stoc ---")
    tip = citeste_text("Tip material (PLA/PETG/ABS/Rasina): ")
    culoare = citeste_text("Culoare: ")
    unitate = unitate_pentru_tip(tip)
    cantitate = citeste_numar(f"Cantitate ({unitate}): ")
    cost = citeste_numar(f"Cost per kg/litru (lei): ")
    furnizor = citeste_text("Furnizor: ")
    prag_minim = citeste_numar(f"Prag minim de reaprovizionare ({unitate}) [implicit 200]: ", 200.0)

    # Daca exista deja un material identic (tip+culoare), intrebam daca vrem
    # sa adaugam la stocul existent in loc sa cream o inregistrare noua.
    existent = conn.execute(
        "SELECT * FROM materiale WHERE lower(tip)=lower(?) AND lower(coalesce(culoare,''))=lower(coalesce(?,''))",
        (tip, culoare),
    ).fetchone()

    acum = acum_iso()
    if existent:
        raspuns = citeste_text(
            f"Exista deja '{existent['tip']} {existent['culoare']}' cu {existent['cantitate_ramasa']:.0f}{existent['unitate']}. "
            f"Adaug {cantitate:.0f}{unitate} la stocul existent? (da/nu) [da]: ", "da")
        if raspuns.lower() in ("da", "d", "y", "yes"):
            noua_cantitate = existent["cantitate_ramasa"] + cantitate
            conn.execute("UPDATE materiale SET cantitate_ramasa=?, cost_per_kg_litru=?, furnizor=?, prag_minim=? WHERE id=?",
                         (noua_cantitate, cost, furnizor, prag_minim, existent["id"]))
            conn.execute("INSERT INTO miscari_stoc (material_id, tip_miscare, cantitate, motiv, data) VALUES (?,?,?,?,?)",
                         (existent["id"], "adaugare", cantitate, "alimentare stoc", acum))
            conn.commit()
            print(f"-> Stoc actualizat: {noua_cantitate:.0f}{unitate}.")
            return

    cursor = conn.execute("""
        INSERT INTO materiale (tip, culoare, unitate, cantitate_ramasa, cost_per_kg_litru, furnizor, prag_minim, data_adaugare)
        VALUES (?,?,?,?,?,?,?,?)
    """, (tip, culoare, unitate, cantitate, cost, furnizor, prag_minim, acum))
    conn.execute("INSERT INTO miscari_stoc (material_id, tip_miscare, cantitate, motiv, data) VALUES (?,?,?,?,?)",
                 (cursor.lastrowid, "adaugare", cantitate, "material nou", acum))
    conn.commit()
    print(f"-> Material adaugat cu ID {cursor.lastrowid}.")


def actiune_listeaza_materiale(conn):
    randuri = conn.execute("SELECT * FROM materiale ORDER BY tip, culoare").fetchall()
    if not randuri:
        print("\nNu exista inca niciun material inregistrat.")
        return
    print(f"\n{'ID':<4}{'Tip':<10}{'Culoare':<12}{'Stoc':>10}{'Prag minim':>12}{'Cost/kg-l':>14}  {'Furnizor':<15}")
    print("-" * 80)
    for r in randuri:
        semn = " !!" if verifica_alerta(r) else ""
        print(f"{r['id']:<4}{r['tip']:<10}{(r['culoare'] or ''):<12}{r['cantitate_ramasa']:>8.0f}{r['unitate']:<2}"
              f"{r['prag_minim']:>10.0f}{r['unitate']:<2}{r['cost_per_kg_litru']:>10.2f} lei  {(r['furnizor'] or ''):<15}{semn}")
    afiseaza_alerte(conn)


def actiune_scade_stoc_dupa_print(conn):
    print("\n--- Scade stoc dupa print finalizat ---")
    material = alege_material(conn, "ID material folosit la acest print: ")
    if material is None:
        return
    cantitate_folosita = citeste_numar(f"Cantitate folosita ({material['unitate']}): ")
    motiv = citeste_text("Nume produs / comanda (optional): ")

    noua_cantitate = material["cantitate_ramasa"] - cantitate_folosita
    if noua_cantitate < 0:
        print(f"  -> Atentie: cantitatea folosita depaseste stocul ramas ({material['cantitate_ramasa']:.0f}{material['unitate']}).")
        confirmare = citeste_text("  Continui oricum (stocul va ramane pe 0)? (da/nu) [nu]: ", "nu")
        if confirmare.lower() not in ("da", "d", "y", "yes"):
            print("Anulat.")
            return
        noua_cantitate = 0

    conn.execute("UPDATE materiale SET cantitate_ramasa=? WHERE id=?", (noua_cantitate, material["id"]))
    conn.execute("INSERT INTO miscari_stoc (material_id, tip_miscare, cantitate, motiv, data) VALUES (?,?,?,?,?)",
                 (material["id"], "consum", cantitate_folosita, motiv, acum_iso()))
    conn.commit()
    print(f"-> Stoc actualizat: {material['tip']} {material['culoare'] or ''} are acum {noua_cantitate:.0f}{material['unitate']}.")

    material_actualizat = conn.execute("SELECT * FROM materiale WHERE id=?", (material["id"],)).fetchone()
    if verifica_alerta(material_actualizat):
        print(f"  *** ALERTA: stocul a scazut sub pragul minim ({material_actualizat['prag_minim']:.0f}{material_actualizat['unitate']})! Comanda material. ***")


def actiune_modifica_prag(conn):
    print("\n--- Modifica prag de reaprovizionare ---")
    material = alege_material(conn, "ID material pentru care schimb pragul: ")
    if material is None:
        return
    prag_nou = citeste_numar(f"Prag minim nou ({material['unitate']}) [actual {material['prag_minim']:.0f}]: ", material["prag_minim"])
    conn.execute("UPDATE materiale SET prag_minim=? WHERE id=?", (prag_nou, material["id"]))
    conn.commit()
    print(f"-> Prag actualizat la {prag_nou:.0f}{material['unitate']}.")


def meniu_principal():
    conn = get_connection()
    init_tabele(conn)

    # La pornire, aratam direct daca exista alerte de reaprovizionare
    afiseaza_alerte(conn)

    while True:
        print("\n================ INVENTAR MATERIALE ================")
        print("1. Adauga material nou / alimenteaza stoc existent")
        print("2. Listeaza materiale (cu alerte)")
        print("3. Scade stoc dupa print finalizat")
        print("4. Modifica prag de reaprovizionare")
        print("0. Iesire")
        optiune = input("Alege o optiune: ").strip()

        if optiune == "1":
            actiune_adauga_material(conn)
        elif optiune == "2":
            actiune_listeaza_materiale(conn)
        elif optiune == "3":
            actiune_scade_stoc_dupa_print(conn)
        elif optiune == "4":
            actiune_modifica_prag(conn)
        elif optiune == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida, incearca din nou.")

    conn.close()


if __name__ == "__main__":
    meniu_principal()
