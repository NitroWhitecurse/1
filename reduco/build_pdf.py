#!/usr/bin/env python3
"""Construiește PDF-ul planului de remediere, proiectat pentru citit și prezentat."""

import re
import subprocess
from pathlib import Path

import markdown

BASE = Path(__file__).parent
SRC = BASE / "plan-remediere.md"
HTML = BASE / "plan-remediere-print.html"
PDF = BASE / "Reduco-Plan-de-remediere.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4; margin: 18mm 16mm 16mm 16mm; }

:root {
  --ink: #1A1A1A;
  --soft: #55625E;
  --faint: #7E8B87;
  --grid: #0F5C4E;
  --grid-wash: #EDF4F1;
  --copper: #A8481F;
  --copper-wash: #FAF0EA;
  --rule: #D3DAD7;
  --sunk: #F2F5F3;
  --sans: Helvetica, Arial, sans-serif;
  --serif: Georgia, "Times New Roman", serif;
  --mono: "Courier New", monospace;
}

* { box-sizing: border-box; }

body {
  font-family: var(--serif);
  font-size: 10.5pt;
  line-height: 1.55;
  color: var(--ink);
  margin: 0;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}

/* ---------- cover ---------- */

.cover {
  page-break-after: always;
  height: 245mm;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cover-top { border-top: 3pt solid var(--ink); padding-top: 8mm; }
.cover .brand {
  font-family: var(--mono);
  font-size: 9pt;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grid);
  margin-bottom: 28mm;
}
.cover h1 {
  font-family: var(--sans);
  font-size: 34pt;
  line-height: 1.03;
  letter-spacing: -0.025em;
  font-weight: bold;
  margin: 0 0 6mm;
  max-width: 15ch;
}
.cover .sub {
  font-size: 13pt;
  line-height: 1.4;
  color: var(--soft);
  max-width: 48ch;
  margin: 0;
}
.cover-foot {
  border-top: 1pt solid var(--rule);
  padding-top: 5mm;
  font-family: var(--mono);
  font-size: 8.5pt;
  color: var(--faint);
  letter-spacing: 0.02em;
  line-height: 1.7;
}
.cover-stats {
  display: flex;
  gap: 0;
  border-top: 1pt solid var(--rule);
}
.cover-stats div {
  flex: 1;
  padding: 6mm 6mm 6mm 0;
  border-right: 0.5pt solid var(--rule);
  margin-right: 6mm;
}
.cover-stats div:last-child { border-right: none; margin-right: 0; }
.cover-stats .n {
  font-family: var(--sans);
  font-size: 30pt;
  font-weight: bold;
  color: var(--grid);
  line-height: 1;
  display: block;
  margin-bottom: 3mm;
}
.cover-stats p {
  font-family: var(--sans);
  font-size: 9pt;
  line-height: 1.35;
  color: var(--soft);
  margin: 0;
}

/* ---------- headings ---------- */

h2 {
  font-family: var(--sans);
  font-size: 17pt;
  line-height: 1.15;
  letter-spacing: -0.018em;
  font-weight: bold;
  margin: 0 0 5mm;
  padding-top: 4mm;
  border-top: 2.5pt solid var(--ink);
  page-break-before: always;
  page-break-after: avoid;
}
h2.nobreak { page-break-before: auto; }

h3 {
  font-family: var(--sans);
  font-size: 9pt;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: bold;
  color: var(--grid);
  margin: 6mm 0 2mm;
  page-break-after: avoid;
}

h1 { font-family: var(--sans); font-size: 20pt; margin: 0 0 4mm; }

p { margin: 0 0 3mm; orphans: 3; widows: 3; }
strong { font-weight: bold; }
em { font-style: italic; }
code { font-family: var(--mono); font-size: 9pt; background: var(--sunk); padding: 0 1mm; }

ul, ol { margin: 0 0 3mm; padding-left: 6mm; }
li { margin-bottom: 1.5mm; }

