#!/usr/bin/python3
from flask import Flask
"""
creating a flask application: creates a new instance
of the Flask class which represents the web app.
__name__: python convention that tells Flask where to
look for resources like templates and static files
"""

app = Flask(__name__)

"""
* defines a route for the root URL '/'. @app.route is
a decorator used to associate the index function with
the root URL
* The strict_slashes=False option means that URLs with or
without a trailing slash will be matched.
* The index function returns a string which will be
displayed in the browser when the root URL is accessed.
"""


@app.route('/', strict_slashes=False)
def index():
    """new route to display Hello HBNB"""
    return 'Hello HBNB!'


"""
* checks if the script is being run directly (not imported as a module).
If it is the main script, it calls the app.run method to start the Flask
development server.
* The app.run() function is used to start the Flask development server
and run the Flask application. It is typically called at the end of the
script, after defining all the routes and configurations.
* The host and port optional arguments allow to specify the host and
port on which the Flask application should listen for incoming requests.
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
