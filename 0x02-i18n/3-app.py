#!/usr/bin/env python3
""" Babel """

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """ Configures the language to loal timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Returns the language requested that
    matches the configured languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Parameterizes the template """
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('3-index.html', home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
