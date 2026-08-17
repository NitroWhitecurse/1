#!/usr/bin/env python3
"""Construiește PDF-ul planului de creștere a brandului Reduco."""

import re
import subprocess
from pathlib import Path

import markdown

BASE = Path(__file__).parent
SRC = BASE / "plan-crestere-brand.md"
HTML = BASE / "plan-crestere-print.html"
PDF = BASE / "Reduco-Plan-de-crestere.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4; margin: 17mm 16mm 16mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 10.4pt; line-height: 1.55; color: #1A1A1A; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
.cover { page-break-after: always; height: 244mm; display: flex; flex-direction: column; justify-content: space-between; }
.cover-top { border-top: 3pt solid #1A1A1A; padding-top: 8mm; }
.cover .brand { font-family: "Courier New", monospace; font-size: 9pt; letter-spacing: 0.18em; text-transform: uppercase; color: #0F5C4E; margin-bottom: 24mm; }
.cover h1 { font-family: Helvetica, Arial, sans-serif; font-size: 33pt; line-height: 1.04; letter-spacing: -0.025em; font-weight: bold; margin: 0 0 6mm; max-width: 16ch; }
.cover .sub { font-size: 12.5pt; line-height: 1.45; color: #55625E; max-width: 50ch; margin: 0; }
.cover-stats { display: flex; border-top: 1pt solid #D3DAD7; }
.cover-stats div { flex: 1; padding: 6mm 6mm 6mm 0; border-right: 0.5pt solid #D3DAD7; margin-right: 6mm; }
.cover-stats div:last-child { border-right: none; margin-right: 0; }
.cover-stats .n { font-family: Helvetica, Arial, sans-serif; font-size: 28pt; font-weight: bold; color: #0F5C4E; line-height: 1; display: block; margin-bottom: 3mm; }
.cover-stats p { font-family: Helvetica, Arial, sans-serif; font-size: 8.8pt; line-height: 1.35; color: #55625E; margin: 0; }
.cover-foot { border-top: 1pt solid #D3DAD7; padding-top: 4mm; font-family: "Courier New", monospace; font-size: 8.5pt; color: #7E8B87; line-height: 1.7; }

h2 {
  font-family: Helvetica, Arial, sans-serif; font-size: 16pt; line-height: 1.15;
  letter-spacing: -0.018em; font-weight: bold; margin: 0 0 5mm;
  padding-top: 4mm; border-top: 2.5pt solid #1A1A1A;
  page-break-before: always; page-break-after: avoid;
}
h3 {
  font-family: Helvetica, Arial, sans-serif; font-size: 11.5pt; font-weight: bold;
  color: #0F5C4E; margin: 6mm 0 2.5mm; page-break-after: avoid;
}
p { margin: 0 0 3mm; orphans: 3; widows: 3; }
strong { font-weight: bold; } em { font-style: italic; }
code { font-family: "Courier New", monospace; font-size: 9pt; background: #F2F5F3; padding: 0 1mm; }
ul, ol { margin: 0 0 3mm; padding-left: 6mm; } li { margin-bottom: 1.6mm; }
blockquote { margin: 3.5mm 0; padding: 3mm 5mm; border-left: 2.5pt solid #0F5C4E; background: #EDF4F1; font-family: Helvetica, Arial, sans-serif; font-size: 10pt; page-break-inside: avoid; }
blockquote p { margin: 0; }
hr { display: none; }
table { border-collapse: collapse; width: 100%; margin: 3mm 0 5mm; font-family: Helvetica, Arial, sans-serif; font-size: 8.4pt; page-break-inside: avoid; }
th, td { text-align: left; vertical-align: top; padding: 1.9mm 2.3mm; border-bottom: 0.5pt solid #D3DAD7; }
thead th { background: #F2F5F3; font-size: 7.4pt; letter-spacing: 0.08em; text-transform: uppercase; border-bottom: 1pt solid #1A1A1A; }
tbody tr:last-child td { border-bottom: none; }
a { color: #0F5C4E; }
"""

COVER = """
<section class="cover">
  <div class="cover-top">
    <div class="brand">Reduco &middot; ALMA SKY SRL</div>
    <h1>Plan de cre&#537;tere a brandului</h1>
    <p class="sub">Cre&#537;terea afacerii &#537;i aducerea de clien&#539;i noi persoan&#259; juridic&#259; &mdash;
    o funda&#539;ie, trei motoare de achizi&#539;ie &#537;i trei ferestre care se &icirc;nchid &icirc;n s&#259;pt&#259;m&acirc;ni.</p>
  </div>
  <div class="cover-stats">
    <div><span class="n">3</span><p>motoare de clien&#539;i noi, aprinse &icirc;n ordine: recolta proprie, conformarea &#537;i banii publici, agregarea</p></div>
    <div><span class="n">3</span><p>ferestre cu termen &icirc;n s&#259;pt&#259;m&acirc;ni: criza energetic&#259; din august, SME Eco-Tech (24 sept), Programul de eficien&#539;&#259; (30 sept)</p></div>
    <div><span class="n">8</span><p>numere urm&#259;rite s&#259;pt&#259;m&acirc;nal &icirc;n &#537;edin&#539;a cu CEO</p></div>
  </div>
  <div class="cover-foot">
    Document intern de lucru &middot; august 2026<br>
    Surse: 7 analize &icirc;n acela&#537;i folder &mdash; pozi&#539;ionare, remediere (P1&ndash;P10), audit + re-audit site,
    cercetare competitiv&#259; RO/UK/IT/PL, economia modelelor de venit, declan&#537;atoare de reglementare,
    cercetare independent&#259; august 2026
  </div>
</section>
"""


def main():
    md = SRC.read_text(encoding="utf-8")
    md = re.sub(r"^# .*?\n", "", md, count=1)
    # Scoatem blocul de metadate de sub titlu — îl acoperă coperta.
    md = re.sub(r"\*\*Obiectiv:\*\*.*?citează documentul-sursă din același folder\.\n", "", md, flags=re.S)

    body = markdown.markdown(md, extensions=["tables", "sane_lists"])
    # Prima secțiune nu are nevoie de page-break (vine imediat după copertă).
    body = body.replace("<h2>", '<h2 style="page-break-before:auto">', 1)

    html = (
        "<!doctype html><html lang='ro'><head><meta charset='utf-8'>"
        "<title>Reduco — Plan de creștere</title>"
        f"<style>{CSS}</style></head><body>{COVER}{body}</body></html>"
    )
    HTML.write_text(html, encoding="utf-8")
    subprocess.run(
        [CHROME, "--headless", "--no-sandbox", "--disable-gpu",
         "--no-pdf-header-footer", f"--print-to-pdf={PDF}", HTML.as_uri()],
        check=True, capture_output=True,
    )
    print(f"PDF scris: {PDF} ({PDF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
