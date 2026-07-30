"""Loads active-energy offers from a local file, in whatever format they were exported
from posf.ro's offer comparator (or the bundled sample dataset).

Expected columns (Romanian, matching POSF's own labels):
    furnizor, denumire_oferta, tip_client, pret_energie_activa_lei_kwh,
    abonament_lunar_lei (optional), durata_contract_luni (optional), sursa (optional)
"""

import csv
import json
from pathlib import Path

from energy_pricing.models import Offer

REQUIRED_COLUMNS = {"furnizor", "denumire_oferta", "tip_client", "pret_energie_activa_lei_kwh"}


def _row_to_offer(row: dict) -> Offer:
    missing = REQUIRED_COLUMNS - row.keys()
    if missing:
        raise ValueError(f"Offer row is missing required column(s): {sorted(missing)}")
    return Offer(
        furnizor=row["furnizor"],
        denumire_oferta=row["denumire_oferta"],
        tip_client=row["tip_client"],
        pret_energie_activa_lei_kwh=float(row["pret_energie_activa_lei_kwh"]),
        abonament_lunar_lei=float(row.get("abonament_lunar_lei") or 0),
        durata_contract_luni=(
            int(row["durata_contract_luni"]) if row.get("durata_contract_luni") else None
        ),
        sursa=row.get("sursa", ""),
    )


def load_offers_from_csv(path: str | Path) -> list[Offer]:
    with open(path, newline="", encoding="utf-8") as f:
        return [_row_to_offer(row) for row in csv.DictReader(f)]


def load_offers_from_json(path: str | Path) -> list[Offer]:
    with open(path, encoding="utf-8") as f:
        rows = json.load(f)
    return [_row_to_offer(row) for row in rows]


def load_offers(path: str | Path) -> list[Offer]:
    """Dispatches to the right loader based on file extension."""
    path = Path(path)
    if path.suffix.lower() == ".json":
        return load_offers_from_json(path)
    if path.suffix.lower() == ".csv":
        return load_offers_from_csv(path)
    raise ValueError(
        f"Unsupported offers file type: {path.suffix!r}. Use .csv or .json "
        "(export .xlsx from Excel/POSF as .csv first)."
    )


def load_sample_offers() -> list[Offer]:
    sample_path = Path(__file__).resolve().parent.parent / "data" / "sample_offers.csv"
    return load_offers_from_csv(sample_path)
