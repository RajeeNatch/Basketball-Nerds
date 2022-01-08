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

