from pspots import app
from flask import jsonify, request
from pspots.db import Parking
from pspots.helper import *

@app.route("/spots", methods=['GET'])
def available_parking():
    """ List out available parking spots on map"""
    parking = Parking()
    res = parking.list_available()
    return jsonify(res)


@app.route("/search", methods=["POST"])
def search():
    """ Search for parking spot by lattitude, longitude & radius """
    lat = float(request.form['lat'])
    lng = float(request.form['lng'])
    km = int(request.form['distance'])

    off_lat = offset_lat(lat, km)
    off_lng = offset_lng(lat + off_lat, lng, km)

    parking = Parking()
    res = parking.search(lat, lng, off_lat, off_lng)
    return jsonify(res)


@app.route("/parking/reserve", methods=["POST"])
def reserve_parking():
    """ Reserve a given `spot_id` to `user_id`"""
    pass

@app.route("/my/reservations/<uid>", methods=["GET"])
def get_my_reservations(uid):
    """ Get my existing reservations """
    user = User()
    res = user.get_my_reservations()
    return jsonify(res)


@app.route("/parking/cancel", methods=["POST"])
def cancel_reservation():
    """ Cancel reserved parking spot """
    pass

@app.route("/my/bill")
def show_bill():
    pass

@app.route("/signup", methods=['POST'])
def signup():
    """ New user sign-up """
    name = request.form['name']
    number = request.form['phnumber']
    user = NewUser()
    try:
        user.create(name, number)
    except:
        return {'created': False}
    return {'created': True}
