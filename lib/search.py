import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()# Create the search_terms table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS search_terms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    term TEXT
                )''')
conn.commit()# Search section

# Function to search for recipes by name
def search_recipes():
    keyword = input("Enter a keyword to search for: ")
    query = "SELECT * FROM recipes WHERE id IN (SELECT recipe_id FROM search_terms WHERE term LIKE ?)"
    cursor.execute(query, ('%' + keyword.lower() + '%',))
    recipes = cursor.fetchall()

    if len(recipes) == 0:
        print("No recipes found.")
    else:
        for recipe in recipes:
            print("Recipe ID:", recipe[0])
            print("Name:", recipe[1])
            print("Ingredients:", recipe[2])
            print("Instructions:", recipe[3])
            print("Cooking Time:", recipe[4], "minutes")
            print("------------------------------")