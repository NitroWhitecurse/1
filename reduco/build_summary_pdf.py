#!/usr/bin/env python3
"""Construiește PDF-ul rezumatului strategic pentru CEO — scurt, de citit dintr-o privire."""

import re
import subprocess
from pathlib import Path

import markdown

BASE = Path(__file__).parent
SRC = BASE / "rezumat-strategic-ceo.md"
HTML = BASE / "rezumat-strategic-print.html"
PDF = BASE / "Reduco-Rezumat-Strategic-CEO.pdf"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4; margin: 16mm 16mm 16mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 10.3pt;
  line-height: 1.5;
  color: #1A1A1A;
  margin: 0;
  -webkit-print-color-adjust: exact;
}
.eyebrow {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 8.5pt;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: #0F5C4E;
  border-top: 2.5pt solid #1A1A1A;
  padding-top: 3mm;
  margin-bottom: 2mm;
}
h1 {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 22pt;
  letter-spacing: -0.02em;
  margin: 0 0 6mm;
}
h2 {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 13.5pt;
  font-weight: bold;
  color: #1A1A1A;
  margin: 7mm 0 3mm;
  padding-top: 3mm;
  border-top: 1pt solid #D3DAD7;
  page-break-after: avoid;
}
h2:first-of-type { border-top: none; padding-top: 0; }
p { margin: 0 0 2.8mm; orphans: 3; widows: 3; }
strong { font-weight: bold; }
hr { border: none; border-top: 1pt solid #D3DAD7; margin: 6mm 0; }
blockquote {
  margin: 3mm 0;
  padding: 2.5mm 4.5mm;
  border-left: 2.5pt solid #0F5C4E;
  background: #EDF4F1;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 10pt;
  page-break-inside: avoid;
}
blockquote p { margin: 0; }
blockquote p + p { margin-top: 3mm; padding-top: 2.5mm; border-top: 0.5pt dashed #B6C1BD; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 3mm 0 4mm;
  font-family: Helvetica, Arial, sans-serif;
  font-size: 8.7pt;
  page-break-inside: avoid;
}
th, td { text-align: left; vertical-align: top; padding: 1.8mm 2.2mm; border-bottom: 0.5pt solid #D3DAD7; }
thead th { background: #F2F5F3; font-size: 7.6pt; letter-spacing: 0.07em; text-transform: uppercase; border-bottom: 1pt solid #1A1A1A; }
ol, ul { margin: 0 0 3mm; padding-left: 5.5mm; }
li { margin-bottom: 1.5mm; }
"""


def main():
    md = SRC.read_text(encoding="utf-8")
    md = re.sub(r"^# (.+)\n", "", md, count=1)
    title_match = re.search(r"^# (.+)$", SRC.read_text(encoding="utf-8"), re.M)
    title = title_match.group(1) if title_match else "Rezumat strategic"

    body = markdown.markdown(md, extensions=["tables"])
    body = body.replace("<hr />", "").replace("<hr>", "")

    html = (
        "<!doctype html><html lang='ro'><head><meta charset='utf-8'>"
        f"<title>{title}</title><style>{CSS}</style></head><body>"
        '<div class="eyebrow">Reduco &middot; ALMA SKY SRL &middot; pentru ședința cu CEO</div>'
        f"<h1>{title}</h1>"
        f"{body}"
        "</body></html>"
    )
    HTML.write_text(html, encoding="utf-8")

    subprocess.run(
        [
            CHROME, "--headless", "--no-sandbox", "--disable-gpu",
            "--no-pdf-header-footer", f"--print-to-pdf={PDF}", HTML.as_uri(),
        ],
        check=True, capture_output=True,
    )
    print(f"PDF scris: {PDF} ({PDF.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
