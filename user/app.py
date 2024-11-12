
from flask import Flask
from routes import user_routes
from models import init_db
import config


app = Flask(__name__)
app.config.from_object('config')

init_db(app)

app.register_blueprint(user_routes)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
