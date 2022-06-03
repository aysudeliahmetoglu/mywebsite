from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #decorators
@app.route("/home") 
def home_page():
    return render_template("home.html")

@app.route("/market") 
def market_page():
    items=[
    {'id':1 ,'name':'Phone','barcode':'123456786','price':500},
    {'id':2 ,'name':'Laptop','barcode':'987654321','price':1500},
    {'id':3 ,'name':'Keyboard','barcode':'7684090585837','price':150}


    ]
    return render_template("market.html",items=items)    