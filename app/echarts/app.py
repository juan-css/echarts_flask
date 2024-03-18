from flask import Flask, render_template
from .tasks import generate_data

app = Flask(__name__)


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():

    data = generate_data()

    return render_template("index.html",
                           data=data)
