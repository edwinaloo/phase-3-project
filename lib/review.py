import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Create the reviews table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    recipe_id INTEGER,
                    rating INTEGER,
                    comment TEXT
                )''')
conn.commit()

# Review section

# Function to add a review for a recipe
def add_review():
    recipe_id = int(input("Enter the recipe ID to add a review for: "))
    rating = int(input("Enter the rating (1-5): "))
    comment = input("Enter your comment: ")

    # Insert the review into the reviews table
    cursor.execute('''INSERT INTO reviews (recipe_id, rating, comment)
                      VALUES (?, ?, ?)''', (recipe_id, rating, comment))
    conn.commit()
    print("Review added successfully!")

