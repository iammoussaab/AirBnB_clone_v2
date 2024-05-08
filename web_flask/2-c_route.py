#!/usr/bin/python3
"""
script starts Flask web app

listen on 0.0.0.0, port 5000

Routes:
        /: display "Hello HBNB!".
        /hbnb: display "HBNB".
        /c/<text>: display "C"
"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """display text"""
    return ("C {}".format(text.replace("_", " ")))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