blockquote {
  margin: 4mm 0;
  padding: 3mm 5mm;
  border-left: 2.5pt solid var(--grid);
  background: var(--grid-wash);
  font-family: var(--sans);
  font-size: 11pt;
  line-height: 1.4;
  page-break-inside: avoid;
}
blockquote p { margin: 0; }
blockquote p + p { margin-top: 2mm; }

hr { display: none; }

/* ---------- tables ---------- */

table {
  border-collapse: collapse;
  width: 100%;
  margin: 3mm 0 5mm;
  font-family: var(--sans);
  font-size: 8.5pt;
  page-break-inside: avoid;
}
th, td {
  text-align: left;
  vertical-align: top;
  padding: 2mm 2.5mm;
  border-bottom: 0.5pt solid var(--rule);
}
thead th {
  background: var(--sunk);
  font-size: 7.5pt;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-bottom: 1pt solid var(--ink);
}
tbody tr:last-child td { border-bottom: none; }

/* ---------- summary page ---------- */

.map { page-break-after: always; }
.map h1 {
  border-top: 3pt solid var(--ink);
  padding-top: 5mm;
}
.map table { font-size: 9pt; }
.map td.code {
  font-family: var(--mono);
  font-weight: bold;
  color: var(--copper);
  white-space: nowrap;
}
.sev { font-family: var(--sans); font-size: 7.5pt; text-transform: uppercase; letter-spacing: 0.06em; white-space: nowrap; }
.sev-mare { color: var(--copper); font-weight: bold; }
.sev-mediu { color: var(--soft); }

.howto {
  background: var(--sunk);
  padding: 4mm 5mm;
  margin: 0 0 6mm;
  page-break-inside: avoid;
}
.howto p { margin: 0 0 2mm; font-family: var(--sans); font-size: 9pt; }
.howto ul { margin: 0; font-family: var(--sans); font-size: 9pt; }

/* ---------- checklist ---------- */

ul.check { list-style: none; padding-left: 0; }
ul.check li {
  padding-left: 7mm;
  position: relative;
  margin-bottom: 2.5mm;
}
ul.check li::before {
  content: "";
  position: absolute;
  left: 0; top: 1.2mm;
  width: 3.6mm; height: 3.6mm;
  border: 1pt solid var(--soft);
}
"""

MAP_ROWS = [
    ("P1", "Ne prezentăm drept un comparator — adică exact ce face statul gratis", "mare", "Text, 2 săptămâni", "Marian + admin site"),
    ("P2", "Site-ul se încarcă prea greu, iar paginile pentru firme arată prețuri din 2022", "mare", "1 oră urgent, 30 zile complet", "Redactor + dezvoltator"),
    ("P3", "Grila de preț nu are nici podea, nici tavan", "mare", "Decizie", "CEO"),
    ("P4", "Nu măsurăm nimic — niciun eveniment de conversie definit", "mare", "1 săptămână", "Admin site"),
    ("P5", "Nu există un loc unic unde trăiesc leadurile", "mare", "1 zi", "Marian"),
    ("P6", "Datele de expirare a contractelor se pierd", "mediu", "1 zi", "Marian"),
    ("P7", "Raportul de optimizare nu e standardizat și nu are termen", "mediu", "2 săptămâni", "Marian"),
    ("P8", "Nu avem atestare — ne închide contractele obligatorii prin lege", "mare", "3 căi în paralel", "CEO decide"),
    ("P9", "Totul depinde de un singur om", "mare", "Decizie", "CEO"),
    ("P10", "Contractul de mandat are defecte care îl pot întoarce împotriva noastră", "mare", "1 oră", "Juristul firmei"),
]


def build_map():
    rows = []
    for code, desc, sev, effort, who in MAP_ROWS:
        cls = "sev-mare" if sev == "mare" else "sev-mediu"
        rows.append(
            f'<tr><td class="code">{code}</td><td>{desc}</td>'
            f'<td class="sev {cls}">{sev}</td><td>{effort}</td><td>{who}</td></tr>'
        )
    return f"""
