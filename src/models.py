from datetime import datetime

from sqlalchemy import desc
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from src import db


class Car(db.Model):
    """Car database table"""
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    @staticmethod
    def newest(num: int) -> list:
        """Return <num> of latest cars"""
        return Car.query.order_by(desc(Car.date)).limit(num)

    def __repr__(self) -> str:
        return "<Car '{}': '{}'>".format(self.description, self.plate)


class Owner(db.Model, UserMixin):
    """Owner database table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    cars = db.relationship('Car', backref='owner', lazy='dynamic')
    password_hash = db.Column(db.String)

    @property
    def password(self):
        """Raise when attempt to read password"""
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password: str):
        """Generate hash using password as seed"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Validate if password is correct"""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_name(name: str) -> object:
        """Return owner instance"""
        return Owner.query.filter_by(name=name).first()

    def __repr__(self) -> str:
        return '<Owner %r>' % self.username
