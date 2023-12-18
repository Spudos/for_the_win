import sqlite3

def player_load():
    home_abbr = input("Please enter the team code for the home team: ").upper()
    away_abbr = input("Please enter the team code for the away team: ").upper()

    # Connect to the database
    conn = sqlite3.connect('for_the_win.db')
    cursor = conn.cursor()

    # Retrieve multiple records
    cursor.execute("SELECT * FROM players WHERE club = ?", (home_abbr,))
    team_home = cursor.fetchall()

    cursor.execute("SELECT * FROM players WHERE club = ?", (away_abbr,))
    team_away = cursor.fetchall()

    # Close the connection
    conn.close()

    return team_home, team_away, home_abbr, away_abbr