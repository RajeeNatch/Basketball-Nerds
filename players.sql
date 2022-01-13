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

ALTER TABLE teams
ADD CONSTRAINT PK_teams PRIMARY KEY (team_id)

ALTER TABLE players
ADD CONSTRAINT PK_players PRIMARY KEY (player_id)

ALTER TABLE games
ADD CONSTRAINT PK_teams PRIMARY KEY (games_id)

ALTER TABLE stats
ADD CONSTRAINT PK_teams PRIMARY KEY (id)
