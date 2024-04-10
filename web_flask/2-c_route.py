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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
