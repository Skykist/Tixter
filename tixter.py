from flask import Flask, render_template, url_for
app = Flask(__name__)
from model import *

@app.route("/")
@app.route("/home")
def home():
    showtimes = Showtime.query.join(Movie,Movie.movieID == Showtime.movieID).order_by(Showtime.price,Showtime.showtime).all()
    movies = Movie.query.all()
    theaters = Theater.query.all()
    return render_template('home.html',showtimes=showtimes, movies=movies, theaters=theaters)

@app.route("/movies")
def getMovies():
    moviesList = Movie.query.all()
    return render_template('movies.html',title='Now Playing', moviesList=moviesList)

@app.route("/theaters")
def getTheaters():
    theaters = Theater.query.all()
    return render_template('theaters.html',title='Theaters',theaters=theaters)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/help")
def help():
    return render_template('help.html',title='Help')

if __name__ == "__main__":
    app.run(debug=True)  