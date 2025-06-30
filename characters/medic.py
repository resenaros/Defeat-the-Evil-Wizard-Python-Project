from .character import Character
import random

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, health=95, attack_power=10)

    def heal_ally(self, ally):
        amount = random.randint(18, 25)
        heal_amt = min(amount, ally.max_health - ally.health)
        ally.health += heal_amt
        print(f"{self.name} heals {ally.name} for {heal_amt} HP! ({ally.health}/{ally.max_health} HP)")

    def regular_attack(self, opponent, party):
        damage = self.attack_power + random.randint(-2, 2)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

        # Redistribute half the damage as healing to lowest HP ally (including self)
        living = [p for p in party if p.health > 0]
        if living:
            lowest = min(living, key=lambda p: p.health)  # Lambda version
            heal_amt = damage // 2  # Integer division for half
            heal_amt = min(heal_amt, lowest.max_health - lowest.health)
            lowest.health += heal_amt
            print(f"{self.name} redistributes {heal_amt} HP to {lowest.name} ({lowest.health}/{lowest.max_health} HP)")

    def special_ability(self, party):
        # Heals lowest health ally (including self)
        living = [p for p in party if p.health > 0]
        if living:
            # Use get_health method directly, no lambda
            lowest = min(living, key=type(living[0]).get_health)
            self.heal_ally(lowest)