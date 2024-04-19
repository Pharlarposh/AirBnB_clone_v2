#!/usr/bin/python3
from flask import Flask, render_template
from models.state import State
from models.city import City
from models import storage
from os import getenv
app = Flask(__name__)


@app.route("/states")
def states():
    states_l = storage.all("State")
    return (render_template("9-states.html", states_l=states_l))


@app.route("/states/<id>")
def states_id(id):
    states = storage.all("State")

    for id_state in states:
        if id_state == id:
            get_state = states[id_state]
            get_state = str(get_state)
    return (render_template("9-states.html", state=get_state))


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
