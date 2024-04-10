#!/usr/bin/python3


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route to display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route to display HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """Route to display text with 'C' prefix"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route to display text with 'Python' prefix"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """
    Flask provides a built-in converter called int that can
    be used to ensure that the URL variable is an integer:
    thanks to the <int:num> syntax, which uses Flask's
    built-in int converter.
    """
    return f"{escape(n)} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
