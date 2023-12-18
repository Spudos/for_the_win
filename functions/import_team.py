import sqlite3

def player_load():
    team_home = input("Please enter the team code for the home team: ").upper()
    
    # Connect to the database
    conn = sqlite3.connect('for_the_win.db')
    cursor = conn.cursor()

    # Retrieve multiple records
    cursor.execute("SELECT * FROM players WHERE club = ?", (team_home,))
    team_home = cursor.fetchall()


    # Close the connection
    conn.close()

    return team_home