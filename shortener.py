from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import string
import random

#https://flask.palletsprojects.com/en/2.3.x/
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), nullable=False)
    generated_url_end = db.Column(db.String(6), nullable=False)
    short_url = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Long link: {self.long_url}, short link: {self.short_url}"


@app.route("/", methods= ['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = f"{request.url_root}{generate_short_url()}"
        return f"""
        Long URL: {long_url}\n
        Shortened URL: {short_url}"""
    return render_template('mainpage.html')


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join([random.choice(chars) for x in range(length)])
    return short_url


if __name__ == '__main__':
    app.run(debug=True)