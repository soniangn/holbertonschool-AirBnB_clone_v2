#!/usr/bin/python3
""" doc """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ display a HTML page """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template(states=states, amenities=amenities)


@app.teardown_appcontext
def close(exception):
    storage.close()
