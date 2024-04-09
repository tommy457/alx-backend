#!/usr/bin/env python3
"""
Module that starts a flask app.
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """ languages Configurations for the app. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@app.route("/")
def hello():
    """ renders a simple page. """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
