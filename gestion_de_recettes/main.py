# main.py

from src.terminal_application import TerminalApplication
from src.gui_application import GuiApplication

# Fonction principale pour démarrer l'application et choisir entre l'interface terminal ou graphique.
def main():
    print("Choisissez le mode de l'application :")
    print("1. Terminal")
    print("2. Interface Graphique")
    choice = int(input("Votre choix: "))

    # Utilisation de match case pour remplacer les if else
    match choice:
        case 1:
            app = TerminalApplication()
        case 2:
            app = GuiApplication()
        case _:
            print("Choix invalide!")
            return

    app.start()

# Main Guard pour s'assurer que la fonction main est appelée uniquement lorsque le script est exécuté directement.
if __name__ == "__main__":
    main()
