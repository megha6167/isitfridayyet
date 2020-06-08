import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now().weekday()
    friday = now==4
    return render_template("index.html",friday=friday)

#@app.route("/<string:name>")
#def hello(name):
#    name=name.capitalize
#    headline="HELLO {}".format(name)
#    return render_template("index.html",headline=headline)
