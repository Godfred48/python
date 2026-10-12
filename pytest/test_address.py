from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    city = extract_city("525 S Center St, Rexburg, ID 83460")
    assert isinstance(city, str) , "making sure the vaalue returned is a string"

    assert extract_city("Diabase Street, Accra,GA 0233") == "Accra"


def test_extract_state():
    state = extract_state("525 S Center St, Rexburg, ID 83460")
    assert isinstance(state, str), "making sure the value retruned is a string"

    assert extract_state("Diabase Street, Accra, GA 0233") == "GA"

def test_extract_zipcode():
    zip_code = extract_zipcode("525 S Center St, Rexburg, ID 83460")
    assert isinstance(zip_code, str) , "making sure value returned is a string"

    assert extract_zipcode("Diabase Street, Accra, GA 0233") == "0233"
 
#call pytest
pytest.main(["-v", "--tb=line", "-rN", __file__])
