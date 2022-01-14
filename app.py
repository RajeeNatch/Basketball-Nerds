import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime
import plotly.express as px
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

games_table_df = pd.read_sql_query('select * from "seasons"', con=engine)

# games_table = list(engine.execute("select * from games"))

# games_table_df = pd.games_table
# print(games_table_df)

# Flask Setup
#################################################
app = Flask(__name__)

# teams_headings = ("index", "team_id", "team_full_name")
#################################################
# Flask Routes
#################################################


@app.route("/")
def index():
    # teams_table = list(engine.execute("select * from seasons"))
    season_df = pd.read_sql('select * from seasons', engine)
    fig1 = px.line(season_df, x='Season', y='Win%', title='Teams Legacy')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", seasons=season_df, graph1JSON=graph1JSON)


@app.route("/teams-data")
def teams():
    # teams_table = list(engine.execute("select * from seasons"))
    season_df = pd.read_sql('select * from seasons', engine)
    fig1 = px.line(season_df, x='Season', y='Win%', title='Teams Legacy')
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    # return render_template("index.html", seasons=season_df, graph1JSON=graph1JSON)
    return season_df.to_json(orient='records')


@app.route("/players")
def players():
    players_table = list(engine.execute("select * from players"))
    # return str(players_table)
    return render_template("players_Page.html", players=players_table)


@app.route("/schedules/")
def games():
    games_table = list(engine.execute("select * from games"))
    return render_template("schedule_Page.html", games=games_table)


if __name__ == '__main__':
    app.run(debug=True)
