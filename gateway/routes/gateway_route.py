
import config

from flask import Blueprint
from flask import request
from flask import jsonify

from services import gateway_service

from loguru import logger


gateway_bp = Blueprint('gateway_bp', __name__)


@gateway_bp.before_request
def bp_before_request():
    logger.debug(f'{request.path} {request.method} {request.endpoint}')


@gateway_bp.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_request(path):
    logger.info(f'proxy request: {path}')
    service_url = f'http://{path}'  # 简化的服务路由逻辑
    return gateway_service.proxy_request(service_url)


@gateway_bp.route('/user/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_request(path):
    service_host = config.USER_SERVICE_HOST
    service_port = config.USER_SERVICE_PORT
    service_url = f'http://{service_host}:{service_port}/{path}'
    return gateway_service.proxy_request(service_url)


@gateway_bp.route('/order/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def order_request(path):
    service_host = config.ORDER_SERVICE_HOST
    service_port = config.ORDER_SERVICE_PORT
    service_url = f'http://{service_host}:{service_port}/{path}'
    return gateway_service.proxy_request(service_url)


@gateway_bp.route('/inventory/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def inventory_request(path):
    service_host = config.INVENTORY_SERVICE_HOST
    service_port = config.INVENTORY_SERVICE_PORT
    service_url = f'http://{service_host}:{service_port}/{path}'
    return gateway_service.proxy_request(service_url)


@gateway_bp.route('/payment/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def payment_request(path):
    service_host = config.PAYMENT_SERVICE_HOST
    service_port = config.PAYMENT_SERVICE_PORT
    service_url = f'http://{service_host}:{service_port}/{path}'
    return gateway_service.proxy_request(service_url)
