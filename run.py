from functions import import_team, player_adjustments, team_calc, match_calc
from datetime import datetime
import os

def text_file_match_output(home_abbr, away_abbr, data_home1, data_away1, def_counth, mid_counth, att_counth, def_counta, mid_counta, att_counta, home_chances, away_chances, home_on_target, away_on_target, home_possession, away_possession, home_goals, away_goals):
    
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Construct the file name with the current date and time
    file_name = f"match_reports/match_output_{home_abbr}_v_{away_abbr}_{current_datetime}.txt"
    
    with open(file_name, "w") as file:
        file.write(f"Home team abbr: {home_abbr}\n")
        for item in data_home1:
            file.write(f"{item}\n")
        file.write(f" \n")
        file.write(f"Away team abbr: {away_abbr}\n")
        for item in data_away1:
            file.write(f"{item}\n")
        file.write(f" \n")        
        file.write(f"Defense - home: {def_counth} away: {def_counta}\n")
        file.write(f"Midfield - home: {mid_counth} away: {mid_counta}\n") 
        file.write(f"Attack - home: {att_counth} away: {att_counta}\n")       
        file.write(f" \n")
        file.write(f"Possession - home: {home_possession} away: {away_possession}\n")        
        file.write(f"Chances - home: {home_chances} away: {away_chances}\n")
        file.write(f"On target - home: {home_on_target} - away: {away_on_target}\n")  
        file.write(f"Goals - home: {home_goals} - away: {away_goals}\n")  

def main():
    # load the teams based on player selections
    home, away, home_abbr, away_abbr = import_team.player_load()
    
    # make player adjustments and calculate team values for the home team
    data_home = player_adjustments.calc_on_player_fitness(home)
    data_home1 = player_adjustments.calc_on_player_random_perf(data_home)
    def_counth, mid_counth, att_counth = team_calc.calculate_team(data_home1)
    
    # make player adjustments and calculate team values for the away team
    data_away = player_adjustments.calc_on_player_fitness(away)
    data_away1 = player_adjustments.calc_on_player_random_perf(data_away)
    def_counta, mid_counta, att_counta = team_calc.calculate_team(data_away1)

    # calculate the number of chances per team
    home_chances, away_chances = match_calc.calc_chances(mid_counth, mid_counta)

    # claculate how many chances are on target
    home_on_target, away_on_target = match_calc.calc_on_target(home_chances, away_chances, att_counth, def_counth, att_counta, def_counta)

    # calculate the possesion stats
    home_possession, away_possession = match_calc.calc_possession(home_chances, away_chances)

    # calculate how many goals are scored
    home_goals, away_goals = match_calc.calc_goals(home_on_target, away_on_target, def_counth, att_counth, att_counta, def_counta)
    
    # output match data to a text file
    text_file_match_output(home_abbr, away_abbr, data_home1, data_away1, def_counth, mid_counth, att_counth, def_counta, mid_counta, att_counta, home_chances, away_chances, home_on_target, away_on_target, home_possession, away_possession, home_goals, away_goals)

main()

