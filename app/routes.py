import datetime
from app import app
from flask import render_template

from app.models import Test


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rusty'}
    return render_template('index.html', title='Home', user=user)


@app.route('/suite/<name>')
def suite(name):
    suite = {}
    return render_template('suite.html', title='Home', suite=suite)


@app.route('/test/<name>')
def test(name):
    t = Test.query.get(1)
    test = t
    return render_template('test.html', title='Test', test=test)



