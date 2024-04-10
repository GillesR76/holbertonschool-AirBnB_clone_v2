#!/usr/bin/python3
"""Flask web application to display the HBNB data"""

from flask import Flask, render_template, appcontext_tearing_down
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_cities(id=None):
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    if id is None:
        return render_template('9-states.html', states=sorted_states)
    else:
        for state in sorted_states:
            if id == state.id:
                sorted_cities = {state: sorted(
                    state.cities, key=lambda city: city.name)}
                return render_template('9-states.html', states=sorted_states, cities=sorted_cities)
        return render_template('9-states.html', not_found=True)


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
