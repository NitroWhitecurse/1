"""Command-line report: import offers, order by final price, break down region costs.

Usage:
    python -m energy_pricing.cli --county Cluj --consumption 200
    python -m energy_pricing.cli --county Cluj --consumption 200 --offers data/sample_offers.csv
    python -m energy_pricing.cli --list-counties
"""

import argparse
import sys

from energy_pricing.importers import load_offers, load_sample_offers
from energy_pricing.pricing import price_offers
from energy_pricing.regions import get_data_as_of, list_counties, region_for_county


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--county", help="Romanian county (judet), e.g. Cluj, Ilfov, Dolj")
    parser.add_argument(
        "--consumption", type=float, default=150.0, help="Monthly consumption in kWh (default: 150)"
    )
    parser.add_argument(
        "--offers",
        help="Path to a .csv/.json offers file exported from POSF. Defaults to the bundled sample data.",
    )
    parser.add_argument(
        "--list-counties", action="store_true", help="Print all known counties and exit"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.list_counties:
        for county in list_counties():
            print(county)
        return 0

    if not args.county:
        print("error: --county is required (or pass --list-counties)", file=sys.stderr)
        return 2

    region = region_for_county(args.county)
    offers = load_offers(args.offers) if args.offers else load_sample_offers()
    priced = price_offers(offers, region, args.consumption)

    print(f"Region: {region.name} (formerly {region.former_name}) - county: {args.county}")
    print(f"Regulated tariffs as of: {get_data_as_of()}")
    print(
        f"Network costs (transport + distributie + cogenerare + acciza): "
        f"{region.total_lei_kwh:.4f} lei/kWh (excl. TVA)"
    )
    print(f"Monthly consumption: {args.consumption:.0f} kWh\n")

    header = (
        f"{'Furnizor':<28} {'Oferta':<22} {'Energie activa':>15} "
        f"{'Pret final':>12} {'Total lunar':>13}"
    )
    print(header)
    print("-" * len(header))
    for p in priced:
        print(
            f"{p.offer.furnizor:<28} {p.offer.denumire_oferta:<22} "
            f"{p.active_energy_lei_kwh:>13.4f} lei "
            f"{p.final_price_lei_kwh:>10.4f} lei "
            f"{p.monthly_total_lei:>11.2f} lei"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
