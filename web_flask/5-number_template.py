#!/usr/bin/python3
"""
A Python script that starts a Flask web application.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    """
    Serves a basic 'Hello HBNB!' message.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Serves an 'HBNB' message.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    Serves the provided text after replacing underscores with spaces.
    Args:
        text (str): The text to be displayed.
    """
    new_text = text.replace('_', ' ')
    return "C %s" % new_text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    Serves the provided text or a
    default message with spaces instead of underscores.
    Args:
        text (str): The text to be displayed (default is 'is cool').
    """
    new_text = text.replace('_', ' ')
    return "Python %s" % new_text


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Serves a template with the provided number.
    Args:
        n (int): The number to be displayed in the template.
    """
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
