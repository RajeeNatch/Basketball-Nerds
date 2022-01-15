import numpy as np
import plotly.graph_objs as go
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime
import plotly.express as px
from flask import Flask, jsonify, render_template,url_for
from config import DB_KEY
import pandas as pd
import plotly
import json
import dash
import dash_bootstrap_components as dbc
import dash_table

#################################################
# Database Setup
#################################################

connection_string = "postgres:postgres@localhost:5432/Basketball_stats"
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
dash_app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

@app.route("/")
def index():
    # teams_table = list(engine.execute("select * from seasons"))
    season_df = pd.read_sql('select * from seasons', engine)
    fig1 = px.bar(season_df, x="Season", y =["Win%"], title="Teams Legacy")
    
    layout = dict(xaxis=dict(title="Seasons"),yaxis=dict(title="Win %"))
    fig1 = go.Figure(layout=layout)    
    nba_list = list(season_df['Teams'].unique())

    for team in nba_list:
        fig1.add_trace(
            go.Scatter(
                x = season_df['Season'][season_df['Teams']==team],
                y = season_df['Win%'][season_df['Teams']==team],
                name = team, visible = True
            )
        )
        
    buttons = []

    for i, team in enumerate(nba_list):
        args = [False] * len(nba_list)
        args[i] = True
        
        button = dict(label = team,
                    method = "update",
                    args=[{"visible": args}])
        
        buttons.append(button)
        
    
    graph1JSON = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", season_df=season_df,graph1JSON=graph1JSON)


@app.route("/teams-data")
def teams():
    # teams_table = list(engine.execute("select * from seasons"))
    season_df = pd.read_sql('select * from seasons', engine)
    fig1 = px.bar(season_df, x='Season', y='Win%', title='Teams Legacy')
    graph1JSON = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)
    # return render_template("index.html", seasons=season_df, graph1JSON=graph1JSON)
    return season_df.to_json(orient='records')


@app.route("/players")
def players():
    p_df = pd.read_sql('select * from stats_avg', engine)
    ps_df = p_df.rename(columns={"player fullname":"player_name"})
    ps_df = ps_df.drop(['index'], axis=1)
    ps_df=ps_df.round({'ast': 2, 'blk': 2,'pts': 2,'reb': 2,'stl': 2,'turnover': 2})
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(ps_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[ps_df.pgame_season, ps_df.player_name, ps_df.ast, ps_df.blk, ps_df.pts, ps_df.reb, ps_df.stl, ps_df.turnover],
               fill_color='lavender',
               align='left'))
])
    fig.update_layout(
    updatemenus=[
        {
            "buttons": [
                {
                    "label": c,
                    "method": "update",
                    "args": [
                        {
                            "cells": {
                                "values": ps_df.T.values
                                if c == "All"
                                else ps_df.loc[ps_df["pgame_season"].eq(c)].T.values
                            }
                        }
                    ],
                }
                for c in ["All"] + ps_df["pgame_season"].unique().tolist()
            ]
        }
    ]
)
    fig3 = px.bar(ps_df, x=px.Constant('col'), y =["ast","pts"], title="player")
    
    layout = dict(xaxis=dict(title="stats"))
    fig3 = go.Figure(layout=layout)    
    player_list = list(ps_df['player_name'].unique())
    for player in player_list:
        fig3.add_trace(
            go.Scatter(
                x = ps_df['pgame_season'][ps_df['player_name']==player],
                y = ps_df['pts'][ps_df['player_name']==player],
                name = player, visible = True
            )
        )
        
    buttons = []

    for i, player in enumerate(player_list):
        args = [False] * len(player_list)
        args[i] = True
        
        button = dict(label = player,
                    method = "update",
                    args=[{"visible": args}])
        
        buttons.append(button)
        
    
    graph3JSON = json.dumps(fig3, cls = plotly.utils.PlotlyJSONEncoder)
    # return str(players_table)
    graph2JSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template("players_Page.html", players=graph2JSON, graph3JSON=graph3JSON)


@app.route("/schedules/")
def games():
    games_table = list(engine.execute("select * from games"))
    return render_template("schedule_Page.html", games=games_table)


if __name__ == '__main__':
    app.run(debug=True)
