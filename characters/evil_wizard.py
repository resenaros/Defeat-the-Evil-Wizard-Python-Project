from .character import Character
import random

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=500, attack_power=22)

    def dark_bolt(self, opponent):
        damage = self.attack_power + random.randint(-4, 6)
        opponent.health -= damage
        print(f"{self.name} casts Dark Bolt for {damage} damage!")

    def infernal_blast(self, opponent):
        damage = self.attack_power + random.randint(0, 8)
        opponent.health -= damage
        print(f"{self.name} unleashes Infernal Blast for {damage} damage!")

    def soul_leech(self, opponent):
        damage = self.attack_power + random.randint(-2, 4)
        opponent.health -= damage
        self.health = min(self.max_health, self.health + (damage // 2))
        print(f"{self.name} uses Soul Leech for {damage} damage and heals for {damage // 2}!")

    def wizard_attack(self, opponent):
        move = random.choice([self.dark_bolt, self.infernal_blast, self.soul_leech])
        move(opponent)

    def regenerate(self):
        regen = random.randint(8, 18)
        self.health = min(self.max_health, self.health + regen)
        print(f"{self.name} regenerates {regen} health! ({self.health}/{self.max_health} HP)")