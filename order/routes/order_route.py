
from flask import Blueprint
from flask import request
from flask import jsonify

from services import order_service

from loguru import logger


order_bp = Blueprint('order_bp', __name__)


@order_bp.before_request
def bp_before_request():
    logger.debug(f'{request.path} {request.method} {request.endpoint}')


@order_bp.route('/orders', methods=['GET'])
def get_orders():
    return order_service.get_orders()


@order_bp.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    return order_service.get_order(order_id)


@order_bp.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    return order_service.add_order(data)


@order_bp.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    return order_service.update_order(order_id, data)


@order_bp.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    return order_service.delete_order(order_id)
