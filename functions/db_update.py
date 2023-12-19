import sqlite3

def update_player_stats(goals_list):
    # Connect to the SQLite database
    conn = sqlite3.connect("for_the_win.db")
    cursor = conn.cursor()

    # Iterate through the goals_list and update the player stats
    for goal in goals_list:
        scored_by = goal['scored_by']
        assisted_by = goal['assisted_by']

        # Update the goals column by 1
        cursor.execute("UPDATE players SET gls = gls + 1 WHERE name = ?", (str(scored_by),))

        # Update the assists column by 1
        cursor.execute("UPDATE players SET asst = asst + 1 WHERE name = ?", (str(assisted_by),))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()