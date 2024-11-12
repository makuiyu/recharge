
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()