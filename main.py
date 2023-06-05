# main.py

import click
from recipe import RecipeManager

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt='Enter recipe name', help='Name of the recipe')
@click.option('--ingredients', prompt='Enter ingredients (separated by commas)', help='List of ingredients')
@click.option('--instructions', prompt='Enter instructions', help='Recipe instructions')
def add(name, ingredients, instructions):
    """Add a new recipe"""
    RecipeManager.add_recipe(name, ingredients, instructions)
    click.echo('Recipe added successfully.')

@cli.command()
@click.option('--name', prompt='Enter recipe name', help='Name of the recipe')
def view(name):
    """View details of a recipe"""
    recipe = RecipeManager.get_recipe(name)
    if recipe:
        click.echo(f'Recipe: {recipe.name}')
        click.echo(f'Ingredients: {", ".join(recipe.ingredients)}')
        click.echo(f'Instructions: {recipe.instructions}')
    else:
        click.echo('Recipe not found.')

@cli.command()
@click.option('--ingredient', prompt='Enter ingredient', help='Ingredient to search')
def search(ingredient):
    """Search for recipes containing a specific ingredient"""
    recipes = RecipeManager.search_recipes(ingredient)
    if recipes:
        click.echo(f'Recipes containing {ingredient}:')
        for recipe in recipes:
            click.echo(recipe.name)
    else:
        click.echo('No recipes found.')

if __name__ == '__main__':
    cli()

