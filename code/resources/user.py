import sqlite3
from flask_restful import Resource , reqparse
from models.user import UserModel


class Userregister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="you must enter a username (username)!"
            )
    parser.add_argument('password',
            type=str,
            required=True,
            help="you must enter a password!"
            )

    def post(self):
        data = Userregister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
