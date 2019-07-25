from sfab import db

class Location(db.Model):
    __tablename__ = 'location'
    id = db.Column(db.Integer,primary_key=True)
    latitude = db.Column(db.Integer)
    longitude = db.Column(db.Integer)
    angle = db.Column(db.Integer)
    direction = db.Column(db.String(100))
