import random

def calc_on_player_fitness(data):
    # Perform calculation on each stat and update the 'perf' field in the original data list
    for record in data:
        pos = record['pos']
        fit = record['fit']
        if pos == "GK":
            perf = int(((record['pa'] + record['co'] + record['sh'] + record['he'] + record['st']) + (record['tk'] + record['ru'] + record['fl'] + record['cr']) / 2) * fit / 100)
        elif pos == "DEF":
            perf = int(((record['co'] + record['tk'] + record['ru'] + record['he'] + record['st']) + (record['pa'] + record['sh'] + record['fl'] + record['cr']) / 2) * fit / 100)
        elif pos == "MID":
            perf = int(((record['pa'] + record['co'] + record['ru'] + record['fl'] + record['cr']) + (record['tk'] + record['sh'] + record['he'] + record['st']) / 2) * fit / 100)
        else:
            perf = int(((record['co'] + record['ru'] + record['sh'] + record['fl'] + record['st']) + (record['pa'] + record['tk'] + record['he'] + record['cr']) / 2) * fit / 100)
        
        record['perf'] = perf

    return data


def calc_on_player_random_perf(data):
    
    for i in data:
        perf = i['perf']
        random_adjustment = random.randint(-20, 20)
        i['adj_perf'] = int(perf + random_adjustment)
    
    return data

def run_player_adj(hm,aw):
    hm_data = calc_on_player_fitness(hm)
    hm_data_1 = calc_on_player_random_perf(hm_data)

    aw_data = calc_on_player_fitness(aw)
    aw_data_1 = calc_on_player_random_perf(aw_data)

    return hm_data_1, aw_data_1