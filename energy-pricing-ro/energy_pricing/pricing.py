"""Computes the final price a Romanian household customer pays per kWh and per month,
starting from a supplier's active energy offer plus the regulated network costs for
their distribution region, TVA included.
"""

from energy_pricing.models import Offer, PricedOffer, RegionTariffs
from energy_pricing.regions import get_tva_rate


def price_offer(
    offer: Offer,
    region: RegionTariffs,
    monthly_consumption_kwh: float,
    tva_rate: float | None = None,
) -> PricedOffer:
    if tva_rate is None:
        tva_rate = get_tva_rate()

    network_costs_lei_kwh = region.total_lei_kwh
    subtotal_lei_kwh = offer.pret_energie_activa_lei_kwh + network_costs_lei_kwh
    final_price_lei_kwh = subtotal_lei_kwh * (1 + tva_rate)

    monthly_energy_cost_lei = final_price_lei_kwh * monthly_consumption_kwh
    monthly_subscription_lei = offer.abonament_lunar_lei * (1 + tva_rate)
    monthly_total_lei = monthly_energy_cost_lei + monthly_subscription_lei

    return PricedOffer(
        offer=offer,
        region=region,
        monthly_consumption_kwh=monthly_consumption_kwh,
        active_energy_lei_kwh=offer.pret_energie_activa_lei_kwh,
        network_costs_lei_kwh=network_costs_lei_kwh,
        subtotal_lei_kwh=subtotal_lei_kwh,
        tva_rate=tva_rate,
        final_price_lei_kwh=final_price_lei_kwh,
        monthly_energy_cost_lei=monthly_energy_cost_lei,
        monthly_subscription_lei=monthly_subscription_lei,
        monthly_total_lei=monthly_total_lei,
    )


def price_offers(
    offers: list[Offer],
    region: RegionTariffs,
    monthly_consumption_kwh: float,
    tva_rate: float | None = None,
) -> list[PricedOffer]:
    """Prices every offer for the given region/consumption and returns them ordered
    ascending by monthly total (i.e. cheapest offer for that customer first)."""
    priced = [
        price_offer(offer, region, monthly_consumption_kwh, tva_rate) for offer in offers
    ]
    priced.sort(key=lambda p: p.monthly_total_lei)
    return priced
