from names import make_full_name, extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    assert make_full_name("Brett", "Snyder") == "Snyder; Brett"
    assert make_full_name("Frank", "Loyd-Wright") == "Loyd-Wright; Frank"
    assert make_full_name("BB", "King") == "King; BB"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    assert extract_family_name("Snyder; Brett") == "Snyder"
    assert extract_family_name("Madison; James") == "Madison"
    assert extract_family_name("King; BB") == "King"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    assert extract_given_name("Snyder; Brett") == "Brett"
    assert extract_given_name("Madison; James") == "James"
    assert extract_given_name("King; BB") == "BB"
    assert extract_given_name("; ") == ""


pytest.main(["-v", "--tb=line", "-rN", __file__])
