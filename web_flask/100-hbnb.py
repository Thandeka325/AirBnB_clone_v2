#!/usr/bin/python3
"""Starts a Flask web application for AirBnB Clone"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays the HBNB home page with sorted States, Cities,
    Amenities, and Places."""
    states = sorted(
            storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(
            storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    places = sorted(
            storage.all(Place).values(), key=lambda place: place.name)

    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
