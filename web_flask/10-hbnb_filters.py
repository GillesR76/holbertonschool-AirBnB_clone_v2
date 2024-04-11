#!/usr/bin/python3
"""Flask web application to display the HBNB data"""

from flask import Flask, render_template, appcontext_tearing_down
from markupsafe import escape
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    """
    Closes the database session after each request.

    Args:
        exception: The exception raised during the request, if any.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda x: x.name)
    for state in sorted_states:
        cities = sorted(state.cities, key=lambda x: x.name)

    return render_template('10-hbnb_filters.html', states=sorted_states,
                           amenities=sorted_amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
