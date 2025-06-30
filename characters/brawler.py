from .character import Character
import random

class Brawler(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=18)

    def haymaker(self, opponent):
        damage = self.attack_power + random.randint(-2, 6)
        opponent.health -= damage
        print(f"{self.name} throws a Haymaker for {damage} damage!")

    def flurry(self, opponent):
        damage = self.attack_power + random.randint(1, 5)
        opponent.health -= damage
        print(f"{self.name} uses Flurry for {damage} damage!")

    def regular_attack(self, opponent):
        self.haymaker(opponent)

    def special_ability(self, opponent):
        self.flurry(opponent)