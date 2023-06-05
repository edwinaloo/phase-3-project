# recipe_manager.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///recipes.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    instructions = Column(String)
    ingredients = relationship('Ingredient', secondary='recipe_ingredients')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)

class RecipeManager:
    @staticmethod
    def add_recipe(name, ingredients, instructions):
        recipe = Recipe(name=name, instructions=instructions)
        for ingredient_name in ingredients.split(','):
            ingredient = session.query(Ingredient).filter_by(name=ingredient_name.strip()).first()
            if not ingredient:
                ingredient = Ingredient(name=ingredient_name.strip())
            recipe.ingredients.append(ingredient)
        session.add(recipe)
        session.commit()

    @staticmethod
    def get_recipe(name):
        return session.query(Recipe).filter_by(name=name).first()

    @staticmethod
    def search_recipes(ingredient):
        return session.query(Recipe).join(Recipe.ingredients).filter(Ingredient.name == ingredient).all()

