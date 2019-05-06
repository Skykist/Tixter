from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Cha12345@localhost:5433/tixterdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rxcoocabwqxkny:f2437d9fa13163136acf06b7a31f31f9843962af3d34742d886fad789911fd03@ec2-54-225-116-36.compute-1.amazonaws.com:5432/dal2c5gdmpse1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    movieID = db.Column(db.Integer, primary_key=True)
    movieTitle = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    length = db.Column(db.String(30))

    def __init__(self, title, description, length):
        self.movieTitle = title
        self.description = description
        self.length = length
    
    def __repr__(self):
        return '<Movie %r>' % self.movieTitle
"""
Importing movie:
after activating env:
>python
>from model import Movie
>from model import db
>new = Movie("...") to create object
>db.session.add(new)
>db.session.commit()
"""
"""
Updating movie:
in python:
>update = movie.query.filter_by(id=1).first()
>update
>update.length = "00h 00m"
>db.session.commit()
"""
"""
Deleting row:
>update = movie.query.filter_by(id=1).first()
>update
>db.session.delete(update)
>db.session.commit()
"""

class Theater(db.Model):
    theaterID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    phoneNbr = db.Column(db.String(100))

    def __init__(self, id, name, address, number):
        self.theaterID = id
        self.name = name
        self.address = address
        self.phoneNbr = number
    
    def __repr__(self):
        return '<Theater %r>' % self.name

class Showtime(db.Model):
    showtimeID = db.Column(db.Integer, primary_key=True)
    movieID = db.Column(db.Integer)
    theaterID = db.Column(db.Integer)
    showtime = db.Column(db.Time)
    date = db.Column(db.Date)
    price = db.Column(db.Numeric)

    def __init__(self, movieID, theaterID, showtime, date, price):
        self.movieID = movieID
        self.theaterID = theaterID
        self.showtime = showtime
        self.date = date
        self.price = price
    
    def __repr__(self):
        return '<Showtime %r>' % self.showtime

if __name__ == "__main__":
    app.run()