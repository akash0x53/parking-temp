import pytest
import unittest
from pspots.api import *


class TestParkingSpot(unittest.TestCase):
    
    def setUp(self):
        from pspots import app
        self.client = app.test_client()
    
    def test_list_all_available_spots(self):
        res = self.client.get('/spots')
        self.assertEqual(200, res.status_code)
        self.assertIsNotNone(res.json)

    def test_search_nearby(self):
        res = self.client.post('/search', \
                data={'lat':18.5167, 'lng': 73.8563, 'distance': 7})
        self.assertIsNotNone(res.json)

    def test_signup(self):
        res = self.client.post('/signup',\
                data={'name': 'Akash', 'phnumber': '+91-6377265738'})
        self.assertTrue(res.json.get('created', False))

    def test_reserve_spot(self):
        res = self.client.post('/parking/reserve',
                data={'spot_id': 1, 'user_id': 1})
        self.assertTrue(res.json.get('reserved'))
    
    def test_reserve_spot_failed(self):
        res = self.client.post('/parking/reserve',
                data={'spot_id': 12, 'user_id': 1})
        self.assertFalse(res.json.get('reserved'))

    def test_view_reservations(self):
        res = self.client.get('/my/reservations/1')
        self.assertIsNotNone(res.json)

    def test_cancel_reservation(self):
        pass

    def test_show_my_bill(self):
        pass



if __name__ == "__main__":
    unittest.main()
