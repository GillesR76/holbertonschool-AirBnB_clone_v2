#!/usr/bin/python3
"""Flask web application to display the HBNB data"""

from flask import Flask, render_template, appcontext_tearing_down
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states/', strict_slashes=False)
def cities_by_state():
    """
    Route decorator to display cities by states with
    sorted states and their cities
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_cities = {state: sorted(
        state.cities, key=lambda city: city.name) for state in sorted_states}
    return render_template('8-cities_by_states.html',
                           states=sorted_states, cities=sorted_cities)


@app.teardown_appcontext
def remove_session(exception):
    """
    Closes the database session after each request.

    Args:
        exception: The exception raised during the request, if any.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
