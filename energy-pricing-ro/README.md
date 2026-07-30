# Pret energie electrica Romania

A local tool that imports active-energy supply offers (as published on **POSF**,
ANRE's official platform for comparing/switching electricity suppliers, at
[posf.ro](https://posf.ro)), orders them by price, adds Romania's regulated
network costs broken down by distribution region, and computes the final
price a household customer pays per kWh - TVA included.

## What it does

1. **Imports** active-energy offers (supplier, offer name, price per kWh, monthly
   subscription fee) from a CSV/JSON file exported from POSF's offer comparator,
   or from the bundled sample dataset.
2. **Orders** offers by final monthly price, cheapest first.
3. **Organizes the "other costs"** - transport, distribution, high-efficiency
   cogeneration contribution, and excise duty - by Romania's 4 electricity
   distribution regions (each covering a different set of counties/județe).
4. **Calculates the final price**, TVA included, in both a command-line report
   and a local web interface.

## About POSF and the data

POSF (*Platforma Online pentru Schimbarea Furnizorului*) is ANRE's platform for
comparing supplier offers and switching electricity/gas suppliers in Romania.
Its offer comparator (`posf.ro/comparator?comparatorType=electric`) is a
client-rendered app; at the time this was built there was no confirmed public,
unauthenticated JSON API for the per-offer price data (a plausible export
endpoint returned an auth error). Two things **do** work without a login and
are used directly by `energy_pricing.posf_client`:

- `GET https://posf.ro/broker/export/furnizor/operational` - registered suppliers
- `GET https://posf.ro/broker/export/operational` - registered network operators

For the actual offer prices, the supported workflow is:

1. Use POSF's comparator in your browser, filter by your county and consumption.
2. Export/copy the results into the CSV format described below (see
   `data/sample_offers.csv` for the template), **or**
3. If you find POSF's underlying JSON endpoint for the comparator (e.g. via your
   browser's DevTools Network tab while filtering results), point
   `energy_pricing.posf_client.fetch_offers(api_url, params)` at it - it's
   written generically to consume a JSON list of offer rows.

This keeps the tool honest about what it can reach automatically versus what
needs a manual export, rather than guessing at an API that might not exist.

### Offers file format (CSV or JSON)

| column | required | meaning |
|---|---|---|
| `furnizor` | yes | Supplier name |
| `denumire_oferta` | yes | Offer name |
| `tip_client` | yes | Customer type (e.g. `casnic` = household) |
| `pret_energie_activa_lei_kwh` | yes | Active energy price, lei/kWh, excl. TVA |
| `abonament_lunar_lei` | no | Fixed monthly subscription fee, excl. TVA (default 0) |
| `durata_contract_luni` | no | Contract length in months |
| `sursa` | no | Free-text note on where the row came from |

## Regulated network costs, by region

Romania has 4 electricity distribution regions, each with its own regulated
distribution tariff; transport, the cogeneration contribution, and the excise
duty are national. Values live in `data/regions.json`:

| Region | Formerly | Counties |
|---|---|---|
| Retele Electrice Romania | Enel Distributie | Arad, Caras-Severin, Hunedoara, Timis, Calarasi, Constanta, Ialomita, Tulcea, Ilfov, Giurgiu, Bucuresti |
| Delgaz Grid | E.ON Distributie | Botosani, Suceava, Neamt, Iasi, Bacau, Vaslui |
| Distributie Oltenia | CEZ Distributie | Arges, Dolj, Gorj, Mehedinti, Olt, Teleorman, Valcea |
| Distributie Energie Electrica Romania | Electrica Distributie | Prahova, Buzau, Dambovita, Braila, Galati, Vrancea, Cluj, Maramures, Satu Mare, Salaj, Bihor, Bistrita-Nasaud, Brasov, Alba, Sibiu, Mures, Harghita, Covasna |

**These tariffs (and the TVA rate) change periodically** - ANRE typically issues
new transport/distribution orders each January and July, and TVA/excise rates
follow tax law. `data/regions.json` is a snapshot as of the date recorded in
that file (`as_of` field); check it against a current ANRE order before relying
on this for real financial decisions, and just edit the JSON when values
change - nothing else needs to be touched.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### Command line

```bash
python -m energy_pricing.cli --county Cluj --consumption 200
python -m energy_pricing.cli --county Cluj --consumption 200 --offers path/to/exported_offers.csv
python -m energy_pricing.cli --list-counties
```

### Web interface

```bash
streamlit run app.py
```

Opens a local page where you pick a county and monthly consumption, optionally
upload your own offers file, and see offers ordered by final price alongside
the region's cost breakdown.

## Tests

```bash
pytest
```
