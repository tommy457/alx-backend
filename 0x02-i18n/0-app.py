#!/usr/bin/env python3
"""
Module that starts a flask app.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello():
    """ renders a simple page. """
    return render_template("0-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
