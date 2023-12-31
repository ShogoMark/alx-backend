#!/usr/bin/env python3
"""A flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app: Flask = Flask(__name__)


class Config:
    """Class config to instantiate default locale/timezone"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """function to set the match languages with locale"""
    sup_lang = app.config['LANGUAGES']
    return request.accept_languages.best_match(sup_lang)


@app.route('/')
def index() -> str:
    """index function returning an html page"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
