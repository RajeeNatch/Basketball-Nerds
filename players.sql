CREATE TABLE IF NOT EXISTS public.teams
(
  team_id INT NOT NULL,
  team_full_name VARCHAR ( 50 ) UNIQUE NOT NULL,
  PRIMARY KEY (team_id)
  
);

CREATE TABLE IF NOT EXISTS public.players
(
  player_id INT NOT NULL,
  first_name VARCHAR ( 50 ) UNIQUE NOT NULL,
  last_name VARCHAR ( 50 ) UNIQUE NOT NULL,
  positions VARCHAR ( 50 ) UNIQUE NOT NULL,
  team_id INT NOT NULL,
  team_full_name VARCHAR ( 50 ) UNIQUE NOT NULL,
  PRIMARY KEY (player_id),
  FOREIGN KEY (team_id)
      REFERENCES teams (team_id)
);

CREATE TABLE public.games
(
  game_id INT NOT NULL,
  game_date DATE NOT NULL,
  home_team_score INT NOT NULL,	
  periods INT NOT NULL,	
  postseason VARCHAR (10) NOT NULL,	
  season INT NOT NULL,	
  status VARCHAR (10) NOT NULL,		
  visitor_team_score INT NOT NULL,	
  home_team_id INT NOT NULL,
  home_team_full_name VARCHAR ( 50 ) UNIQUE NOT NULL,	
  visitor_team_id INT NOT NULL,	
  visitor_team_full_name VARCHAR ( 50 ) UNIQUE NOT NULL,
  player_id INT NOT NULL
  );
  
  CREATE TABLE public.stats
(
	stats_id INT NOT NULL,	
	ast	INT NOT NULL,
	blk	INT NOT NULL,
	dreb INT NOT NULL,	
	fg3_pct INT NOT NULL,
	pts	INT NOT NULL,
	reb	INT NOT NULL,
	stl	INT NOT NULL,
	turnover INT NOT NULL,	
	game_season INT NOT NULL,	
	player_id INT NOT NULL,	
	player_first_name VARCHAR (50) NOT NULL,	
	player_height_feet INT NOT NULL,	
	player_last_name VARCHAR (50) NOT NULL,	
	player_position VARCHAR (10) NOT NULL,		
	player_team_id INT NOT NULL,	
	team_id	INT NOT NULL,
	team_full_name VARCHAR (50) NOT NULL
  );

ALTER TABLE teams
ADD CONSTRAINT PK_teams PRIMARY KEY (team_id)

ALTER TABLE players
ADD CONSTRAINT PK_players PRIMARY KEY (player_id)

ALTER TABLE games
ADD CONSTRAINT PK_teams PRIMARY KEY (games_id)

ALTER TABLE stats
ADD CONSTRAINT PK_teams PRIMARY KEY (id)
