import sqlite3

def player_load():
    aw_abbr = input("Please enter the team code for the aw team: ").upper()

    # Connect to the database
    conn = sqlite3.connect('for_the_win.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM players WHERE club = ?", (aw_abbr,))
    team_aw = cursor.fetchall()

    # Close the connection
    conn.close()

    return list(team_aw), aw_abbr