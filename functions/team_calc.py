def calculate_team(data):
    print()
    print("Calculating total team values.....")
    # Initialize position counters
    def_count = 0
    mid_count = 0
    att_count = 0

    # Iterate through the player data
    for record in data:
        perf = record[22]
        pos = record[5]
     
        # Add the performance to the respective position counter
        if pos == "GK":
            def_count += perf
        elif pos == "DEF":
            def_count += perf       
        elif pos == "MID":
            mid_count += perf
        elif pos == "ATT":
            att_count += perf
    
    print()
    print("Team values calculated")
    print("Defence: ", def_count, " Midfield: ", mid_count, " Attack: ", att_count)

    return def_count, mid_count, att_count