<section class="map">
  <h1>Harta problemelor</h1>
  <p>Zece probleme confirmate. Nu sunt bănuieli — fiecare a fost verificată în documentele firmei,
  în contracte sau direct pe site. Ordinea de reparare e la sfârșitul documentului și nu coincide
  cu numerotarea: se repară întâi ce deblochează altceva.</p>
  <table>
    <thead><tr><th>Cod</th><th>Problema</th><th>Impact</th><th>Efort</th><th>Cine</th></tr></thead>
    <tbody>{''.join(rows)}</tbody>
  </table>
  <div class="howto">
    <p><strong>Cum se citește fiecare problemă din paginile următoare:</strong></p>
    <ul>
      <li><strong>Ce e stricat</strong> — descrierea, fără menajamente</li>
      <li><strong>Cât ne costă</strong> — de ce contează, în bani sau în leaduri pierdute</li>
      <li><strong>Reparația</strong> — pașii concreți, în ordine</li>
      <li><strong>Cine și până când</strong></li>
      <li><strong>Cum știm că e reparat</strong> — testul care spune da sau nu</li>
    </ul>
  </div>
</section>
"""


COVER = """
<section class="cover">
  <div class="cover-top">
    <div class="brand">Reduco &middot; ALMA SKY SRL</div>
    <h1>Plan de remediere</h1>
    <p class="sub">Zece probleme confirmate ale firmei, fiecare cu reparația explicată pas cu pas,
    responsabil, termen și testul care spune dacă a fost rezolvată.</p>
  </div>
  <div class="cover-stats">
    <div>
      <span class="n">10</span>
      <p>probleme confirmate, verificate în documentele firmei, în contracte și direct pe site</p>
    </div>
    <div>
      <span class="n">5</span>
      <p>se repară în prima săptămână, aproape fără cost — text, o coloană în tabel, o oră de corectură</p>
    </div>
    <div>
      <span class="n">3</span>
      <p>cer o decizie a CEO-ului înainte ca restul să poată porni</p>
    </div>
  </div>
  <div class="cover-foot">
    Document intern de lucru &middot; august 2026<br>
    Pregătit pentru ședința cu CEO
  </div>
</section>
"""


def main():
    md = SRC.read_text(encoding="utf-8")

    # Scoatem titlul și blocul introductiv — sunt înlocuite de copertă și de harta problemelor.
    md = re.sub(r"^# .*?\n", "", md, count=1)
    md = re.sub(
        r"Nu idei noi\..*?- \*\*Cum știm că e reparat\*\* — testul care spune da sau nu\n",
        "",
        md,
        flags=re.S,
    )
    # Notă devenită caducă după finalizarea secțiunilor.
    md = re.sub(r"\*Secțiunile P1.*?\*\s*$", "", md, flags=re.S)

    body = markdown.markdown(md, extensions=["tables", "sane_lists"])

    # Checklist-ul „Primele 7 zile" primește casete de bifat.
    body = body.replace("<li>[ ] ", "<li>").replace("[ ] ", "")
    body = re.sub(
        r"(<h2[^>]*>Primele 7 zile.*?</h2>\s*)<ul>",
        r'\1<ul class="check">',
        body,
        flags=re.S,
    )

    html = (
        "<!doctype html><html lang='ro'><head><meta charset='utf-8'>"
        "<title>Reduco — Plan de remediere</title>"
        f"<style>{CSS}</style></head><body>"
        f"{COVER}{build_map()}{body}"
        "</body></html>"
    )
    HTML.write_text(html, encoding="utf-8")

    subprocess.run(
        [
            CHROME,
            "--headless",
            "--no-sandbox",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={PDF}",
            HTML.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
    print(f"PDF scris: {PDF}  ({PDF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
