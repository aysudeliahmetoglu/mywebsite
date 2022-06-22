from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'dfd27c6c63080ec139990f7b'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes