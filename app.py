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

teams_headings = ("index", "team_id", "team_full_name")
#################################################
# Flask Routes
#################################################


@app.route("/")
def teams():
    teams_table = list(engine.execute("select * from teams"))
    return render_template("index.html", teams=teams_table)


@app.route("/players")
def players():
    players_table = list(engine.execute("select * from players"))
    # return str(players_table)
    return render_template("players_Page.html", players=players_table)


@app.route("/schedules/")
def games():
    games_table = list(engine.execute("select * from games"))
    return render_template("schedule_Page.html", games=games_table)


df = pd.read_csv()
df = df[df[] == ]
if __name__ == '__main__':
    app.run(debug=True)
++
