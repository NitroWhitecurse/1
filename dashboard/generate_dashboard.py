# -*- coding: utf-8 -*-
"""
MODUL 5: DASHBOARD SIMPLU
============================

Ce face acest modul:
- Citeste datele din baza de date SQLite (stoc, comenzi) si din fisierele
  de idei generate de agent, si genereaza O SINGURA pagina HTML statica:
  dashboard/dashboard.html

- Fisierul HTML e complet independent (CSS inclus in pagina, fara internet,
  fara server) - il poti deschide direct facand dublu-click pe el.

Cum rulezi (regenerezi dashboard-ul cu datele curente):
    python dashboard/generate_dashboard.py

Sau, mai simplu, ruleaza scriptul de pornire care regenereaza SI deschide
automat pagina in browser:
    python dashboard/porneste_dashboard.py

Daca un modul (inventar/comenzi/agent idei) nu a fost folosit inca, sectiunea
corespunzatoare din dashboard apare goala - nu primesti nicio eroare.
"""

import os
import sys
import glob
import re
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.db import get_connection

FOLDER_DASHBOARD = os.path.dirname(os.path.abspath(__file__))
FOLDER_PROIECT = os.path.dirname(FOLDER_DASHBOARD)
FOLDER_IDEI = os.path.join(FOLDER_PROIECT, "agent_idei", "idei")
CALE_HTML = os.path.join(FOLDER_DASHBOARD, "dashboard.html")

# Trebuie sa corespunda cu FLUX_STARI din comenzi/tracker.py
FLUX_STARI = ["Primita", "In slicing", "La imprimanta", "Post-procesare", "Ambalare", "Expediata"]


# ---------------------------------------------------------------------------
# COLECTARE DATE (fiecare functie e izolata - daca tabela nu exista, returnam gol)
# ---------------------------------------------------------------------------

def obtine_stoc_materiale(conn):
    try:
        randuri = conn.execute("SELECT * FROM materiale ORDER BY tip, culoare").fetchall()
    except Exception:
        return []
    materiale = []
    for r in randuri:
        raport = (r["cantitate_ramasa"] / r["prag_minim"]) if r["prag_minim"] else 999
        if raport <= 1.0:
            stare = "critical"
        elif raport <= 1.3:
            stare = "warning"
        else:
            stare = "good"
        materiale.append({
            "tip": r["tip"], "culoare": r["culoare"] or "-", "cantitate": r["cantitate_ramasa"],
            "unitate": r["unitate"], "prag": r["prag_minim"], "furnizor": r["furnizor"] or "-",
            "stare": stare, "raport": min(raport, 2.0),
        })
    return materiale


def obtine_comenzi_active(conn):
    try:
        randuri = conn.execute("SELECT stare, COUNT(*) as numar FROM comenzi WHERE stare != ? GROUP BY stare",
                                (FLUX_STARI[-1],)).fetchall()
    except Exception:
        return []
    counts = {r["stare"]: r["numar"] for r in randuri}
    return [{"stare": s, "numar": counts.get(s, 0)} for s in FLUX_STARI[:-1]]


def obtine_marja_medie_si_venit_30_zile(conn):
    prag = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
    try:
        randuri = conn.execute(
            "SELECT * FROM comenzi WHERE stare = ? AND data_ultima_schimbare >= ?",
            (FLUX_STARI[-1], prag)
        ).fetchall()
    except Exception:
        return None, 0.0, 0

    if not randuri:
        return None, 0.0, 0

    marje = []
    venit_total = 0.0
    for r in randuri:
        venit_comanda = r["pret_vanzare_unitate"] * r["cantitate"]
        cost_comanda = r["cost_estimat_unitate"] * r["cantitate"]
        venit_total += venit_comanda
        if r["pret_vanzare_unitate"] > 0:
            marje.append((r["pret_vanzare_unitate"] - r["cost_estimat_unitate"]) / r["pret_vanzare_unitate"] * 100)

    marja_medie = sum(marje) / len(marje) if marje else None
    return marja_medie, venit_total, len(randuri)


def obtine_ultimele_idei(numar=5):
    """Citeste titlurile din cel mai recent fisier idei-YYYY-MM-DD.md."""
    fisiere = sorted(glob.glob(os.path.join(FOLDER_IDEI, "idei-*.md")), reverse=True)
    if not fisiere:
        return None, []
    cale_recenta = fisiere[0]
    nume_fisier = os.path.basename(cale_recenta)
    with open(cale_recenta, "r", encoding="utf-8") as f:
        continut = f.read()
    titluri = re.findall(r"^## (.+)$", continut, re.MULTILINE)
    return nume_fisier, titluri[:numar]


# ---------------------------------------------------------------------------
# GENERARE HTML
# ---------------------------------------------------------------------------

