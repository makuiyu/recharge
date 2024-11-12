
from flask import Flask
from routes import order_routes
from models import init_db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:makuiyu@db/recharge_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


init_db(app)


app.register_blueprint(order_routes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
