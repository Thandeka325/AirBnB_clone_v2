#!/usr/bin/python3
"""A simple Flask web application with multiple routes."""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns 'Hello HBNB!' when accessing the root URL."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB' when accessing the /hbnb URL."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C ' followed by the text variable,
    replacing '_' with spaces."""
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Returns 'Python ' followed by the text variable,
    replacing '_' with spaces."""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Returns '<n> is a number' only if n is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
