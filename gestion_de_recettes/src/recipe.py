# Classe Recipe pour représenter une recette avec des attributs de nom, d'ingrédients et d'instructions.
class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return f"Recette: {self.name}\nIngrédients: {', '.join(self.ingredients)}\nInstructions: {self.instructions}"