import pymysql
import hashlib

"""
Datbase
----

1. parking_spots
 id, lat, lng, address, city, country, reserved (bool), reserved_by, bill

2. users
id, name, phone_num, passwd

3. reservations
id, user_id, duration, bill
"""

class MySQL:
    def __init__(self, *args, **kwargs):
        self.conn = None
        self.dbargs = kwargs

    def __connect(self, username='root', password='@Securly', host='localhost', database='parkings', **kwargs):
        try:
            self.conn.ping()
        except:
            self.conn = pymysql.connect(
                    host=host,
                    user=username,
                    passwd=password,
                    db=database)

    def get_cursor(self):
        """Returns cursor object and checks MySQL connection before.
        """
        self.__connect(**self.dbargs)
        return self.conn.cursor()


class User:
    def __init__(self):
        self.mysql = MySQL()

    def login(self, number, passwd):
        query = "SELECT id, name FROM parkings.users WHERE number=%s AND\
                passwd=%s"
        cursor = self.mysql.get_cursor()
        cursor.execute(query, (number, hashlib.md5(passwd).hexdigest()))
        res = cursor.fetchone()
        if not res:
            raise ValueError("Unauthorized user")
        self.id = res[0]

    def my_reservations(self, uid):
        query = "SELECT *FROM spots WHERE reserved_by = %s"
        cursor = self.mysql.get_cursor()
        cursor.execute(query, (uid,))
        return cursor.fetchall()

    def reserve(self, spot_id, uid):
        query = "UPDATE spots SET reserved_by=%s WHERE id=%s AND reserved_by=0"
        cursor = self.mysql.get_cursor()
        cursor.execute(query, (uid, spot_id))
        return True

class NewUser:
    def __init__(self, name, number, passwd):
        self.name = name
        self.number = number
        self.mysql = MySQL()

    def create(self):
        cursor = self.mysql.get_cursor()
        query = "INSERT INTO users(name, phone) VALUES(%s, %s)"
        cursor.execute(query, (self.name, self.number))
        return True


class Parking:
    def __init__(self):
        self.mysql = MySQL()

    def list_available(self):
        cursor = self.mysql.get_cursor()
        query = "SELECT id, lat, lng, address, city FROM spots WHERE\
                reserved = 0"
        cursor.execute(query)
        return cursor.fetchall()

    def search(self, lat, lng, dlat, dlng):
        lat_min = lat-dlat
        lat_max = lat+dlat
        lng_min = lng-dlng
        lng_max = lng+dlng
        print lat_min

        query = "SELECT id, lat, lng FROM spots WHERE\
                (lat >= %s AND lat <= %s) AND (lng >= %s AND lng <= %s)"
        cursor = self.mysql.get_cursor()
        cursor.execute(query, (lat_min, lat_max, lng_min, lng_max))
        return cursor.fetchall()
