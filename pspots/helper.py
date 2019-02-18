import math

EARTH_RAD = 6378

def offset_lat(lat, distance):
    offset = (float(distance)/EARTH_RAD) * (180/math.pi)
    return offset


def offset_lng(lat, lng, distance):
    offset = (float(distance)/EARTH_RAD) * (180/math.pi) / math.cos(lat*math.pi/180)
    return offset

