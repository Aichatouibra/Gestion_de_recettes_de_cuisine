from abc import ABC, abstractmethod

# Classe abstraite Application, servant de point d'entrée pour les différentes versions de l'application.
class Application(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass