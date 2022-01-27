#!/usr/bin/python3
"""
Module 2-c_route.Starts a Flask Web App
Test on tab 1:python3 -m web_flask.2-c_route
On another tab:curl 0.0.0.0:5000/c/<text> ; echo "" | cat -e
There must be a value in <text> otherwise returns 404
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    route function
    displays the string on url page
    """
    return ("Hello HBNB!")


@app.route("/hbnb")
def hbnb():
    """
    displays HBNB when /hbnb is used in url
    """
    return ("HBNB!")


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Dispays C followed by value in <text>
    Without the text it returns 404
    """
    return ("C {}".format(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
