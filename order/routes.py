
from flask import Blueprint, jsonify, request
from models import Order, db


order_routes = Blueprint('order_routes', __name__)


@order_routes.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': order.id, 'user_id': order.user_id, 'status': order.status} for order in orders])


@order_routes.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return jsonify({'id': order.id, 'user_id': order.user_id, 'status': order.status})


@order_routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(user_id=data['user_id'], status='Pending')
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order created', 'id': new_order.id}), 201


@order_routes.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.get_json()
    order.status = data.get('status', order.status)
    db.session.commit()
    return jsonify({'message': 'Order updated', 'id': order.id})
