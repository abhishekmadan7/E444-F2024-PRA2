from flask import Flask,render_template
from flask_moment import Moment
from datetime import datetime
from flask_bootstrap import Bootstrap



app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'hard to guess string'


@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404



