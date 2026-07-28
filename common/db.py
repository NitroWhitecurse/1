# -*- coding: utf-8 -*-
"""
Modul comun de conectare la baza de date SQLite.

Toate modulele (inventar, calculator, tracker, agent idei, dashboard)
folosesc ACELAȘI fișier de bază de date: data/business.db

De ce e important: toate modulele sunt independente (fiecare poate
rula singur, chiar dacă celelalte nu au fost pornite niciodată), dar
folosesc aceleași tabele ca să se poată "vedea" între ele (de exemplu,
calculatorul de cost poate citi stocul de materiale din inventar).

Fiecare modul își creează singur tabelele de care are nevoie, dacă nu
există deja (vezi "CREATE TABLE IF NOT EXISTS" în fiecare fișier).
Astfel poți rula orice modul, în orice ordine, fără erori.
"""

import os
import sqlite3

# Calea către folderul rădăcină al proiectului (un nivel deasupra "common/")
FOLDER_PROIECT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOLDER_DATE = os.path.join(FOLDER_PROIECT, "data")
CALE_BAZA_DATE = os.path.join(FOLDER_DATE, "business.db")


def get_connection():
    """
    Deschide (sau creează dacă nu există) baza de date SQLite și
    returnează o conexiune gata de folosit.

    Folosim row_factory = sqlite3.Row ca să putem accesa coloanele
    după nume (ex: rand["cantitate"]) în loc de index (rand[2]),
    ceea ce face codul mult mai ușor de citit.
    """
    os.makedirs(FOLDER_DATE, exist_ok=True)
    conexiune = sqlite3.connect(CALE_BAZA_DATE)
    conexiune.row_factory = sqlite3.Row
    # Activăm cheile străine (foreign keys) pentru integritatea datelor
    conexiune.execute("PRAGMA foreign_keys = ON;")
    return conexiune


def acum_iso():
    """Returnează data/ora curentă în format text standard (ex: 2026-07-28 13:45:00)."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
