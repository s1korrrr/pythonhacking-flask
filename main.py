import time

from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/index')
def index():
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