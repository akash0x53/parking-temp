import unittest
from pspots.helper import offset_lat, offset_lng

class TestCoordinates(unittest.TestCase):

    def setUp(self):
        self.lat = 18.532758
        self.lng = 73.824273
    
    def test_1km_from_current(self):
        km = 1

        new_lat = offset_lat(self.lat, 1)
        new_lng = offset_lng(self.lat + new_lat, self.lng, km)

        self.assertEqual(18.54174134580011, self.lat + new_lat)
        self.assertEqual(73.83374818123819, self.lng + new_lng)
    
    def test_7km_from_current(self):
        km = 7

        new_lat = offset_lat(self.lat, km)
        new_lng = offset_lng(self.lat + new_lat, self.lng, km)
        
        self.assertEqual(18.59564142060075, self.lat + new_lat)
        self.assertEqual(73.8906202323904, self.lng + new_lng)

if __name__ == "__main__":
    unittest.main()
