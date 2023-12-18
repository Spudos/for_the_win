import sqlite3

def player_load():
    # Connect to the database
    conn = sqlite3.connect('for_the_win.db')
    cursor = conn.cursor()

    # Retrieve multiple records
    cursor.execute("SELECT * FROM players WHERE club = 'ALVWOL'")
    records = cursor.fetchall()

    # Close the connection
    conn.close()

    return records

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
        perf = int(((pa + co + tk + ru + sh + he + fl + st + cr) * fit / 100)/2)
        
        # Save the calculated result
        results.append((name, perf))

    return results  # Adjust the indentation of the return statement

def player_perf_print(data):
    # Print the results
    for record in data:
        print(f"Player: {record[0]}, Perf: {record[1]}")

def main():
    data = player_load()
    data1 = calc_on_player_fitness(data)
    player_perf_print(data1)

main()