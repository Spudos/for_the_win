from functions import import_team, player_adjustments, team_calc, match_calc

def main():
    data = import_team.player_load()
    data1 = player_adjustments.calc_on_player_fitness(data)
    def_count, mid_count, att_count = team_calc.calculate_team(data1)
    home_chances, away_chances = match_calc.calc_chances(mid_count)
    home_on_target, away_on_target = match_calc.calc_on_target(home_chances, away_chances, att_count, def_count)
    match_calc.calc_possesion(home_chances, away_chances)
    match_calc.calc_goals(home_on_target, away_on_target, def_count, att_count)
main()
