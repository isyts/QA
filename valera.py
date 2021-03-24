import requests
import unittest

class TestStringMethods(unittest.TestCase):
    def test_create(self):
    	r = requests.post('http://petstore.swagger.io/v2/pet', data = {'id':'1616',"name": "valera"})
    	assert r.status_code == 200
    def test_read(self):
    	r = requests.get('http://petstore.swagger.io/v2/pet')
    	assert r.status_code == 200
    def test_update(self):
    	r = requests.get('http://petstore.swagger.io/v2/pet')
    	assert r.status_code == 200
    def test_delete(self):
    	r = requests.get('http://petstore.swagger.io/v2/pet')
    	assert r.status_code == 200
if __name__ == '__main__':
    unittest.main()