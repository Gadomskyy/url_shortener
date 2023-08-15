from flask import Flask


#https://flask.palletsprojects.com/en/2.3.x/
app = Flask(__name__)

@app.route("/")
def shortener():
    return "<p>URL Shortener</p>"