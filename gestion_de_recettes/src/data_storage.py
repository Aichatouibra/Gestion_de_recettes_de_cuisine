# Classe DataStorage pour stocker les données des recettes, avec des méthodes pour sauvegarder et charger les recettes.
class DataStorage:
    def __init__(self):
        self.recipes = []

    def save_recipe(self, recipe):
        self.recipes.append(recipe)

    def load_recipes(self):
        return self.recipes