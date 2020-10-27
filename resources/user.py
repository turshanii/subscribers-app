from flask_restful import Resource, reqparse
from models.user import User
import sqlite3

class Userreg(Resource):

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

        data = Userreg.parser.parse_args()
        if User.find_by_username(data['username']):
            return {"message": "A user with the same username already exists"}, 400

        user = User(**data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201
