from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def render_dashboard():
    return render_template("dashboard.html")