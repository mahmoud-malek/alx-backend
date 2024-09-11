#!/usr/bin/env python3
"""
A Basic flask application
for practicing Babel i18n
"""

from flask import Flask, request, render_template
from flask_babel import Babel, _, gettext
from typing import List


class Config(object):
    """
    Application configuration class
    and sets the following:
    - Babel default locale
    - Babel default timezone
    - Babel default locale
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)


def get_locale() -> str:
    """
    Gets locale from request object
    and returns the best matching language
    """
    if request.args.get('locale'):
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Wrap the application with Babel
babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
