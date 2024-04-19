#!/usr/bin/python3
"""
This is module 7-states_list.py
"""
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list")
def states_list():
    states_l = storage.all("State")
    return (render_template("7-states_list.html", states_l=states_l))


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
