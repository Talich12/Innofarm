from app import db, ma
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_sqlalchemy import fields, auto_field
from hashlib import md5
import base64
from datetime import datetime, timedelta
import os



class RevokedTokenModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))
    
    def add(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
    
    def __repr__(self):
        return '<Token {}>'.format(self.body)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    ser_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    date = db.Column(db.String(64))
    email = db.Column(db.String(64))
    avatar = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    status = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 
    

class Garden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship("User", backref="Gardens")

    def __repr__(self):
        return '<GreeHouse {}>'.format(self.username) 
    
class Supplie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    measure = db.Column(db.String(64))

class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    garden_id =  db.Column(db.Integer, db.ForeignKey('garden.id'))
    supplie_id = db.Column(db.Integer, db.ForeignKey('supplie.id'))
    count = db.Column(db.Integer)

    garden = db.relationship("Garden", backref="Metric")
    supplie = db.relationship("Supplie", backref="Metric")
    

class Workers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    worker_id =  db.Column(db.Integer, db.ForeignKey('user.id'))
    garden_id =  db.Column(db.Integer, db.ForeignKey('garden.id'))

    worker = db.relationship("User", backref="Worker")
    garden = db.relationship("Garden", backref="Worker")

    def __repr__(self):
        return '<GreeHouse {}>'.format(self.username) 


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True

    id = ma.auto_field()
    username = ma.auto_field()
    status = ma.auto_field()

class GardenSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Garden
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()

    author = fields.Nested(UserSchema)

class SupplieSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Supplie
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    measure = ma.auto_field()

class MetricSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Metric
        load_instance = True

    id = ma.auto_field()
    supplie = fields.Nested(SupplieSchema)
    count = ma.auto_field()