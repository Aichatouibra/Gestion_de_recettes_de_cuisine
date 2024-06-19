import os
import sys
from src.abstract_application import Application
from src.recipe_manager import RecipeManager

# Classe TerminalApplication qui hérite de la classe abstraite Application et implémente une interface en ligne de commande.
class TerminalApplication(Application):
    def __init__(self):
        self.manager = RecipeManager()

    def start(self):
        self.app_initialize()
        self.app_launch()
        self.run()

    def app_initialize(self):
        # Nettoyage du terminal (fonctionne sur Windows)
        os.system('cls' if os.name == 'nt' else 'clear')

    def app_launch(self):
        print("Bienvenue dans l'application de gestion des recettes")

    def run(self):
        while True:
            self.app_menu()

    def app_menu(self):
        print("\nMenu Principal")
        print("1) Ajouter une recette")
        print("2) Afficher toutes les recettes")
        print("3) Quitter")

        user_choice = int(input("Choisissez une option: "))

        # Utilisation de match case pour remplacer les if else
        match user_choice:
            case 1:
                self.add_recipe()
            case 2:
                self.show_recipes()
            case 3:
                self.stop()
            case _:
                print("Option invalide!")

    def add_recipe(self):
        name = input("Nom de la recette: ")
        ingredients = input("Ingrédients (séparés par des virgules): ").split(',')
        instructions = input("Instructions: ")
        self.manager.add_recipe(name, [ingredient.strip() for ingredient in ingredients], instructions)
        print("Recette ajoutée avec succès!")

    def show_recipes(self):
        recipes = self.manager.get_recipes()
        if not recipes:
            print("Aucune recette disponible.")
        else:
            for recipe in recipes:
                print(recipe)

    def stop(self):
        print("Arrêt de l'application de terminal...")
        sys.exit()