import random

def calc_on_player_fitness(data):
    # Perform calculation on each stat and save the results
    results = []
    for record in data:
        name = record[1]
        age = int(record[3])
        pos = record[5]
        pa = int(record[6])
        co = int(record[7])
        tk = int(record[8])
        ru = int(record[9])
        sh = int(record[10])
        he = int(record[11])
        fl = int(record[12])
        st = int(record[13])
        cr = int(record[14])
        fit = int(record[15])

        # Perform calculation on each stat
        # Use different stats based on the value of POS
        if pos == "GK":
            perf = int(((pa + co + sh + he + st) + (tk + ru + fl + cr)/2) * fit / 100)
        elif pos == "DEF":
            perf = int(((co + tk + ru + he + st) + (pa + sh + fl + cr)/2) * fit / 100)            
        elif pos == "MID":
            perf = int(((pa + co + ru + fl + cr)  + (tk + sh + he + st)/2)* fit / 100) 
        else:
            perf = int(((co + ru + sh + fl + st)  + (pa + tk + he + cr)/2)* fit / 100)

        ts = co + ru + sh + fl + st  + pa + tk + he + cr
        
        record_with_perf = record + (ts,) + (perf,)
        
        # Save the calculated result
        results.append(record_with_perf)

    return results

def calc_on_player_random_perf(data):

    for i, record in enumerate(data):
        name = record[1]
        perf = int(record[21])

        random_adjustment = random.randint(-20, 20)
        new_perf = int(perf + random_adjustment)

        # Save the adjusted performance value to the record
        record = record[:22] + (new_perf,)
        data[i] = record

        print (f"player: {record[1]} pos: {record[5]} perf: {record[22]}")

    return data

def run_player_adj(hm,aw):
    hm_data = calc_on_player_fitness(hm)
    hm_data_1 = calc_on_player_random_perf(hm_data)

    aw_data = calc_on_player_fitness(aw)
    aw_data_1 = calc_on_player_random_perf(aw_data)

    return hm_data_1, aw_data_1