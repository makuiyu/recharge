
from flask import jsonify

from models.order_model import db
from models.order_model import Order

from loguru import logger


def get_orders():
    logger.info('Getting all orders')
    orders = Order.query.all()
    result = [{'id': order.id, 'user_id': order.user_id, 'status': order.status} for order in orders]
    return jsonify(result), 200


def get_order(order_id):
    logger.info(f'Getting order with id: {order_id}')
    order = Order.query.get_or_404(order_id)
    result = {'id': order.id, 'user_id': order.user_id, 'status': order.status}
    return jsonify(result), 200


def add_order(data):
    logger.info('Creating order with %s', data)
    new_order = Order(user_id=data['user_id'], status='Pending')
    db.session.add(new_order)
    db.session.commit()
    result = {'message': 'Order created', 'id': new_order.id}
    return jsonify(result), 201


def update_order(order_id, data):
    logger.info(f'Updating order with id: {order_id}')
    order = Order.query.get_or_404(order_id)
    order.status = data.get('status', order.status)
    db.session.commit()
    result = {'message': 'Order updated', 'id': order.id}
    return jsonify(result), 200


def delete_order(order_id):
    logger.info(f'Deleting order with id: {order_id}')
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    result = {'message': 'Order deleted'}
    return jsonify(result), 200

