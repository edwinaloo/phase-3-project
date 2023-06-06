import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('recipes.db')
cursor = conn.cursor()

# Create the recipes table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    ingredients TEXT,
                    instructions TEXT,
                    cooking_time INTEGER
                )''')
conn.commit()

# Function to add a new recipe
def add_recipe():
    name = input("Enter the recipe name: ")
    ingredients = input("Enter the ingredients (comma-separated): ")
    instructions = input("Enter the instructions: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))

    # Insert the recipe into the database
    cursor.execute('''INSERT INTO recipes (name, ingredients, instructions, cooking_time)
                      VALUES (?, ?, ?, ?)''', (name, ingredients, instructions, cooking_time))
    conn.commit()
    print("Recipe added successfully!")

# Function to display all recipes
def display_recipes():
    cursor.execute("SELECT * FROM recipes")
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
            print("------------------------------")# Close the database connection
conn.close()