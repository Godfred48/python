from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
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

def test_pressure_loss_from_pipe():
    pressure_loss = pressure_loss_from_pipe(0.048692, 0.00, 0.018, 0.018) 
    assert isinstance(pressure_loss, float) , "making sure value retuurned is float"

    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75,) == approx(0.0000, abs=0.0001)

def test_pressure_loss_from_fittings():
    pressure_loss_ff = pressure_loss_from_fittings(0.00, 3) , "making sure value returned is flooat"
    assert isinstance(pressure_loss_ff, float) == approx(0.000 ,abs= 0.001) 

    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000 ,abs=0.001)

def test_reynolds_number():
    reynolds = reynolds_number(0.048692, 0.00)
    assert isinstance(reynolds, float) , 'making sure value returned is a float'

    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)

def test_pressure_loss_fpr():
    pressure_loss_fpr = pressure_loss_from_pipe_reduction(0.28687, 0.00, 1,	0.048692)
    assert isinstance(pressure_loss_fpr, float) , 'making sure value returned is float'

    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-164.015, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75,	500318, 0.048692) == approx(-184.487, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])