from flask import Flask, render_template, url_for

app = Flask("Apico Web")


@app.route('/')
def index():
    return "hello"


app.run(host="localhost", port=8000, debug=True)