#!/usr/bin/python3
"""python script that starts a Flask web application"""
from flask import Flask

app = Flask("__name__")


@app.route("/")
def hello():
    """func to serve the above route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """func to serve the above route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """func to serve the above route"""
    new_text = text.replace('_', ' ')
    return "C % s" % new_text


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """func to serve the above routes"""
    new_text = text.replace('_', ' ')
    return "python % s" % new_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
