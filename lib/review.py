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

# Main menu loop
while True:
    print("\n-------- Recipe Management CLI --------")
    print("1. Add a new recipe")
    print("2. Display all recipes")
    print("3. Search for recipes")
    print("4. Update a recipe")
    print("5. Delete a recipe")
    print("6. Add a review")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "6":
        add_review()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
