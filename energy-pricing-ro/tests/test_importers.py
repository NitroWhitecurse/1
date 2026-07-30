from energy_pricing.importers import load_sample_offers


def test_load_sample_offers():
    offers = load_sample_offers()
    assert len(offers) == 10
    assert all(o.pret_energie_activa_lei_kwh > 0 for o in offers)
    assert all(o.furnizor for o in offers)
