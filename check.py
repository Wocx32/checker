from a1 import *
import pickle
import requests
import unittest

ENDPOINT = 'http://localhost:5000/test/a1'


def check_function(function):
    pickled_function = pickle.dumps(function)
    res = requests.post(ENDPOINT, data=pickled_function)

    if res.status_code == 200 and res.json().get('status'):
        return True
    
    raise Exception



class testcases(unittest.TestCase):

    def test_1(self):
        check_function(harness_solar_energy)

    def test_2(self):
        check_function(solve_riddle_of_sphinx)
        
        
    def test_3(self):
        check_function(concoct_elixir_of_life)

if __name__ == '__main__':
    unittest.main()
