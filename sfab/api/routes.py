from flask import Blueprint
from sfab.models import Location
from flask import Flask,request,jsonify
from sfab import app,db

mod = Blueprint('api',__name__)

@mod.route('/home')
def home():
    return "In home"

# welcome home page
# this seems to be working when i deploy on gcp
@mod.route('/')
def hello():

    """Return a friendly HTTP greeting."""
#     return 'Flippingo !!'
    loc = Location.query.all()

    data = []

    print(loc)
    for l in loc:
        data.append({
        "latitude" : l.latitude,
        "longitude" : l.longitude,
        "angle"     : l.angle,
        "direction" : l.direction
        })
    # print(l.latitude)

    return jsonify({"data":data})

# saves the location data

@mod.route('/location_save',methods=['POST'])
def location_save():
    location = Location(
    latitude = request.json.get('latitude'),
    longitude = request.json.get('longitude'),
    angle = request.json.get('angle'),
    direction = request.json.get('direction')
    )

    db.session.add(location)
    db.session.commit()

    return jsonify({ "latitude":location.latitude , "longitude" : location.longitude , "angle":location.angle , "direction":location.direction})

# get details of a location by passing latitude and longitude values in json
@mod.route('/get_location',methods=['GET'])
def get_location():

    latitude = request.json.get('latitude')
    longitude = request.json.get('longitude')

    print(latitude)
    print(longitude)

    loc = Location.query.filter_by(latitude = latitude).first()



    return jsonify({"latitude":loc.latitude , "longitude" : loc.longitude , "angle" : loc.angle , "direction" : loc.direction})


# link to get all of the location data in the table
@mod.route('/get_all',methods=['GET'])
def get_all():

    loc = Location.query.all()

    data = []

    print(loc)
    for l in loc:
        data.append({
        "latitude" : l.latitude,
        "longitude" : l.longitude,
        "angle"     : l.angle,
        "direction" : l.direction
        })
    # print(l.latitude)

    return jsonify({"data":data})


# if __name__ == "__main__":
#     db.create_all()
#     app.run(host="0.0.0.0", port=8080)
#     app.run(host="127.0.0.1", port=5000,debug=True)
