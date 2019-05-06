from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Cha12345@localhost:5433/tixterdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    movieID = db.Column(db.Integer, primary_key=True)
    movieTitle = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(500))
    length = db.Column(db.String(30))

    def __init__(self, title, description, length):
        self.movieTitle = movieTitle
        self.email = email
        self.description = description
        self.length = length
    
    def __repr__(self):
        return '<Movie %r>' % self.movieTitle

@app.route("/")
def home():
    return render_template('get_movie.html')

@app.route('/get_movie')
def get_movie():
    return True

if __name__ == "__main__":
    app.run()