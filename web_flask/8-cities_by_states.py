#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from os import getenv
from models.state import State
from models.city import City
app = Flask(__name__)


def show_state():
    states_l = storage.all("State").values()
    return render_template('7-states_list.html', states_l=states_l)


@app.route('/cities_by_states')
def cities_by_states_html():
    states_l = storage.all("State").values()
    return render_template('8-cities_by_states.html', states_l=states_l)


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
