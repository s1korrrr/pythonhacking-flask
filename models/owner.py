from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from database import Base
from .car import Car


class Owner(Base):
    __tablename__ = 'owner'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer)
    car_id = Column(Integer, ForeignKey('car.id'))
    car = relationship(Car)

    def __init__(self, name=None, age=None, car_id=None, car=None):
        self.name = name
        self.age = age
        self.car_id = car_id
        self.car = car

    def __repr__(self):
        return '<Owner {}>'.format(self.name)
