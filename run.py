from functions import import_team, player_adjustments, team_calc, match_calc

def main():
    data = import_team.player_load()
    data1 = player_adjustments.calc_on_player_fitness(data)
    def_count, mid_count, att_count = team_calc.calculate_team(data1)
    home_chances, away_chances = match_calc.calc_chances(mid_count)
    match_calc.calc_goals(home_chances, away_chances)
    
main()
