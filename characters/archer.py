from .character import Character
import random

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=85, attack_power=15)

    def quick_shot(self, opponent):
        damage = self.attack_power + random.randint(-2, 5)
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot for {damage} damage!")

    def double_arrow(self, opponent):
        total_damage = 0
        for i in range(2):
            damage = self.attack_power + random.randint(0, 3)
            opponent.health -= damage
            total_damage += damage
            print(f"{self.name} fires Double Arrow shot {i+1} for {damage} damage!")
        print(f"{self.name} dealt a total of {total_damage} damage with Double Arrow!")

    def regular_attack(self, opponent):
        self.quick_shot(opponent)

    def special_ability(self, opponent):
        self.double_arrow(opponent)