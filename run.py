from functions import import_team, player_adjustments, team_calc

def player_perf_print(data):
    # Print the results
    for record in data:
        print(f"Player: {record[1]}, Perf: {record[16]}")

def main():
    data = import_team.player_load()
    data1 = player_adjustments.calc_on_player_fitness(data)
    def_count, mid_count, att_count = team_calc.calculate_team(data1)
  
main()
