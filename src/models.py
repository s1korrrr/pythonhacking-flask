from datetime import datetime

from sqlalchemy import desc

from src import db


class Car(db.Model):
    """Car database table"""
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(300))
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    @staticmethod
    def newest(num):
        return Car.query.order_by(desc(Car.date)).limit(num)

    def __repr__(self):
        return "<Car '{}': '{}'>".format(self.description, self.plate)


class Owner(db.Model):
    """Owner database table"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    cars = db.relationship('Car', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<Owner %r>' % self.username
