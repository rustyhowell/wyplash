from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rusty'}
    return render_template('index.html', title='Home', user=user)

@app.route('/suite/<name>')
def suite(name):
    return 'the suite: %s' % name
