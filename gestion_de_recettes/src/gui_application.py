import tkinter as tk
from tkinter import messagebox
from src.abstract_application import Application
from src.recipe_manager import RecipeManager

# Classe GuiApplication qui hérite de la classe abstraite Application et implémente une interface graphique.
class GuiApplication(Application):
    def __init__(self):
        self.manager = RecipeManager()
        self.root = tk.Tk()

    def start(self):
        self.root.title("Application de Recettes")
        self.run()

    def run(self):
        self.setup_gui()
        self.root.mainloop()

    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.pack()

        self.recipe_name_var = tk.StringVar()
        self.ingredients_var = tk.StringVar()
        self.instructions_var = tk.StringVar()

        tk.Label(frame, text="Nom de la recette:").pack()
        tk.Entry(frame, textvariable=self.recipe_name_var).pack()
        tk.Label(frame, text="Ingrédients (séparés par des virgules):").pack()
        tk.Entry(frame, textvariable=self.ingredients_var).pack()
        tk.Label(frame, text="Instructions:").pack()
        tk.Entry(frame, textvariable=self.instructions_var).pack()

        tk.Button(frame, text="Ajouter", command=self.add_recipe).pack()
        tk.Button(frame, text="Afficher toutes les recettes", command=self.show_recipes).pack()
        tk.Button(frame, text="Quitter", command=self.stop).pack()

    def add_recipe(self):
        name = self.recipe_name_var.get()
        ingredients = self.ingredients_var.get().split(',')
        instructions = self.instructions_var.get()

        if not name or not ingredients or not instructions:
            messagebox.showwarning("Erreur", "Tous les champs doivent être remplis!")
            return

        self.manager.add_recipe(name, [ingredient.strip() for ingredient in ingredients], instructions)
        messagebox.showinfo("Succès", "Recette ajoutée avec succès!")

        # Réinitialiser les champs après l'ajout
        self.recipe_name_var.set("")
        self.ingredients_var.set("")
        self.instructions_var.set("")

    def show_recipes(self):
        recipes = self.manager.get_recipes()
        if not recipes:
            messagebox.showinfo("Recettes", "Aucune recette disponible.")
            return
        recipe_str = "\n\n".join([str(recipe) for recipe in recipes])
        messagebox.showinfo("Recettes", recipe_str)

    def stop(self):
        self.root.quit()