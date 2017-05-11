import time
from flask import Flask, render_template, jsonify, request


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

if __name__ == "__main__":
    app.run()
