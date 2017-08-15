from flask_script import Manager, prompt_bool

from src import app, db
from src.models import Car, Owner

manager = Manager(app)


@manager.command
def init_db():
    db.create_all()
    db.session.add(Owner(name='Patryk', email='pat@wp.pl'))
    db.session.add(Owner(name='Nikodem', email='nik@wp.pl'))
    db.session.add(Car(plate='GKW 883A6', description='Opel Astra', owner_id=1))
    db.session.commit()
    print('Database has been initialized')


@manager.command
def drop_db():
    msg = 'Are you sure you want to delete your database?'
    if prompt_bool(msg):
        db.drop_all()
        print('Database has been dropped.')


if __name__ == '__main__':
    manager.run()
