#!/usr/bin/python3
"""Starts a Flask web application and displays a list of all State objects"""

from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all State objects sorted by name"""
    all_states = storage.all("State").values()
    states = sorted(list(all_states), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
