from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, prompt_bool

from src import app, db
from src.models import Task, User

manager = Manager(app)


def fill_db(conn: SQLAlchemy):
    """Fill database with initial fake data"""
    conn.session.add(User(name='Patryk', password='admin', email='pat@mail.pl'))
    conn.session.add(User(name='Nikodem', password='admin', email='nik@mail.pl'))
    conn.session.add(User(name='Andrzej', password='admin', email='and@mail.pl'))
    conn.session.add(Task(description='Opel', user_id=1))
    conn.session.add(Task(description='BMW', user_id=2))
    conn.session.add(Task(description='Lexus', user_id=3))
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
