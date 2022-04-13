# Testing file for ODF fire danger update

from ..src.services.updateFireDanger import getFireDangerConditions


def test_valid_location():
    # Corvallis:
    lat = 44.5646
    long = -123.2620
    r = getFireDangerConditions(lat, long)
    print(x)
    assert isinstance(r, list)


def test_swapped_coord():
    # Corvallis:
    lat = 44.5646
    long = -123.2620
    r = getFireDangerConditions(long, lat)
    assert r == -1


def test_bad_location():
    # Sydney, Australia
    lat = -33.8688
    long = 151.2093
    r = getFireDangerConditions(lat, long)
    assert r == -1
