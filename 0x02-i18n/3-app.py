#!/usr/bin/env python3
"""
Module that starts a flask app.
"""
from flask_babel import Babel
from flask import (
    Flask,
    render_template,
    request)


class Config:
    """ languages Configurations for the app. """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config())
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ return the best match """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route("/")
def hello():
    """ renders a simple page. """
    return render_template("3-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
