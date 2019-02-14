

from flask import Flask

app = Flask(__name__)


@app.route("/parking", methods=['GET'])
def available_parking():
    """ List out available parking spots on map"""
    pass


@app.route("/search", methods=["POST"])
def search():
    """ Search for parking spot by lattitude, longitude & radius """
    pass


@app.route("/parking/reserve", methods=["POST"])
def reserve_parking():
    """ Reserve a given `spot_id` to `user_id`"""
    pass

@app.route("/my/reservations/<uid>", methods=["GET"])
def get_my_reservations(uid):
    """ Get my existing reservations """
    pass

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
    pass


@app.route("/login", methods=['POST'])
def login():
    pass

