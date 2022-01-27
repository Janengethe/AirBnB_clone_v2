#!/usr/bin/python3
"""
Module 5-number_template.Starts a Flask Web App
Test on tab 1:python3 -m web_flask.5-number_template
On another tab:curl 0.0.0.0:5000/number_template/<n> ; echo "" | cat -e
"""
from flask import Flask
from flask import render_template

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


@app.route("/python")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable
    replaces underscore _ symbols with a space
    The default value of text is “is cool”
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route("/number/<int:n>")
def is_number(n):
    """display text only if int given"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_even(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    number = "even" if (n % 2 == 0) else "odd"
    return render_template("6-number_odd_or_even.html", n=n, number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
