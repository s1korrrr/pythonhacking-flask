import os, time

from flask import Flask, render_template, jsonify, request, url_for
from database import db_session, init_engine, init_db

from models.car import Car

app = Flask(__name__)
app.config.from_object('default_settings')
if 'LOCAL_SETTINGS' in os.environ:
    app.config.from_envvar('LOCAL_SETTINGS')


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index page"""
    if request.method == 'POST':
        return render_template('index.html', name=request.form['name'])
    return render_template('index.html')


@app.route('/json_example')
def json_example():
    """Example json endpoint"""
    return jsonify({'hs': 3, 'timestamp': time.time()})


@app.route('/form', methods=['GET', 'POST'])
def name_form():
    """Simple form example"""
    if request.method == 'POST':
        return render_template('site.html', name=request.form['name'])
    return render_template('form.html', action_url=url_for('name_form'))


@app.route('/cars')
def cars():
    """Table with all cars from db"""
    all_cars = Car.query.all()
    return render_template('cars.html', auta=all_cars)


@app.route('/car/add', methods=['POST'])
def add_car():
    """Add car"""
    data = request.json
    c = Car(id=data['id'], make=data['make'],
            model=data['model'], plates=data['plates'],
            dmv_number=data['dmv'], year=data['year'])
    db_session.add(c)
    db_session.commit()
    return 'Success\n'


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Teardown method"""
    db_session.remove()


if __name__ == '__main__':
    init_engine(app.config['DATABASE_URI'])
    init_db()
    app.run(
        debug=True,
        host=app.config.get('SERVER_HOST'),
        port=app.config.get('SERVER_PORT'),
    )
