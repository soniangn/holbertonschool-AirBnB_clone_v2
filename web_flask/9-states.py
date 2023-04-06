#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states_list)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ if found, display the list of city linked
        to the state sorted by name, else H1 not found
    """
    id_exist = False
    state_id = None
    states = storage.all(State)
    cities = storage.all(cities)
    for state in states.values():
        if state.id == id:
            state_id = state
            id_exist = True
    return render_template("9-states.html", cities=cities, state_id=state_id, id_exist=id_exist)


@app.teardown_appcontext
def close_session(exception):
    """ remove the current SQLalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
