import time
from random import randint
from datetime import datetime

from flask import render_template, jsonify, redirect, url_for, flash

from src import app, db
from src.forms import CarForm
from src.models import Car, Owner


# Fake login
def logged_in_user():
    return Owner.query.filter_by(name='Patryk').first()


@app.route('/')
@app.route('/index')
def index():
    """Main view"""
    return render_template('index.html', new_cars=Car.newest(5))


@app.route('/car', methods=['GET', 'POST'])
def add_car():
    form = CarForm()
    if form.validate_on_submit():
        plate = form.plate.data
        description = form.description.data
        car = Car(owner=logged_in_user(), plate=plate, description=description)
        db.session.add(car)
        db.session.commit()
        # flash('Stored cars: {}'.format(description))
        return redirect(url_for('index'))
    return render_template('add_car.html', form=form)


@app.route('/some_json')
def some_json():
    """Json example"""
    json_ = {
        'date': datetime.utcnow(),
        'epoch_time': time.time(),
    }
    return jsonify(json_)
 

@app.route('/random-list/<int:length>')
def random_list(length):
    """Param example"""
    rand_list = [randint(1, length) for _ in range(1, length+1)]
    return str(rand_list)
