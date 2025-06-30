from .character import Character
import random

class Knight(Character):
    FINAL_ATTACK_CHANCE = 0.1  # Class variable for final attack chance (10%)

    def __init__(self, name):
        super().__init__(name, health=120, attack_power=16)

    def sword_slash(self, opponent):
        damage = self.attack_power + random.randint(2, 6)
        opponent.health -= damage
        print(f"{self.name} uses Sword Slash for {damage} damage!")

    def shield_bash(self, opponent):
        damage = self.attack_power + random.randint(0, 4)
        opponent.health -= damage
        print(f"{self.name} uses Shield Bash for {damage} damage!")

    def final_attack(self, opponent):
        damage = self.attack_power + random.randint(10, 14)
        opponent.health -= damage
        print(f"{self.name} unleashes Holy Lance for {damage} massive damage!")

    def special_ability(self, opponent):
        # 10% chance for final attack, otherwise shield bash
        if random.random() < self.FINAL_ATTACK_CHANCE:
            self.final_attack(opponent)
        else:
            self.sword_slash(opponent)

    def regular_attack(self, opponent):
        # 10% chance for final attack, otherwise sword slash
        if random.random() < self.FINAL_ATTACK_CHANCE:
            self.final_attack(opponent)
        else:
            self.shield_bash(opponent)