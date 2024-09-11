#!/usr/bin/env python3
"""
A Basic flask application
for practicing Babel i18n
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_locale() -> str:
    """
    Gets locale from request object
    and returns the best matching language
    """
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Wrap the application with Babel
babel = Babel(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    username = 'Anonymous'
    if request.args.get('login_as'):
        g.user = users.get(int(request.args.get('login_as')))
        username = g.user.get('name')
    else:
        g.user = None

    return render_template(
        '5-index.html',
        g=g, username=username
    )


if __name__ == '__main__':
    app.run()
