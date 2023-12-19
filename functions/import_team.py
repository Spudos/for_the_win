import sqlite3

def player_load():
    hm_abbr = input("Please enter the team code for the hm team: ").upper()
    aw_abbr = input("Please enter the team code for the aw team: ").upper()

    # Connect to the database
    conn = sqlite3.connect('for_the_win.db')
    cursor = conn.cursor()

    # Retrieve multiple records
    cursor.execute("SELECT * FROM players WHERE club = ?", (hm_abbr,))
    team_hm = cursor.fetchall()

    cursor.execute("SELECT * FROM players WHERE club = ?", (aw_abbr,))
    team_aw = cursor.fetchall()

    # Close the connection
    conn.close()

    return list(team_hm), list(team_aw), hm_abbr, aw_abbr