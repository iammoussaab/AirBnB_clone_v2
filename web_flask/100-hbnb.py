#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb: HBnB home page.
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def state_cities_list():
    """ Get states sorted by names and render on template """
    states_data = list(storage.all(State).values())
    amenity_data = list(storage.all(Amenity).values())
    place_data = list(storage.all(Place).values())
    return render_template('100-hbnb.html',
                           states=states_data,
                           amenities=amenity_data,
                           places=place_data)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