def escape_html(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def randuri_html_stoc(materiale):
    if not materiale:
        return '<p class="gol">Nu exista inca materiale in inventar. Ruleaza <code>inventar/inventar.py</code>.</p>'

    culoare_bara = {"critical": "var(--status-critical)", "warning": "var(--status-warning)", "good": "var(--status-good)"}
    linii = ['<table><thead><tr><th>Material</th><th>Stoc</th><th>Prag minim</th><th>Furnizor</th><th>Nivel</th></tr></thead><tbody>']
    for m in materiale:
        procent_bara = min(m["raport"] / 2.0 * 100, 100)
        eticheta = {"critical": "Sub prag", "warning": "Aproape de prag", "good": "OK"}[m["stare"]]
        linii.append(f"""<tr>
            <td>{escape_html(m['tip'])} {escape_html(m['culoare'])}</td>
            <td class="numeric">{m['cantitate']:.0f}{m['unitate']}</td>
            <td class="numeric">{m['prag']:.0f}{m['unitate']}</td>
            <td>{escape_html(m['furnizor'])}</td>
            <td>
                <div class="bara-fundal"><div class="bara-umplere" style="width:{procent_bara:.0f}%;background:{culoare_bara[m['stare']]}"></div></div>
                <span class="badge badge-{m['stare']}">{eticheta}</span>
            </td>
        </tr>""")
    linii.append("</tbody></table>")
    return "\n".join(linii)


def randuri_html_comenzi(comenzi_active):
    if not comenzi_active or sum(c["numar"] for c in comenzi_active) == 0:
        return '<p class="gol">Nu exista comenzi active. Ruleaza <code>comenzi/tracker.py</code>.</p>'
    maxim = max(c["numar"] for c in comenzi_active) or 1
    linii = ['<div class="lista-status">']
    for c in comenzi_active:
        procent = (c["numar"] / maxim * 100) if maxim else 0
        linii.append(f"""<div class="rand-status">
            <span class="eticheta-status">{escape_html(c['stare'])}</span>
            <div class="bara-fundal"><div class="bara-umplere" style="width:{procent:.0f}%;background:var(--series-1)"></div></div>
            <span class="numar-status">{c['numar']}</span>
        </div>""")
    linii.append("</div>")
    return "\n".join(linii)


def randuri_html_idei(nume_fisier, titluri):
    if not nume_fisier:
        return '<p class="gol">Nu exista inca rapoarte de idei. Ruleaza <code>agent_idei/agent.py</code>.</p>'
    if not titluri:
        return f'<p class="gol">Ultimul raport ({escape_html(nume_fisier)}) nu contine idei noi.</p>'
    linii = [f'<p class="sub-info">Din raportul: <code>{escape_html(nume_fisier)}</code></p>', "<ul>"]
    for t in titluri:
        linii.append(f"<li>{escape_html(t)}</li>")
    linii.append("</ul>")
    return "\n".join(linii)


def genereaza_html(materiale, comenzi_active, marja_medie, venit_30, numar_comenzi_30, nume_fisier_idei, titluri_idei):
    total_alerte = sum(1 for m in materiale if m["stare"] == "critical")
    total_comenzi_active = sum(c["numar"] for c in comenzi_active)
    marja_text = f"{marja_medie:.0f}%" if marja_medie is not None else "N/A"

    data_generare = datetime.now().strftime("%Y-%m-%d %H:%M")

    html = f"""<!doctype html>
<html lang="ro">
<head>
<meta charset="utf-8">
<title>Dashboard Atelier 3D Print</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{
    color-scheme: light;
    --surface-1: #fcfcfb;
    --page: #f9f9f7;
    --text-primary: #0b0b0b;
    --text-secondary: #52514e;
    --muted: #898781;
    --gridline: #e1e0d9;
    --border: rgba(11,11,11,0.10);
    --series-1: #2a78d6;
    --status-good: #0ca30c;
    --status-warning: #fab219;
    --status-critical: #d03b3b;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      color-scheme: dark;
      --surface-1: #1a1a19;
      --page: #0d0d0d;
      --text-primary: #ffffff;
      --text-secondary: #c3c2b7;
      --muted: #898781;
      --gridline: #2c2c2a;
      --border: rgba(255,255,255,0.10);
      --series-1: #3987e5;
      --status-good: #0ca30c;
      --status-warning: #fab219;
      --status-critical: #d03b3b;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 24px; background: var(--page); color: var(--text-primary);
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  }}
  h1 {{ font-size: 1.5rem; margin: 0 0 4px; }}
  .subtitlu {{ color: var(--text-secondary); margin: 0 0 24px; font-size: 0.9rem; }}
  .grid-tile {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 12px; margin-bottom: 28px;
  }}
  .tile {{
    background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px;
    padding: 16px;
  }}
  .tile .eticheta {{ color: var(--text-secondary); font-size: 0.8rem; margin-bottom: 6px; }}
  .tile .valoare {{ font-size: 1.8rem; font-weight: 600; font-variant-numeric: proportional-nums; }}
  .tile .valoare.critical {{ color: var(--status-critical); }}
  .tile .valoare.good {{ color: var(--status-good); }}
  section {{
    background: var(--surface-1); border: 1px solid var(--border); border-radius: 10px;
    padding: 20px; margin-bottom: 20px;
  }}
  section h2 {{ font-size: 1.05rem; margin: 0 0 14px; }}
  table {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
  th {{ text-align: left; color: var(--text-secondary); font-weight: 500; font-size: 0.8rem;
        border-bottom: 1px solid var(--gridline); padding: 6px 8px; }}
  td {{ padding: 8px; border-bottom: 1px solid var(--gridline); vertical-align: middle; }}
  td.numeric {{ font-variant-numeric: tabular-nums; }}
  .bara-fundal {{ background: var(--gridline); border-radius: 4px; height: 6px; width: 120px; display: inline-block; vertical-align: middle; overflow: hidden; }}
  .bara-umplere {{ height: 100%; border-radius: 4px; }}
  .badge {{ display: inline-block; margin-left: 8px; padding: 2px 8px; border-radius: 999px; font-size: 0.75rem; }}
  .badge-critical {{ background: color-mix(in srgb, var(--status-critical) 18%, transparent); color: var(--status-critical); }}
  .badge-warning {{ background: color-mix(in srgb, var(--status-warning) 22%, transparent); color: #8a5a00; }}
  .badge-good {{ background: color-mix(in srgb, var(--status-good) 18%, transparent); color: var(--status-good); }}
  .lista-status {{ display: flex; flex-direction: column; gap: 10px; }}
  .rand-status {{ display: flex; align-items: center; gap: 12px; }}
  .eticheta-status {{ width: 140px; font-size: 0.9rem; }}
  .numar-status {{ font-variant-numeric: tabular-nums; width: 24px; text-align: right; color: var(--text-secondary); }}
  .rand-status .bara-fundal {{ flex: 1; width: auto; }}
  .gol {{ color: var(--muted); font-size: 0.9rem; }}
  .sub-info {{ color: var(--text-secondary); font-size: 0.85rem; margin: 0 0 8px; }}
  code {{ background: var(--gridline); padding: 1px 5px; border-radius: 4px; font-size: 0.85em; }}
  ul {{ margin: 0; padding-left: 20px; }}
  li {{ margin-bottom: 4px; }}
  footer {{ color: var(--muted); font-size: 0.8rem; text-align: center; margin-top: 24px; }}
</style>
</head>
<body>
  <h1>Dashboard Atelier 3D Print</h1>
  <p class="subtitlu">Generat la {data_generare}. Regenereaza cu <code>python dashboard/generate_dashboard.py</code>.</p>

  <div class="grid-tile">
    <div class="tile">
      <div class="eticheta">Materiale sub prag minim</div>
      <div class="valoare {'critical' if total_alerte else 'good'}">{total_alerte}</div>
    </div>
    <div class="tile">
      <div class="eticheta">Comenzi active</div>
      <div class="valoare">{total_comenzi_active}</div>
    </div>
    <div class="tile">
      <div class="eticheta">Marja medie (ultimele 30 zile)</div>
      <div class="valoare">{marja_text}</div>
    </div>
    <div class="tile">
      <div class="eticheta">Venit (ultimele 30 zile)</div>
      <div class="valoare">{venit_30:.0f} lei</div>
    </div>
  </div>

  <section>
    <h2>Stoc curent materiale</h2>
    {randuri_html_stoc(materiale)}
  </section>

  <section>
    <h2>Comenzi active pe status</h2>
    {randuri_html_comenzi(comenzi_active)}
  </section>

  <section>
    <h2>Ultimele idei de produse (agent cercetare)</h2>
    {randuri_html_idei(nume_fisier_idei, titluri_idei)}
  </section>

  <footer>Sistem local Python + SQLite - fara cloud. Datele nu parasesc acest calculator.</footer>
</body>
</html>
"""
    return html


def genereaza_dashboard():
    conn = get_connection()
    materiale = obtine_stoc_materiale(conn)
    comenzi_active = obtine_comenzi_active(conn)
    marja_medie, venit_30, numar_comenzi_30 = obtine_marja_medie_si_venit_30_zile(conn)
    nume_fisier_idei, titluri_idei = obtine_ultimele_idei()
    conn.close()

    html = genereaza_html(materiale, comenzi_active, marja_medie, venit_30, numar_comenzi_30, nume_fisier_idei, titluri_idei)
    with open(CALE_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"-> Dashboard generat: {CALE_HTML}")
    return CALE_HTML


if __name__ == "__main__":
    genereaza_dashboard()
