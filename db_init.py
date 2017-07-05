from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# Base declaration, all of the base tables are classes that input with this object
Base = declarative_base()


# Tables declaration - skeletons for base
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

class Owner(Base):
    __tablename__ = 'owner'
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer)
    car_id = Column(Integer, ForeignKey('car.id'))
    car = relationship(Car)

# Starting point of SQLAlchemy app. Abstraction of the database and its API.
# It works with the connection pool and the Dialect component to deliver SQL
# statements from the SQLAlcehmy to the database.
engine = create_engine('sqlite:///car_club.db')


# Allows to work with the object-relational mapper, primary interface for persistance
# operations. Establishes all connections with database and represents a container for all the objects.
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# Create all tables, equivalent to Create Table in SQL
Base.metadata.create_all(engine)

cars = session.query(Car).all()
car = session.query(Car).first()
for auto in cars:
    print auto.dmv_number
print car.plates
