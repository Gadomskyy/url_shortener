from flask import Flask, render_template, request
import string
import random


#https://flask.palletsprojects.com/en/2.3.x/
app = Flask(__name__)

@app.route("/", methods= ['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_url = f"{request.url_root}{generate_short_url()}"
        return f"""
        Long URL: {long_url}
        Shortened URL: {short_url}"""
    return render_template('mainpage.html')


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join([random.choice(chars) for x in range(length)])
    return short_url


if __name__ == '__main__':
    app.run(debug=True)