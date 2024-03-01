import pytest


def test_harness_solar_energy(function):
    try:
        assert function(2.0, 3.0) == 8.0
        passed = True
    except:
        passed = False
    
    return passed

def test_solve_riddle_of_sphinx(function):
    try:
        assert function('wisdom') == True
        assert function('not wisdom') == False
        passed = True
    except:
        passed = False

    return passed