from abc import ABC,abstractmethod

class Entity(ABC):
    def __init__(self, name):
        self.name = name

        @abstractmethod
        def __str__(sel):
            pass

#Base Class character
class Character:
    def __init__(self, name, health, strength, defense):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense

    @abstractmethod
    def attack(self):
        pass

