import time
from flask import Flask, render_template, jsonify, request
from db_init import cars
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return render_template('index.html', name=request.form['name'])
    else:
        return render_template('index.html')


@app.route('/some_json')
def some_json():
    dict_ = {
        'hs': 3,
        'timestamp': time.time(),
    }
    return jsonify(dict_)
 

@app.route('/hs/<int:number>')
def hackerspace(number):
    l = [x**3 for x in range(1, number+1)]
    return str(l)


@app.route('/form', methods=['GET', 'POST'])
def formularz():
    if request.method == 'POST':
        return render_template('site.html', name=request.form['name'])
    if request.method == 'GET':
        return render_template('form.html')


@app.route('/szablon')
def szablony():
    lista_zakupow = ['mleko', 'jajka']

    return render_template('szablon.html', haha={'costam': 'hahaha, jednak nie'}, zakupy=lista_zakupow)


@app.route('/car_club')
def car_club():
    return render_template('car_club.html', auta=cars)

@app.route('/car_form')
def car_form():
    if request.method == 'POST':
        return render_template('car_club.html', name=request.form['name'])
    if request.method == 'GET':
        return render_template('form.html')


if __name__ == "__main__":
    app.run()

