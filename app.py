import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from models.user import authenticate , identity
from resources.user import Userreg

from models.subscriber import SubscriberModel
from resources.subscriber import Subscribers , Subscriber

app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = True

app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = 'mt'
jwt = JWT(app, authenticate, identity)    #/auth


api.add_resource(Subscriber,'/subscriber/<string:name>')
api.add_resource(Subscribers,'/subscribers')
api.add_resource(Userreg,'/reg')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
