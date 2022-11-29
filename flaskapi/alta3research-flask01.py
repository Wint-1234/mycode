#!/usr/bin/env python3

# Import modules
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import requests

# ======================================================================================================
# This API has a landing page with the top-grossing movie of each calendar year.                        
# There are multiple endpoints provided, most of which query another API (OMDb API)
# to gather information and return it to the client. Endpoints include:
#
#    -> ("/") = Landing page, return all movies as JSON with respective year
#    -> ("/allMovies") = Returns list of top-grossing movies of each calendar year 
#    -> ("/allMoviesWithInfo") = Returns movie-specific data of the top-grossing movies
#    -> ("/searchForMovie/<movie>") = Returns interactive html that injects the searched data
#                                  onto the page using jinja2
#    -> ("/searchForMovieNoJinJa2/<movie>") = Returns movie data with no html
#    -> ("/searchForMovieByYear/<movie>/<year>") = Returns movie-specific data, with an added
#                                               search parameter of year
#    -> ("/searchForMovieAndAwards/<movie>") = Returns movie awards
#    -> ("/plotAndRatings/<movie>") = Returns the plot and ratings of a movie   

# Movie info contains the following: "Actors", "Awards", "BoxOffice", "Country", "DVD", "Director",
# "Genre", "Language", "Metascore": "73", "Plot", "Poster", "Production", "Rated", "Ratings",
# "Released", "Title", etc.
# ======================================================================================================

apiURL = "https://www.omdbapi.com/?"            # URL for OMDb API Database
top_movies_list_with_info = []

# Top-grossing movie of each calendar year (based on worldwide box office) 2022 - 1975,
# Source = https://www.the-numbers.com/movies/#tab=year owned by Nash Information Services, LLC
top_movies = ["Top Gun: Maverick", "Spider-Man: No Way Home", "Demon Slayer the Movie: Mugen Train", "Avengers: Endgame",
"Avengers: Infinity War", "Star Wars: Episode VIII - The Last Jedi", "Captain America: Civil War", "Star Wars: Episode VII - The Force Awakens",
"Transformers: Age of Extinction", "Frozen", "The Avengers", "Harry Potter and the Deathly Hallows: Part 2", "Toy Story 3", "Avatar",
"The Dark Knight", "Pirates of the Caribbean: At World's End", "Pirates of the Caribbean: Dead Man's Chest", "Harry Potter and the Goblet of Fire,", 
"Shrek 2", "The Lord of the Rings: The Return of the King", "The Lord of the Rings: The Two Towers", "Harry Potter and the Sorcerer's Stone", "Mission: Impossible 2",
"Star Wars: Episode I - The Phantom Menace", "Armageddon", "Titanic", "Independence Day", "Die Hard: With a Vengeance", "The Lion King", "Jurassic Park",
"Aladdin", "Terminator 2: Judgment Day", "Ghost", "Indiana Jones and the Last Crusade", "Rain Man", "Fatal Attraction", "Top Gun", "Back to the Future",
"Indiana Jones and the Temple of Doom", "Star Wars: Episode VI - Return of the Jedi", "E.T. the Extra-Terrestrial", "Raiders of the Lost Ark", 
"Star Wars: Episode V - The Empire Strikes Back", "Moonraker", "Grease", "Star Wars: Episode IV - A New Hope", "Rocky", "Jaws"]

# Get API key for OMDb API
creds = ""                                                            # Credentials to perform API call
with open("/home/student/miniproject.creds") as mycreds:
  creds = "apikey=" + mycreds.read().strip("\n")

app = Flask(__name__)

# Return all movies as JSON
@app.route("/", methods=["GET"])
def index():
  movie_dictionary = {}
  year = 2022
  for movie in top_movies:
    movie_dictionary[year] = movie
    year -= 1
  return jsonify((movie_dictionary))

# Return all movies 
@app.route("/allMovies")
def getAllMovies():
  return top_movies

# Get info of all movies from the OMDb API and return the data
@app.route("/allMoviesWithInfo")
def getTopGrossingMoviesWithInfo():
  for movie in top_movies:
    full_apiURL = apiURL + creds + "&t=" + movie
    movie_info = requests.get(full_apiURL).json()
    top_movies_list_with_info.append(movie_info)
  return top_movies_list_with_info

# Get info of a particular movie from the OMDb API and return HTML that uses jinja2 logic
@app.route("/searchForMovie/<movie>")
def searchForMovie(movie):
  full_apiURL = apiURL + creds + "&t=" + movie
  movie_info = requests.get(full_apiURL).json()
  return render_template("index.html", movie_name = movie, movie_data = movie_info)

# Get info of a particular movie from the OMDb API
@app.route("/searchForMovieNoJinJa2/<movie>")
def searchForMovieNoJinJa2(movie):
  full_apiURL = apiURL + creds + "&t=" + movie
  movie_info = requests.get(full_apiURL).json()
  return movie_info

# Get info of a particular movie with a specific year from the OMDb API
@app.route("/searchForMovieByYear/<movie>/<year>")
def searchForMovieByYear(movie, year):
  full_apiURL = apiURL + creds + "&t=" + movie + "&y=" + str(year)
  movie_info = requests.get(full_apiURL).json()
  return movie_info

# Get the awards of a particular movie from the OMDb API
@app.route("/searchForMovieAndAwards/<movie>")
def searchForMovieAndAwards(movie):
  full_apiURL = apiURL + creds + "&t=" + movie
  movie_info = requests.get(full_apiURL).json()
  awards = movie_info["Awards"]
  return awards

# Get the Plot and Ratings of a particular movie from the OMDb API
@app.route("/plotAndRatings/<movie>")
def plotAndRatings(movie):
  full_apiURL = apiURL + creds + "&t=" + movie
  movie_info = requests.get(full_apiURL).json()
  title = movie_info["Title"]
  plot = movie_info["Plot"]
  ratings = movie_info["Ratings"]
  movie_dictionary = {"Title": title, "Plot": plot, "Ratings": ratings}
  return movie_dictionary

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224) # runs the application

