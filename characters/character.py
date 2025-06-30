import random

# Base class for all characters in the game
class Character:
    def __init__(self, name, health=100, attack_power=10):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = self.attack_power + random.randint(-3, 3)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")


    def display_stats(self):
        print(f"{self.name} ({self.__class__.__name__}) - HP: {self.health}/{self.max_health}, ATK: {self.attack_power}")

    def get_health(self):
        return self.health