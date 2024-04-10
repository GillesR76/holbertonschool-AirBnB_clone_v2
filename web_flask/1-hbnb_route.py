"""Flask web application that defines two routes"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """new route to display Hello HBNB"""
    return 'Hello HBNB'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """new route to display HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
