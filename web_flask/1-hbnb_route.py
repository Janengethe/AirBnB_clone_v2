#!/usr/bin/python3
"""
Module 1-hello_route.Starts a Flask Web App
Test on tab 1:python3 -m web_flask.1-hello_route
On another tab:curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
