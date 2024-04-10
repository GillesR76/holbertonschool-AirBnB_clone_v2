#!/usr/bin/python3
from flask import Flask
"""
creating a flask application: creates a new instance
of the Flask class which represents the web app.
__name__: python convention that tells Flask where to
look for resources like templates and static files
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """new route to display Hello HBNB"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
