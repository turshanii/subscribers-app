import sqlite3
from db import db

class SubscriberModel(db.Model):

    TABLE_NAME = 'subscribers'

    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    nid = db.Column(db.String(80))


    def __init__(self, name, nid):
        self.name = name
        self.nid = nid

    def json(self):
        return {'name' : self.name , 'nid' : self.nid}


    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
