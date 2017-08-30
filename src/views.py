import time
from random import randint
from datetime import datetime

from flask import render_template, jsonify, redirect, \
    url_for, flash, request
from flask_login import login_required, login_user,\
    logout_user, current_user

from src import app, db, login_manager
from src.forms import CarForm, LoginForm, SignInForm
from src.models import Car, Owner


@login_manager.user_loader
def load_user(owner_id):
    return Owner.query.get(int(owner_id))


@app.route('/')
@app.route('/index')
def index():
    """Index view"""
    return render_template('index.html', new_cars=Car.newest(5))


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = SignInForm()
    if form.validate_on_submit():
        owner = Owner(
            name=form.owner.data,
            password=form.password.data,
            email=form.email.data,
        )
        db.session.add(owner)
        db.session.commit()
        flash('Rejestracja zakończyła się pomyślnie!')
        return redirect(url_for('login'))
    return render_template('sign_up.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login view"""
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Owner.get_by_name(username)
        if user is not None and user.check_password(password):
            should_stay_logged = form.remember_me.data
            login_user(user, should_stay_logged)
            flash('Zalogowano {}.'.format(user.name))
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        flash('Niepoprawny użytkownik lub hasło.')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """Logout view"""
    logout_user()
    return redirect(url_for('index'))


@app.route('/car', methods=['GET', 'POST'])
@login_required
def add_car():
    """View for adding new car"""
    form = CarForm()
    if form.validate_on_submit():
        plate = form.plate.data
        description = form.description.data
        car = Car(owner=current_user, plate=plate, description=description)
        db.session.add(car)
        db.session.commit()
        flash('Zaposano pojazd: {}'.format(description))
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
def random_list(length: int):
    """Param example"""
    rand_list = [randint(1, length) for _ in range(1, length+1)]
    return str(rand_list)
