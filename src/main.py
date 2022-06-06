"""
Apico Application server
"""
# imports
from flask import Flask, render_template, jsonify

# create app object
app = Flask("Apico_Web")


# default route (main page)
@app.route('/')
def index():
    return render_template("index.html");


# description page
@app.route('/description')
def description():
    return render_template("description.html")


# data download (as json)
@app.route('/get_data')
def get_data():
    l = [{"a": 1, "b":2}, {"a": 1, "b":2}]
    return jsonify(l)


# launch app ( not in production !)
app.run(host="localhost", port=8000, debug=True)
