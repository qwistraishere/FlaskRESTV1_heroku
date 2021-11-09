from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "store already exist"}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception as e:
            return {"message": f"Error Occured: {e}"}, 500

        return store.json(), 201

    def delete(self, name):
        if StoreModel.find_by_name(name):
            store = StoreModel.find_by_name(name)
            store.delete_from_db()
        
        return {"message": f"Store {name} Deleted"}

class StoreList(Resource):
    def get(self):
        return {"items": [item.json() for item in StoreModel.query.all()]}