from flask import Flask
import string
import random


#https://flask.palletsprojects.com/en/2.3.x/
app = Flask(__name__)

@app.route("/")
def shortener():
    return "<p>URL Shortener</p>"


def generate_short_url(length = 6):
    chars = string.ascii_letters + string.digits
    short_url = "".join([random.choice(chars) for x in range(length)])
    return short_url
