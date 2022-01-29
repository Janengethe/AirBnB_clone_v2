#!/usr/bin/python3
"""
script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:                    display "Hello HBNB!"
            /hbnb:                display "HBNB"
            /c/<text>:            display "C" + text (replace "_" with " ")
            /python/<text>:       display "Python" + text (default="is cool")
            /number/<n>:          display "n is a number" only if int
            /number_template/<n>: display HTML page only if n is int
            /number_odd_or_even/<n>: display HTML page; display odd/even info
            /states_list:         display HTML and state info from storage;
"""
from flask import Flask
from flask import render_template
from models import storage

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


@app.teardown_appcontext
def tear_down():
    """
    removes the current SQLAlchemy Session after each request
    calls storage.close()
    """
    storage.close()


@app.route("/states_list")
def states_list():
    """
    Displays HTML page with States
    and a list of State objects in DBStorage
    """
    states = storage.all(classes["State"]).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states")
def cities_by_states():
    """Displays states with city list"""
    states = storage.all(classes["State"]).values()
    return (render_template('8-cities_by_states.html', states=states))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
