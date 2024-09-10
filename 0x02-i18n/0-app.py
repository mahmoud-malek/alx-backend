#!/usr/bin/env python3

""" a module for running the flask app """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world() -> str:
    """ root route """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
