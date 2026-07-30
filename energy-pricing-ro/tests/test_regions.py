import pytest

from energy_pricing.regions import get_tva_rate, list_counties, load_regions, region_for_county


def test_loads_four_regions():
    regions = load_regions()
    assert len(regions) == 4
    assert {r.id for r in regions} == {"rer", "delgaz", "oltenia", "deer"}


def test_region_for_county_known():
    region = region_for_county("Cluj")
    assert region.id == "deer"


def test_region_for_county_accepts_diacritics_and_case():
    assert region_for_county("cluj").id == "deer"
    assert region_for_county("Bucuresti").id == "rer"


def test_region_for_county_unknown_raises():
    with pytest.raises(KeyError):
        region_for_county("Atlantida")


def test_list_counties_nonempty():
    assert len(list_counties()) > 30


def test_tva_rate_is_reasonable():
    assert 0 < get_tva_rate() < 1


def test_region_total_is_sum_of_components():
    region = region_for_county("Dolj")
    assert region.total_lei_kwh == pytest.approx(
        region.transport_lei_kwh
        + region.distributie_lei_kwh
        + region.contributie_cogenerare_lei_kwh
        + region.acciza_lei_kwh
    )
