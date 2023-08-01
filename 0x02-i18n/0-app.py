#!/usr/bin/env python3
"""A flask app"""

from flask import Flask, render_template
from flask.wrappers import Response

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """index function returning an html page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
