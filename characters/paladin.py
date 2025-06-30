from .character import Character
import random

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=14)

    def holy_strike(self, opponent):
        damage = self.attack_power + random.randint(-1, 7)
        opponent.health -= damage
        print(f"{self.name} uses Holy Strike for {damage} damage!")

    def smite(self, opponent):
        damage = self.attack_power + random.randint(2, 6)
        opponent.health -= damage
        print(f"{self.name} uses Smite for {damage} damage!")

    def regular_attack(self, opponent):
        self.holy_strike(opponent)

    def special_ability(self, opponent):
        self.smite(opponent)