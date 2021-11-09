from flask_restful import Resource, reqparse
from models.item import ItemModel
import traceback

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
                        type=float, required=True, help="This filed cannot be empty")

    parser.add_argument("store_id",
                        type=int, required=True, help="Every item needs store id.")

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item Not found"}, 404

    def post(self, name):
        # set new item
        if ItemModel.find_by_name(name):
            # item already exist
            return {"message": f"An item with name {name} already exist"}, 400

        data = Item.parser.parse_args()
        
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            err = traceback.format_exc()
            return {"Message": f"An error occurred inserting the item {err}"}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            # Item exist and we can delete it
            item.delete_from_db()
            return {"message": f"Item {name} deleted"}, 200
        return {"message": f"Item {name} doesnt exist in DB"}, 400

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])

        else:
            item.price = data['price']
        
        item.save_to_db()
        return item.json()
class ItemList(Resource):

    @staticmethod
    def get_all_items():
        items = ItemModel.query.all()
        ret = []
        for item in items:
            data = {"name": item.name, 'price': item.price}
            ret.append(data)
        return ret
        
    def get(self):
        # Get All items
        return {"items": self.get_all_items()}