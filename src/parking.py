"""
1. parking_spots
 id, lat, lng, address, city, country, reserved (bool), reserved_by, bill

"""

class ParkingSpots:
    def __init__(self):
        pass

    def list_available(self):
        query = "SELECT id, lat, lng, address FROM parking_spots WHERE reserved=0"

    def search(self, lat, lng radius):
        pass

    def reserve(self, spot_id, user_id):
        pass

