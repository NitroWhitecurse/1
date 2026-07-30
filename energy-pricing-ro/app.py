"""Local web interface: import offers, order by price, break down region costs, and
show the final price (TVA included) a Romanian household customer pays.

Run with: streamlit run app.py
"""

import pandas as pd
import streamlit as st

from energy_pricing.importers import load_offers_from_csv, load_offers_from_json, load_sample_offers
from energy_pricing.pricing import price_offers
from energy_pricing.regions import (
    get_data_as_of,
    get_tva_rate,
    list_counties,
    load_regions,
    region_for_county,
)

st.set_page_config(page_title="Pret energie electrica Romania", page_icon="⚡", layout="wide")

st.title("⚡ Pret energie electrica pentru clienti casnici din Romania")
st.caption(
    "Importa oferte de energie activa (ex. exportate de pe comparatorul POSF/ANRE), "
    "sorteaza-le dupa pret, si vezi costul final pe regiune, TVA inclus."
)

with st.sidebar:
    st.header("Date de intrare")

    uploaded = st.file_uploader("Importa oferte (.csv sau .json)", type=["csv", "json"])
    if uploaded is not None:
        suffix = uploaded.name.rsplit(".", 1)[-1].lower()
        if suffix == "json":
            offers = load_offers_from_json(uploaded)
        else:
            offers = load_offers_from_csv(uploaded)
        st.success(f"{len(offers)} oferte importate din {uploaded.name}")
    else:
        offers = load_sample_offers()
        st.info(f"Se folosesc {len(offers)} oferte exemplu (incarca un fisier pentru date reale)")

    counties = list_counties()
    county = st.selectbox("Judet", counties, index=counties.index("Cluj") if "Cluj" in counties else 0)
    consumption = st.slider("Consum lunar (kWh)", min_value=50, max_value=1000, value=150, step=10)

    st.divider()
    st.caption(f"Tarife reglementate valabile de la: {get_data_as_of()}")
    st.caption(
        "Tarifele de retea (transport, distributie, cogenerare, acciza) si TVA "
        "sunt incarcate din data/regions.json - actualizeaza-le cand ANRE emite "
        "ordine noi (de regula ianuarie si iulie)."
    )

region = region_for_county(county)
priced_offers = price_offers(offers, region, consumption)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"Oferte ordonate dupa pret final ({region.name})")
    rows = [
        {
            "Furnizor": p.offer.furnizor,
            "Oferta": p.offer.denumire_oferta,
            "Energie activa (lei/kWh)": round(p.active_energy_lei_kwh, 4),
            "Costuri retea (lei/kWh)": round(p.network_costs_lei_kwh, 4),
            "Subtotal fara TVA (lei/kWh)": round(p.subtotal_lei_kwh, 4),
            "Pret final cu TVA (lei/kWh)": round(p.final_price_lei_kwh, 4),
            "Abonament lunar cu TVA (lei)": round(p.monthly_subscription_lei, 2),
            "Total lunar estimat (lei)": round(p.monthly_total_lei, 2),
        }
        for p in priced_offers
    ]
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    if priced_offers:
        cheapest = priced_offers[0]
        st.success(
            f"Cea mai ieftina oferta pentru {consumption:.0f} kWh/luna in "
            f"{region.name}: **{cheapest.offer.furnizor} - {cheapest.offer.denumire_oferta}**, "
            f"~{cheapest.monthly_total_lei:.2f} lei/luna (TVA inclus)."
        )

with col2:
    st.subheader("Defalcare costuri regiune")
    st.metric("Regiune de distributie", region.name, region.former_name)
    breakdown = {
        "Transport (Transelectrica)": region.transport_lei_kwh,
        "Distributie (JT)": region.distributie_lei_kwh,
        "Contributie cogenerare": region.contributie_cogenerare_lei_kwh,
        "Acciza necomerciala": region.acciza_lei_kwh,
    }
    st.dataframe(
        pd.DataFrame(
            {"Componenta": breakdown.keys(), "lei/kWh (fara TVA)": [round(v, 4) for v in breakdown.values()]}
        ),
        use_container_width=True,
        hide_index=True,
    )
    st.metric("Total costuri retea (fara TVA)", f"{region.total_lei_kwh:.4f} lei/kWh")
    st.metric("Cota TVA", f"{get_tva_rate() * 100:.0f}%")

st.divider()
st.subheader("Toate regiunile de distributie")
all_regions_rows = [
    {
        "Regiune": r.name,
        "Fost nume": r.former_name,
        "Transport (lei/kWh)": round(r.transport_lei_kwh, 4),
        "Distributie JT (lei/kWh)": round(r.distributie_lei_kwh, 4),
        "Cogenerare (lei/kWh)": round(r.contributie_cogenerare_lei_kwh, 4),
        "Acciza (lei/kWh)": round(r.acciza_lei_kwh, 4),
        "Total retea (lei/kWh)": round(r.total_lei_kwh, 4),
    }
    for r in load_regions()
]
st.dataframe(pd.DataFrame(all_regions_rows), use_container_width=True, hide_index=True)
