
from flask import jsonify

from models.user_model import db
from models.user_model import User

from loguru import logger


def get_users():
    logger.info('Getting all users')
    users = User.query.all()
    result = [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]
    return jsonify(result), 200


def get_user(user_id):
    logger.info(f'Getting user with id: {user_id}')
    user = User.query.get_or_404(user_id)
    result = {'id': user.id, 'name': user.name, 'email': user.email}
    return jsonify(result), 200


def add_user(data):
    logger.info('Creating user with %s', data)
    if User.query.filter_by(email=data['email']).first():
        result = {'message': 'User already exists'}
        return jsonify(result), 400

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    result = {'message': 'User created', 'id': new_user.id}
    return jsonify(result), 201


def update_user(user_id, data):
    logger.info(f'Updating user with id: {user_id}')
    user = User.query.get_or_404(user_id)
    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    result = {'message': 'User updated', 'id': user.id}
    return jsonify(result), 200


def delete_user(user_id):
    logger.info(f'Deleting user with id: {user_id}')
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    result = {'message': 'User deleted'}
    return jsonify(result), 200
