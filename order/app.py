
import config

from flask import Flask

from models.order_model import init_db
from routes.order_route import order_bp

from loguru import logger


app = Flask(__name__)
app.config.from_object(config)
for key, value in app.config.items():
    logger.info(f'config {key}: {value}')

init_db(app)

app.register_blueprint(order_bp)


with app.app_context():
    # 获取路由列表
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            logger.info(rule)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
