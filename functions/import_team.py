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