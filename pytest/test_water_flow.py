from water_flow import water_column_height, pressure_gain_from_water_height
from pytest import approx # this is used for float values
import pytest 

def test_water_column_height():
    column = water_column_height(0.0, 0.0) 
    assert isinstance(column, float) , "making sure value returned is a float"

    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    pressure_gain = pressure_gain_from_water_height(0.0)
    assert isinstance(pressure_gain, float) , "making sure value returned is a float"

    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

    



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])