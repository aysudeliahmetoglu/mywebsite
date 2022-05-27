from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #decorators
def home_page():
    return render_template("home.html")