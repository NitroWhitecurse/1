import pytest

from energy_pricing.models import Offer
from energy_pricing.pricing import price_offer, price_offers
from energy_pricing.regions import region_for_county


@pytest.fixture
def region():
    return region_for_county("Cluj")


def test_price_offer_applies_tva_on_top_of_energy_plus_network(region):
    offer = Offer(
        furnizor="Test Supplier",
        denumire_oferta="Test Offer",
        tip_client="casnic",
        pret_energie_activa_lei_kwh=0.7,
        abonament_lunar_lei=0,
    )
    priced = price_offer(offer, region, monthly_consumption_kwh=100, tva_rate=0.21)

    expected_subtotal = 0.7 + region.total_lei_kwh
    assert priced.subtotal_lei_kwh == pytest.approx(expected_subtotal)
    assert priced.final_price_lei_kwh == pytest.approx(expected_subtotal * 1.21)
    assert priced.monthly_energy_cost_lei == pytest.approx(priced.final_price_lei_kwh * 100)
    assert priced.monthly_total_lei == pytest.approx(priced.monthly_energy_cost_lei)


def test_price_offer_includes_subscription_fee_with_tva(region):
    offer = Offer(
        furnizor="Test Supplier",
        denumire_oferta="Test Offer",
        tip_client="casnic",
        pret_energie_activa_lei_kwh=0.7,
        abonament_lunar_lei=10,
    )
    priced = price_offer(offer, region, monthly_consumption_kwh=100, tva_rate=0.21)

    assert priced.monthly_subscription_lei == pytest.approx(10 * 1.21)
    assert priced.monthly_total_lei == pytest.approx(
        priced.monthly_energy_cost_lei + priced.monthly_subscription_lei
    )


def test_price_offers_sorts_ascending_by_monthly_total(region):
    cheap = Offer("A", "A1", "casnic", 0.5, 0)
    expensive = Offer("B", "B1", "casnic", 0.9, 0)
    priced = price_offers([expensive, cheap], region, monthly_consumption_kwh=100, tva_rate=0.21)

    assert [p.offer.furnizor for p in priced] == ["A", "B"]
    assert priced[0].monthly_total_lei < priced[1].monthly_total_lei
