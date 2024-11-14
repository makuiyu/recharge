
from flask import Blueprint
from flask import request
from flask import jsonify

from services import user_service

from loguru import logger


user_bp = Blueprint('user_bp', __name__)


@user_bp.before_request
def bp_before_request():
    logger.debug(f'{request.path} {request.method} {request.endpoint}')


@user_bp.route('/users', methods=['GET'])
def get_users():
    return user_service.get_users()


@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return user_service.get_user(user_id)


@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    return user_service.add_user(data)


@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return user_service.update_user(user_id, data)


@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return user_service.delete_user(user_id)
