#!/usr/bin/env python3
"""
Create a get_locale function with the
babel.localeselector decorator
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Configures the locale language """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Matches the clients language with the
    selected language in the locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ Renders the html document on request """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
