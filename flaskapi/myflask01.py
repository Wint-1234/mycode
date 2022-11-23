#!/usr/bin/python3

# Import modules
from flask import Flask
import random


random_ironbowl_facts = [
        "In Auburn wins, the average score is 26-13",
        "In Bama wins, the average score is 27-9",
        "The average margin for every game: Bama 21, Auburn 16.",
        "The exact all-time scoring margin: Bama leads, 1,675-1,307",
        "2017 marks the 70th consecutive year the teams have played",
        "The game has been played in four different cities: Birmingham: 53 times, Auburn: 13 times, Tuscaloosa: 11 times, Montgomery: 4 times",
        "Total points have ranged from 3 to 99",
        "National titles are often on the line, directly or indirectly.",
        "The series has featured five Heisman winners"
        ]

app = Flask(__name__)

@app.route("/auburn")
def auburn_football():
   return {
            "Record": "5-6 (77th of 131)", 
            "Conference": "SEC (West Division)",
            "Coach": "Bryan Harsin (3-5), Cadillac Williams (2-1)"
           }

@app.route("/alabama")
def alabama_football():
   return {
            "Record": "9-2 (8th of 131)",
            "Conference": "SEC (West Division)",
            "Coach": "Nick Saban"
           }

@app.route("/alabama/teams")
def alabama_teams():
   return ["Alabama", "Auburn"]


@app.route("/alabama/ironbowl")
def ironBowl():
   return random.choice(random_ironbowl_facts)

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

