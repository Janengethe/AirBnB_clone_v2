#!/usr/bin/python3
"""
Module hello_route.Starts a Flask Web App
Test on tab 1:python3 -m web_flask.0-hello_route
On another tab:curl 0.0.0.0:5000 ; echo "" | cat -e
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    route function
    displays the string on url page
    """
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
