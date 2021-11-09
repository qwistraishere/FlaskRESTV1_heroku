from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="This Field Can't be empty")
    parser.add_argument("password", type=str, required=True,
                        help="This Field Can't be empty")

    def post(self):

        data = UserRegister.parser.parse_args()
        # Check if user already Exist
        user = UserModel.find_by_username(data["username"])
        if user:
            # User exist
            return {"message": f"User <{user.username}> Already Exist"}, 400
        new_user = UserModel(**data)
        new_user.save_to_db()

        return {"message": "User Created succesfully"}, 201
