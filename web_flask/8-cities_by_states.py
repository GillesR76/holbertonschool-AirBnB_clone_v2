#!/usr/bin/python3


from flask import Flask, render_template, appcontext_tearing_down
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list/', strict_slashes=False)
def state_list():
    """
    Renders a template that displays a list of states sorted by name.

    Returns:
        The rendered template with the sorted list of states.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


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
