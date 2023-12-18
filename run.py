
from functions import import_team, player_adjustments

def player_perf_print(data):
    # Print the results
    for record in data:
        print(f"Player: {record[0]}, Perf: {record[1]}")

def main():
    data = import_team.player_load()
    data1 = player_adjustments.calc_on_player_fitness(data)
    player_perf_print(data1)

main()