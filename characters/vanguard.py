from .character import Character
import random

class Vanguard(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=13)

    def spear_thrust(self, opponent):
        damage = self.attack_power + random.randint(0, 6)
        opponent.health -= damage
        print(f"{self.name} uses Spear Thrust for {damage} damage!")

    def heavy_swing(self, opponent):
        damage = self.attack_power + random.randint(3, 8)
        opponent.health -= damage
        print(f"{self.name} uses Heavy Swing for {damage} damage!")

    def regular_attack(self, opponent):
        self.spear_thrust(opponent)

    def special_ability(self, opponent):
        self.heavy_swing(opponent)