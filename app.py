import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime
from flask import Flask, jsonify
from config import DB_KEY

#################################################
# Database Setup
#################################################

connection_string = f"postgres:{DB_KEY}@localhost:5432/Basketball_stats"
engine = create_engine('postgresql://{connection_string}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Players = Base.classes.players
Teams = Base.classes.teams

# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def players():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/home_Page.html<br/>"
        f"/api/v1.0/player_Page.html"
        f"/api/v1.0/team_Page.html"
    )


@app.route("/api/v1.0/home_Page.html")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""

    # Query all passengers
    results = session.query(Passenger.name).all()

    session.close()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


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


# if __name__ == '__main__':
#     app.run(debug=True)
