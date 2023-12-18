import random

def calc_on_player_fitness(data):
    # Perform calculation on each stat and save the results
    print()
    print("Calculating fitness adjustment for players.....")
    print()

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
        perf = int((pa + co + tk + ru + sh + he + fl + st + cr) * fit / 100)
        
        record_with_perf = record + (perf,)  # Using tuple concatenation to add the performance
        
        # Save the calculated result
        results.append(record_with_perf)
        
        print(record_with_perf)


    return results

def calc_on_player_random_perf(data):
    # Perform calculation on each stat and save the results
    print()
    print("Calculating randomly adjusted perf for players.....")
    print()

    data = list(data)

    for i, record in enumerate(data):
        name = record[1]
        perf = int(record[16])

        random_adjustment = random.randint(-20, 20)
        new_perf = int(perf + random_adjustment)

        # Save the adjusted performance value to the record
        record = record[:16] + (new_perf,)
        data[i] = record
        
        print(name, perf, " ---> ", new_perf)

    # Convert the list back to a tuple if needed
    data = tuple(data)

    return data


