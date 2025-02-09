#!/usr/bin/python3
"""Flask web application to display states and their cities"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    """Displays a list of states or cities of a given state"""
    states = storage.all(State)
    if id:
        state = states.get(f"State.{id}")
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
