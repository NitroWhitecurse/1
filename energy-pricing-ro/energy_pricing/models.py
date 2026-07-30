from dataclasses import dataclass


@dataclass
class Offer:
    """A single active-energy supply offer, as published on POSF/ANRE's offer comparator."""

    furnizor: str
    denumire_oferta: str
    tip_client: str
    pret_energie_activa_lei_kwh: float
    abonament_lunar_lei: float = 0.0
    durata_contract_luni: int | None = None
    sursa: str = ""


@dataclass
class RegionTariffs:
    """Regulated network cost components for one distribution region (lei/kWh, excl. TVA)."""

    id: str
    name: str
    former_name: str
    transport_lei_kwh: float
    distributie_lei_kwh: float
    contributie_cogenerare_lei_kwh: float
    acciza_lei_kwh: float

    @property
    def total_lei_kwh(self) -> float:
        return (
            self.transport_lei_kwh
            + self.distributie_lei_kwh
            + self.contributie_cogenerare_lei_kwh
            + self.acciza_lei_kwh
        )


@dataclass
class PricedOffer:
    """An offer priced for a specific region and consumption, TVA included."""

    offer: Offer
    region: RegionTariffs
    monthly_consumption_kwh: float
    active_energy_lei_kwh: float
    network_costs_lei_kwh: float
    subtotal_lei_kwh: float
    tva_rate: float
    final_price_lei_kwh: float
    monthly_energy_cost_lei: float
    monthly_subscription_lei: float
    monthly_total_lei: float
