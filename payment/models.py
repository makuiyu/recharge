
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey


db = SQLAlchemy()


class Payment(db.Model):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    amount = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
