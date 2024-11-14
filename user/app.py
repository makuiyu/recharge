
import config

from flask import Flask

from models.user_model import init_db
from routes.user_route import user_bp

from loguru import logger


app = Flask(__name__)
app.config.from_object(config)
for key, value in app.config.items():
    logger.info(f'config {key}: {value}')

init_db(app)

app.register_blueprint(user_bp)


with app.app_context():
    # 获取路由列表
    routes = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            logger.info(rule)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
