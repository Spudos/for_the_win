def calculate_team(data):
    print()
    print()
    print("team_calc")
    print(data)
    # Initialize position counters
    def_count = 0
    mid_count = 0
    att_count = 0

    # Iterate through the player data
    for record in data:
        adj_perf = record['adj_perf']
        pos = record['pos']
     
        # Add the performance to the respective position counter
        if pos == "GK":
            def_count += adj_perf
        elif pos == "DEF":
            def_count += adj_perf       
        elif pos == "MID":
            mid_count += adj_perf
        elif pos == "ATT":
            att_count += adj_perf
    
    print()
    print("Team values calculated")
    print("Defence: ", def_count, " Midfield: ", mid_count, " Attack: ", att_count)

    return def_count, mid_count, att_count