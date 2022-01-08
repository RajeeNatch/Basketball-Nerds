import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime

from flask import Flask, jsonify, render_template
from config import DB_KEY
import pandas as pd
import plotly
import json

#################################################
# Database Setup
#################################################

connection_string = "postgres:Dontforget123!@localhost:5432/Basketball_stats"
engine = create_engine(f'postgresql://{connection_string}')

# reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# Save reference to the table
# Players = Base.classes.players
# Teams = Base.classes.teams


# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")

def index():
    players_table = list(engine.execute("select * from players"))
    # return str(players_table)
    return render_template("index.html")


@app.route("/players")
def players():
    players_table = list(engine.execute("select * from players"))
    # return str(players_table)
    return render_template("players_Page.html", players=players_table)

# @app.route("/teams/")
# def teams():
#     teams_table = list(engine.execute("select * from teams"))
#     return str(teams_table)


    # session = Session(engine)
    # print(session.query(Players.id).all())
#     """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/home_Page.html<br/>"
    #     f"/api/v1.0/player_Page.html"
    #     f"/api/v1.0/team_Page.html"
    # )


# @app.route("/api/v1.0/home_Page.html")
# def names():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of all passenger names"""

#     # Query all passengers
#     results = session.query(Passenger.name).all()

#     session.close()

#     # Convert list of tuples into normal list
#     all_names = list(np.ravel(results))

#     return jsonify(all_names)


# @app.route("/api/v1.0/passengers")
# def passengers():
#     # Create our session (link) from Python to the DB
#     session = Session(engine)

#     """Return a list of passenger data including the name, age, and sex of each passenger"""
#     # Query all passengers
#     results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

#     session.close()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_passengers = []
#     for name, age, sex in results:
#         passenger_dict = {}
#         passenger_dict["name"] = name
#         passenger_dict["age"] = age
#         passenger_dict["sex"] = sex
#         all_passengers.append(passenger_dict)

#     return jsonify(all_passengers)

if __name__ == '__main__':
    app.run(debug=True)
