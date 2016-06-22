import re, json, hashlib, datetime
from flask import jsonify
from DummyApp import DummyApp, db

class Users(db.Model, object):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(256))
    mail = db.Column(db.String(256))
    password = db.Column(db.String(512))
    created = db.Column(db.DateTime)
    active = db.Column(db.Boolean(), default=0)

    def add_user(self, User):
        """
        Adds the user object to the db
        """
        db.session.add(User)
        db.session.commit()

    def __init__(self, first_name, last_name, mail, password):
        """
        Create the new user object

        """
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.password = hashlib.sha256("%s%s" % ("saltandpepper", password)).hexdigest()
        self.created = datetime.datetime.utcnow()
