
from flask import Blueprint, jsonify, request
from models import Payment, db


payment_routes = Blueprint('payment_routes', __name__)


@payment_routes.route('/payments', methods=['POST'])
def process_payment():
    data = request.get_json()
    new_payment = Payment(order_id=data['order_id'], amount=data['amount'], status='Processing')
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({'message': 'Payment initiated', 'id': new_payment.id}), 201
