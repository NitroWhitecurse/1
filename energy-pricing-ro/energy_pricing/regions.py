"""Loads Romania's electricity distribution regions and their regulated network tariffs.

Values live in data/regions.json (not hardcoded here) so they can be updated whenever
ANRE issues new transport/distribution tariff orders (typically each January and July)
without touching code. See the README for how to update them.
"""

import json
import unicodedata
from functools import lru_cache
from pathlib import Path

from energy_pricing.models import RegionTariffs

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "regions.json"


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return text.strip().lower()


@lru_cache(maxsize=1)
def _load_raw() -> dict:
    with open(DATA_FILE, encoding="utf-8") as f:
        return json.load(f)


@lru_cache(maxsize=1)
def load_regions() -> list[RegionTariffs]:
    raw = _load_raw()
    national = raw["national"]
    transport_lei_kwh = (
        national["transport_tl_lei_per_mwh"] + national["transport_servicii_sistem_lei_per_mwh"]
    ) / 1000
    cogenerare_lei_kwh = national["contributie_cogenerare_lei_per_mwh"] / 1000
    acciza_lei_kwh = national["acciza_necomerciala_lei_per_mwh"] / 1000

    regions = []
    for r in raw["regions"]:
        regions.append(
            RegionTariffs(
                id=r["id"],
                name=r["name"],
                former_name=r["former_name"],
                transport_lei_kwh=transport_lei_kwh,
                distributie_lei_kwh=r["distributie_jt_lei_per_mwh"] / 1000,
                contributie_cogenerare_lei_kwh=cogenerare_lei_kwh,
                acciza_lei_kwh=acciza_lei_kwh,
            )
        )
    return regions


def get_tva_rate() -> float:
    return _load_raw()["national"]["tva_rate"]


def get_data_as_of() -> str:
    return _load_raw()["as_of"]


def get_region(region_id: str) -> RegionTariffs:
    for region in load_regions():
        if region.id == region_id:
            return region
    raise KeyError(f"Unknown region id: {region_id!r}")


@lru_cache(maxsize=1)
def _county_index() -> dict[str, str]:
    raw = _load_raw()
    index = {}
    for r in raw["regions"]:
        for county in r["counties"]:
            index[_normalize(county)] = r["id"]
    return index


def region_for_county(county: str) -> RegionTariffs:
    """Look up the distribution region responsible for a given Romanian county (judet)."""
    key = _normalize(county)
    index = _county_index()
    if key not in index:
        known = ", ".join(sorted(index.keys()))
        raise KeyError(f"Unknown county {county!r}. Known counties: {known}")
    return get_region(index[key])


def list_counties() -> list[str]:
    raw = _load_raw()
    counties = []
    for r in raw["regions"]:
        counties.extend(r["counties"])
    return sorted(counties)
