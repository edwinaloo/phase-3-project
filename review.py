import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    ingredients TEXT,
                    instructions TEXT,
                    cooking_time INTEGER
                )''')
conn.commit()