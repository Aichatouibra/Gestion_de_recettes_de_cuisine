from src.recipe import Recipe

# Classe RecipeManager pour gérer l'ajout et la récupération des recettes.
class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, name, ingredients, instructions):
        recipe = Recipe(name, ingredients, instructions)
        self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes