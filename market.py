from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1000), nullable=False, unique=True)




@app.route("/")  # decorators
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():

    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '123456786', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '987654321', 'price': 1500},
        {'id': 3, 'name': 'Keyboard', 'barcode': '7684090585837', 'price': 150}


    ]
    return render_template("market.html", items=items)
