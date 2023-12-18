import sqlite3

# Connect to the database
conn = sqlite3.connect('for_the_win.db')
cursor = conn.cursor()

# Execute the SELECT statement based on the clb variable
clb = "ALVWOL"
cursor.execute("SELECT * FROM players WHERE club = ?", (clb,))

# Fetch all the records into a Python variable
records = cursor.fetchall()

# Close the connection
conn.close()

print(records)