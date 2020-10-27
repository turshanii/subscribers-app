from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.subscriber import SubscriberModel
import sqlite3

class Subscribers(Resource):

    def get(self):
        return {'subscribers': [subscribers.json() for subscribers in SubscriberModel.query.all()]}

class Subscriber(Resource):
    TABLE_NAME = 'subscribers'

    parser = reqparse.RequestParser()
    parser.add_argument('nid',
            type=str,
            required=True,
            help="you must enter a national ID (nid)!"
        )


    def get(self, name):
        subscriber = SubscriberModel.find_by_name(name)
        if subscriber :
            return SubscriberModel.json(subscriber)
        return {"message" : "subscriber not found"} , 404


    def post(self, name):
        if SubscriberModel.find_by_name(name):
            return {'message': "An subscriber with name '{}' already exists.".format(name)} , 400

        data = Subscriber.parser.parse_args()
        subscriber = SubscriberModel(name,data['nid'])
        subscriber.save_to_db()
        return subscriber.json() , 201

    @jwt_required()
    def delete(self, name):
        subscriber = SubscriberModel.find_by_name(name)
        if subscriber:
            subscriber.delete_from_db()
            return {'message': 'subscriber deleted'}
        return {'message': 'subscriber not found'}

    def put(self, name):
        data = Subscriber.parser.parse_args()
        subscriber = SubscriberModel.find_by_name(name)
        if subscriber:
            subscriber.nid = data['nid']
        else:
            subscriber = SubscriberModel(name, **data)
        subscriber.save_to_db()
        return subscriber.json()
