#!/usr/bin/env python3
"""
Module that starts a flask app.
"""
from flask_babel import Babel
from flask import (
    Flask,
    render_template,
    request,
    g)
from typing import Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    if g.user:
        lang = g.user.get("locale")
        if lang and lang in app.config["LANGUAGES"]:
            return lang
    lang = request.headers.get('locale', None)
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Dict[str, str] | None:
    """ return a user if id is found """
    user = request.args.get("login_as")
    try:
        return users.get(int(user))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request() -> None:
    """ Find a user if any, and set it as a global on flask.g.user. """
    g.user = get_user()


@app.route("/")
def hello():
    """ renders a simple page. """
    return render_template("5-index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
