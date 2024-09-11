#!/usr/bin/env python3

""" a module for running the flask app """

from flask import Flask, render_template
from babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)


class Config:
    """ a configuration class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def hello_world() -> str:
    """ root route """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
