#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State



app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ display a HTML page with list of states """
    states = storage.all(State)
    states_list = sorted(states.values(), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """ remove the current SQLalchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
