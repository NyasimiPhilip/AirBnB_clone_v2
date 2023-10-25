#!/usr/bin/python3
"""A Python script that starts a Flask web application."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """Route that serves a simple greeting."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Route that serves an 'HBNB' message."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Route that serves the provided text
    after replacing underscores with spaces."""
    new_text = text.replace('_', ' ')
    return "C %s" % new_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
