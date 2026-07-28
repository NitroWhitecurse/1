# -*- coding: utf-8 -*-
"""
Pornire rapida a dashboard-ului: regenereaza fisierul HTML cu datele curente
si il deschide automat in browser-ul implicit.

Cum rulezi:
    python dashboard/porneste_dashboard.py
"""

import webbrowser
from generate_dashboard import genereaza_dashboard

if __name__ == "__main__":
    cale = genereaza_dashboard()
    webbrowser.open(f"file://{cale}")
