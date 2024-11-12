
from flask import Blueprint, jsonify, request
from models import Item, db


inventory_routes = Blueprint('inventory_routes', __name__)


@inventory_routes.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "quantity": item.quantity} for item in items])


@inventory_routes.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    new_item = Item(name=data['name'], quantity=data['quantity'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item added", "id": new_item.id}), 201
