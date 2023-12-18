import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('for_the_win.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS players
                  (id INTEGER PRIMARY KEY, name TEXT, nation TEXT, age INTEGER, club TEXT, pos TEXT,pa INTEGER, co INTEGER, tk INTEGER, ru INTEGER, sh INTEGER, he HEADING, fl INTEGER, st INTEGER, cr INTEGER, fit INTEGER)''')

# Insert multiple records
records = [("Sa", 'Brazil', 30, 'WOLVES', 'GK',8,7,4,5,10,8,8,9,7,100), ("Kilman", 'England', 24, 'WOLVES', 'DEF', 10,9,8,8,8,6,8,7,10,100), ("Bellegarde", 'Spain', 31, 'WOLVES', 'MID', 10,10,8,6,6,6,8,7,10,100), ("Hwang", 'Egypt', 30, 'WOLVES', 'ATT', 8,9,5,10,10,6,10,7,10,100)]
cursor.executemany("INSERT OR IGNORE INTO players (name, nation, age, club, pos, pa, co, tk, ru, sh, he, fl, st, cr, fit) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", records)

# Commit the changes and close the connection
conn.commit()
conn.close()


