
import config

from flask import Flask
from flask_cors import CORS

from routes.gateway_route import gateway_bp

from loguru import logger


app = Flask(__name__)
app.config.from_object(config)
for key, value in app.config.items():
    logger.info(f'config {key}: {value}')

CORS(app)

app.register_blueprint(gateway_bp)


with app.app_context():
    # 获取路由列表
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            logger.info(rule)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
