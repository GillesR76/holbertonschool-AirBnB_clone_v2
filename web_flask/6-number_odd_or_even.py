from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


"""
Flask provides a built-in converter called int that can
be used to ensure that the URL variable is an integer:
thanks to the <int:num> syntax, which uses Flask's
built-in int converter.
"""


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_htmlpage(n):
    """render_template method used to generate a html page
    by providing the name of the template and the name
    of the variable you want to pass to the template
    engine as keyword argument i.e n=n"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    parity = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
