from functions.import_team import player_load
from functions.player_adjustments import calc_on_player_fitness

def player_perf_print(data):
    # Print the results
    for record in data:
        print(f"Player: {record[0]}, Perf: {record[1]}")

def main():
    data = player_load()
    data1 = calc_on_player_fitness(data)
    player_perf_print(data1)

main()