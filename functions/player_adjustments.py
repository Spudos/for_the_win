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
        print()
        
    return results  # Adjust the indentation of the return statement


