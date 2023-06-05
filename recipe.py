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
            print("------------------------------")

# Function to search for recipes by name
def search_recipes():
    keyword = input("Enter a keyword to search for: ")
    query = "SELECT * FROM recipes WHERE name LIKE ?"
    cursor.execute(query, ('%' + keyword + '%',))
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

# Function to update a recipe
def update_recipe():
    recipe_id = int(input("Enter the recipe ID to update: "))
    new_name = input("Enter the new recipe name: ")
    new_ingredients = input("Enter the new ingredients (comma-separated): ")
    new_instructions = input("Enter the new instructions: ")
    new_cooking_time = int(input("Enter the new cooking time (in minutes): "))

    # Update the recipe in the database
    cursor.execute('''UPDATE recipes SET name=?, ingredients=?, instructions=?, cooking_time=?
                      WHERE id=?''', (new_name, new_ingredients, new_instructions, new_cooking_time, recipe_id))
    conn.commit()
    print("Recipe updated successfully!")

# Function to delete a recipe
def delete_recipe():
    recipe_id = int(input("Enter the recipe ID to delete: "))

    # Delete the recipe from the database
    cursor.execute("DELETE FROM recipes WHERE id=?", (recipe_id,))
    conn.commit()
    print("Recipe deleted successfully!")

# Main menu loop
while True:
    print("\n-------- Recipe Management CLI --------")
    print("1. Add a new recipe")
    print("2. Display all recipes")
    print("3. Search for recipes")
    print("4. Update a recipe")
    print("5. Delete a recipe")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_recipe()
    elif choice == "2":
        display_recipes()
    elif choice == "3":
        search_recipes()
    elif choice == "4":
        update_recipe()
    elif choice == "5":
        delete_recipe()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()


