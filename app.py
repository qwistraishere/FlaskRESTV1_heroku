from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import authenticate, identity
from resources.store import Store, StoreList
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.secret_key = "kerw902"
# Flask JWT change default url of authentication endpoint
app.config['JWT_AUTH_URL_RULE'] = '/login'
api = Api(app)
jwt = JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

# add api endpoints
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(StoreList, "/stores")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)
