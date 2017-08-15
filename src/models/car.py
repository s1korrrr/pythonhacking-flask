from sqlalchemy import Column, String, Integer

from src.database import Base


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    make = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    plates = Column(String(250), unique=True)
    dmv_number = Column(Integer, unique=True)
    year = Column(Integer)

    def __init__(self, id, make, model, plates, dmv_number, year):
        self.id = id
        self.make = make
        self.model = model
        self.plates = plates
        self.dmv_number = dmv_number
        self.year = year

    def __repr__(self):
        return '<Car {}>'.format(self.model)
