from functions import import_team, player_adjustments, team_calc, match_calc

def main():
    # load the teams based on player selections
    home, away = import_team.player_load()
    
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
    match_calc.calc_possesion(home_chances, away_chances)

    # calculate how many goals are scored
    match_calc.calc_goals(home_on_target, away_on_target, def_counth, att_counth, att_counta, def_counta)

main()
