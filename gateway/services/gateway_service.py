
import requests

from flask import request
from flask import jsonify

from loguru import logger


def proxy_request(service_url):
    logger.info(f'proxy request: {service_url}')
    try:
        response = requests.request(
            method=request.method,
            url=service_url,
            headers=request.headers,
            data=request.get_data(),
            allow_redirects=False
        )
        return jsonify(response.json()), response.status_code
    except ValueError:
        return {'message': 'Invalid response from upstream service'}, 502