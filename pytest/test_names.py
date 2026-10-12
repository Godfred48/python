from names import make_full_name, extract_family_name, extract_given_name
import pytest 

def test_make_full_name():
    fullname = make_full_name("Sally", "Brown")
    assert isinstance(fullname, str), "make_full_name must return a string"

    assert make_full_name("Godfred", "Agbogah") == "Agbogah;Godfred"
    assert make_full_name("Alfred", "Agbogah") == "Agbogah;Alfred"


def test_extract_family_name():
    familyname = extract_family_name("Sally; Brown")
    assert isinstance(familyname, str), "extract_family_name must return a string"

    assert extract_family_name("Agbogah; Godfred") == "Agbogah"
    assert extract_family_name("Agbogah; Alfred") == "Agbogah"

def test_extract_given_name():
    givenname = extract_given_name("Sally/ Brown")
    assert isinstance(givenname, str), "extract_given_name must return a string"

    assert extract_given_name("Agbogah/ Godfred") == "Godfred"
    assert extract_given_name("Agbogah/ Alfred") == "Alfred"

#call pytest
pytest.main(["-v", "--tb=line", "-rN", __file__])
