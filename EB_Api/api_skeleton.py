from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# DB setup

app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}

# Initializing DB
db = MongoEngine()
db.init_app(app)


class User(db.Document):
    """Creating Database Model"""
    user_id = db.StringField(required=True, unique=True)
    usr_key = db.StringField(required=True, unique=True)
    acc_info = db.StringField(required=True)
    # all other fields can be populated based on preference
    # of either using Json Objects or MetaData Class


api = Api(app)

# Arguments Required to PUT a User
user_put_args = reqparse.RequestParser()
user_put_args.add_argument(
    "usr_key", type=str, help="Required Key for the User", required=True)
user_put_args.add_argument("subscriptions", action='append',
                           help="Required Name of Subscriptions", required=True)
user_put_args.add_argument("account_info", type=str,
                           help="Required Account Information", required=True)

users = {}


def abort_if_user_id_doesnt_exist(user_id):
    if user_id not in users:
        abort(404, message="User not Found . . . . . ")


def abort_if_user_id_exist(user_id):
    if user_id in users:
        abort(404, message="User Already Exists . . . . . ")


class UserSubscription(Resource):
    """A UserSubscription object to interact with subscription Data
    for a user
    - User ID
    - Dict of Subscriptions : Status
    Representing Status of each subscription
    """

    def get(self, user_id):
        abort_if_user_id_doesnt_exist(user_id)
        return users[user_id], 200

    # Database Endpoints not used for simplicity
    # @marshal_with(my_fields)
    # def get(self, user_id):
    #     """Get Using Database"""
    #     users = User.objects().get(user_id).to_json()
    #     return users, 200

    def put(self, user_id):
        """Create user with
        - usr_id: str
        - subscriptions: list
        - account_info: str"""
        abort_if_user_id_exist(user_id)
        args = user_put_args.parse_args()

        # Create Dict for subscriptions with Unpaid value
        subs_dict = {}
        for i in args['subscriptions']:
            subs_dict[i] = "UnPaid"

        args['subscriptions'] = subs_dict
        users[user_id] = args
        return users[user_id], 201

    def patch(self, user_id):
        pass

    def delete(self, user_id):
        abort_if_user_id_doesnt_exist(user_id)
        del users[user_id]
        return '', 204


api.add_resource(UserSubscription, '/api/<user_id>')


if __name__ == "__main__":
    # We will serve our application using waitress
    # Instead of app.run when deploying
    app.run(debug=False)
