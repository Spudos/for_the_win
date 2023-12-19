import sqlite3

def update_player_stats(goals_list, hm_data_1, aw_data_1):
    # Connect to the SQLite database
    conn = sqlite3.connect("for_the_win.db")
    cursor = conn.cursor()
    
    for name in hm_data_1:
        # Update the played column by 1
        cursor.execute("UPDATE players SET played = played + 1 WHERE name = ?", (str(name[1]),))
        cursor.execute("UPDATE players SET perf = perf + ? WHERE name = ?", (name[21], str(name[1])))

    for name in aw_data_1:
        # Update the played column by 1
        cursor.execute("UPDATE players SET played = played + 1 WHERE name = ?", (str(name[1]),))
        cursor.execute("UPDATE players SET perf = perf + ? WHERE name = ?", (name[21], str(name[1])))
        
    # Iterate through the goals_list and update the player stats
    for goal in goals_list:
        scored_by = goal['scored_by']
        assisted_by = goal['assisted_by']

        # Update the goals column by 1
        cursor.execute("UPDATE players SET gls = gls + 1 WHERE name = ?", (str(scored_by),))

        # Update the assists column by 1
        cursor.execute("UPDATE players SET asst = asst + 1 WHERE name = ?", (str(assisted_by),))

    # Calculate average performance and update av_perf column
    cursor.execute("UPDATE players SET av_perf = CASE WHEN played > 0 THEN perf / played ELSE 0 END;")

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

