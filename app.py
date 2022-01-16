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
    
    ##First Chart##
    p_df = pd.read_sql('select * from stats_avg', engine)
    
    ps_df = p_df.rename(columns={"player fullname":"player_name"})
    ps_df = ps_df.drop(['index'], axis=1)
    ps_df=ps_df.round({'ast': 2, 'blk': 2,'pts': 2,'reb': 2,'stl': 2,'turnover': 2})
    ps_df=ps_df.fillna(0)
    fig = go.Figure(data=[go.Table(
    header=dict(values=list(ps_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[ps_df.pgame_season, ps_df.player_name, ps_df.ast, ps_df.blk, ps_df.pts, ps_df.reb, ps_df.stl, ps_df.turnover],
               fill_color='lavender',
               align='left'))
])
    
    ##Secon Chart##
    ps_long_df = pd.melt(ps_df, id_vars=['pgame_season','player_name'], value_vars=['ast', 'blk', 'pts','reb','stl','turnover'],
             var_name='metric', value_name='amount')
    stat_lines = ['metric','amount'] # or df_users_community.columns[3:]
    player_1=ps_long_df.loc[12341]
    

    fig3 = px.bar(ps_long_df, x='metric', y='amount',color='player_name', animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Player Stats')
    fig3.update_traces(width=.2)
    # return str(players_table)
    graph2JSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(fig3, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template("players_Page.html", players=graph2JSON, graph3JSON=graph3JSON)


@app.route("/season_leaders/")
def stat():
    p_df = pd.read_sql('select * from stats_avg', engine)
    
    ps_df = p_df.rename(columns={"player fullname":"player_name"})
    ps_df = ps_df.drop(['index'], axis=1)
    ps_df=ps_df.round({'ast': 2, 'blk': 2,'pts': 2,'reb': 2,'stl': 2,'turnover': 2})
    ps_df=ps_df.fillna(0)
    ###
    pts_df=ps_df[['pgame_season','player_name','pts']]
    new_df1=pts_df.sort_values(by=['pgame_season','pts'],ascending=False)
    pts_leader_df=new_df1.groupby('pgame_season').head(3).reset_index(drop=True)
    fig5 = go.Figure(data=[go.Table(
    header=dict(values=list(pts_leader_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[pts_leader_df.pgame_season, pts_leader_df.player_name, pts_leader_df.pts],
               fill_color='lavender',
               align='left'))])
    ###
    ast_df=ps_df[['pgame_season','player_name','ast']]
    new_df2=ast_df.sort_values(by=['pgame_season','ast'],ascending=False)
    ast_leader_df=new_df2.groupby('pgame_season').head(3).reset_index(drop=True)
    fig6 = go.Figure(data=[go.Table(
    header=dict(values=list(ast_leader_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[ast_leader_df.pgame_season, ast_leader_df.player_name, ast_leader_df.ast],
               fill_color='lavender',
               align='left'))])
    ###
    reb_df=ps_df[['pgame_season','player_name','reb']]
    new_df3=reb_df.sort_values(by=['pgame_season','reb'],ascending=False)
    reb_leader_df=new_df3.groupby('pgame_season').head(3).reset_index(drop=True)
    fig7 = go.Figure(data=[go.Table(
    header=dict(values=list(reb_leader_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[reb_leader_df.pgame_season, reb_leader_df.player_name, reb_leader_df.reb],
               fill_color='lavender',
               align='left'))])
    ###
    stl_df=ps_df[['pgame_season','player_name','stl']]
    new_df4=stl_df.sort_values(by=['pgame_season','stl'],ascending=False)
    stl_leader_df=new_df4.groupby('pgame_season').head(3).reset_index(drop=True)
    fig8 = go.Figure(data=[go.Table(
    header=dict(values=list(stl_leader_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[stl_leader_df.pgame_season, stl_leader_df.player_name, stl_leader_df.stl],
               fill_color='lavender',
               align='left'))])
    ###
    blk_df=ps_df[['pgame_season','player_name','blk']]
    new_df5=blk_df.sort_values(by=['pgame_season','blk'],ascending=False)
    blk_ldeader_df=new_df5.groupby('pgame_season').head(3).reset_index(drop=True)
    fig9 = go.Figure(data=[go.Table(
    header=dict(values=list(blk_ldeader_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[blk_ldeader_df.pgame_season, blk_ldeader_df.player_name, blk_ldeader_df.blk],
               fill_color='lavender',
               align='left'))])
    ###
    to_df=ps_df[['pgame_season','player_name','turnover']]
    new_df5=to_df.sort_values(by=['pgame_season','turnover'],ascending=False)
    turnover_ldeader_df=new_df5.groupby('pgame_season').head(3).reset_index(drop=True)
    fig10 = go.Figure(data=[go.Table(
    header=dict(values=list(turnover_ldeader_df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[turnover_ldeader_df.pgame_season, turnover_ldeader_df.player_name, turnover_ldeader_df.turnover],
               fill_color='lavender',
               align='left'))])
    ###
    fig5 = px.bar(pts_leader_df, x='player_name', y='pts',color = "pts", animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Scoring Leaders')
    ###
    fig6 = px.bar(ast_leader_df, x='player_name', y='ast',color = "ast", animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Assist Leaders')
    ###
    fig7 = px.bar(reb_leader_df, x='player_name', y='reb',color = "reb", animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Rebound Leaders')
    ###
    fig8 = px.bar(stl_leader_df, x='player_name', y='stl',color = "stl", animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Steals Leaders')
    ###
    fig9 = px.bar(blk_ldeader_df, x='player_name', y='blk',color = "blk", animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Block Leaders')
    ###
    fig10 = px.bar(turnover_ldeader_df, x='player_name', y='turnover', color = "turnover",animation_frame='pgame_season', 
                labels={'variable':'categorie, whatever', 'value':'count,value,whatever'}, 
                barmode='group', title='Turnover Leaders')
    
    
    graph5JSON = json.dumps(fig5, cls = plotly.utils.PlotlyJSONEncoder)
    graph6JSON = json.dumps(fig6, cls = plotly.utils.PlotlyJSONEncoder)
    graph7JSON = json.dumps(fig7, cls = plotly.utils.PlotlyJSONEncoder)
    graph8JSON = json.dumps(fig8, cls = plotly.utils.PlotlyJSONEncoder)
    graph9JSON = json.dumps(fig9, cls = plotly.utils.PlotlyJSONEncoder)
    graph10JSON = json.dumps(fig10, cls = plotly.utils.PlotlyJSONEncoder)
    return render_template("season_leaders.html", graph5JSON=graph5JSON,graph6JSON=graph6JSON,graph7JSON=graph7JSON,graph8JSON=graph8JSON,graph9JSON=graph9JSON,graph10JSON=graph10JSON)


if __name__ == '__main__':
    app.run(debug=True)
