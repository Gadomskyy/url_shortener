from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random
from datetime import datetime

#https://flask.palletsprojects.com/en/2.3.x/
app = Flask(__name__, static_folder='./templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Links(db.Model):
    #if you add any additional columns here, you need to re-run the database or find a way to add wanted columns
    #commands to create new database
    """
    from shortener import app, db
    app.app_context().push()
    db.create_all()
    """
    #watch out when recreating db when data already exists there
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(6), nullable=False)
    full_short_url = db.Column(db.String(50), nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def __repr__(self):
        return f"Long link: {self.long_url}, short link: {self.short_url}"

    def generate_short_url(self, length=6):
        chars = string.ascii_letters + string.digits
        self.short_url = "".join([random.choice(chars) for x in range(length)])
        while Links.query.filter_by(short_url=self.short_url).first():
            self.generate_short_url()
        return self.short_url


@app.route("/", methods=['GET', 'POST'])
def mainpage():
    if request.method == 'POST':
        action = request.form.get('action')
        #generate short_url
        if action == 'generate_url':
            #read long URL posted by client
            long_url = request.form['long_url']
            #create Links object to be added to db
            link = Links(long_url=long_url, create_date=datetime.now())
            #full short URL to be shown to client
            full_short_url = f"{request.url_root}{link.short_url}"
            link.full_short_url = full_short_url
            #add data to database
            db.session.add(link)
            db.session.commit()
            #return visual information on site
            return render_template('result.html', short_url=link.full_short_url)
    return render_template('mainpage.html')

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    link = Links.query.filter_by(short_url=short_url).first_or_404()
    return redirect(link.long_url)

if __name__ == '__main__':
    app.run(debug=True)