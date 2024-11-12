
import requests

from flask import Flask, request, jsonify
from flask_cors import CORS

import logging


app = Flask(__name__)
CORS(app)


@app.route('/user/<path:path>', methods=['GET', 'POST'])
def user_service(path):
    service_port =  5001
    service_url = f'http://user-service:{service_port}/{path}'
    response = requests.request(
        method=request.method,
        url=service_url,
        headers=request.headers,
        data=request.get_data(),
        allow_redirects=False
    )
    return jsonify(response.json()), response.status_code


@app.route('/order/<path:path>', methods=['GET', 'POST'])
def order_service(path):
    service_port =  5002
    service_url = f'http://order-service:{service_port}/{path}'
    response = requests.request(
        method=request.method,
        url=service_url,
        headers=request.headers,
        data=request.get_data(),
        allow_redirects=False
    )
    return jsonify(response.json()), response.status_code


@app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy_request(path):
    logging.info(f'proxy request: {path}')
    service_url = f'http://{path}'  # 简化的服务路由逻辑
    response = requests.request(
        method=request.method,
        url=service_url,
        headers=request.headers,
        data=request.get_data(),
        allow_redirects=False
    )
    return (response.content, response.status_code, response.headers.items())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
