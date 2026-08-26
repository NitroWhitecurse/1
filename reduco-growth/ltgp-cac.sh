#!/usr/bin/env bash
# LTGP:CAC de bază pentru Reduco. Vezi ltgp-cac.md pentru formula si context.
set -euo pipefail

if [ "$#" -ne 5 ]; then
  echo "Usage: $0 <abonament_anual> <comisioane_switch_an> <ani_durata_relatie> <cost_livrare_an> <cac>"
  exit 1
fi

abonament="$1"
comisioane="$2"
ani="$3"
cost_livrare="$4"
cac="$5"

python3 - "$abonament" "$comisioane" "$ani" "$cost_livrare" "$cac" <<'EOF'
import sys

abonament, comisioane, ani, cost_livrare, cac = (float(x) for x in sys.argv[1:6])

valoare_anuala = abonament + comisioane
ltv_brut = valoare_anuala * ani
ltgp = ltv_brut - (cost_livrare * ani)
raport = ltgp / cac if cac else float("inf")

print(f"Valoare anuala client: {valoare_anuala:.2f} Lei")
print(f"LTV brut ({ani:.1f} ani): {ltv_brut:.2f} Lei")
print(f"LTGP: {ltgp:.2f} Lei")
print(f"CAC: {cac:.2f} Lei")
print(f"Raport LTGP:CAC: {raport:.2f}:1  (tinta cadru: >= 3:1)")
EOF
