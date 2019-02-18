import math
import hashlib

EARTH_RAD = 6378

def offset_lat(lat, distance):
    offset = (float(distance)/EARTH_RAD) * (180/math.pi)
    return offset


def offset_lng(lat, lng, distance):
    offset = (float(distance)/EARTH_RAD) * (180/math.pi) / math.cos(lat*math.pi/180)
    return offset

def generate_otp(data):
    """ dirty way to generate OTP w.o storing it at server """
    return long(hashlib.md5(data).hexdigest())%10000
