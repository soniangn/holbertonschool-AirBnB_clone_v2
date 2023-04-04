#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """ display a HTML page with list of cities
    sorted by states
    """
    states_list = []
    states = storage.all(State)
    for _, v in states.items():
        states_list.append(v)
    return render_template("8-cities_by_states.html", states_list=states_list)


@app.teardown_appcontext
def close_session(exception):
    """ remove the current SQLalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
