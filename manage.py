from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, prompt_bool

from src import app, db
from src.models import Car, Owner

manager = Manager(app)


def fill_db(conn: SQLAlchemy):
    """Fill database with initial fake data"""
    conn.session.add(Owner(name='Patryk', email='pat@mail.pl'))
    conn.session.add(Owner(name='Nikodem', email='nik@mail.pl'))
    conn.session.add(Owner(name='Andrzej', email='and@mail.pl'))
    conn.session.add(Car(plate='GKW 883A6', description='Opel', owner_id=1))
    conn.session.add(Car(plate='GD 523DD', description='BMW', owner_id=2))
    conn.session.add(Car(plate='GO NER55', description='Lexus', owner_id=3))
    conn.session.commit()


@manager.command
def init_db():
    """Initialize database"""
    db.create_all()
    fill_db(conn=db)
    print('Database has been initialized')


@manager.command
def drop_db():
    """Drop database"""
    msg = 'Are you sure you want to delete your database?'
    if prompt_bool(msg):
        db.drop_all()
        print('Database has been dropped.')


if __name__ == '__main__':
    manager.run()
