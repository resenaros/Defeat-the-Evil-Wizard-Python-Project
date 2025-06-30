from .paladin import Paladin
from .knight import Knight
from .vanguard import Vanguard
from .medic import Medic
from .archer import Archer
from .brawler import Brawler

class CharacterFactory:
    """
    A helper class for creating different character types and providing example names.
    """
    def __init__(self):
        # Store each class type with two example names
        self.character_types = {
            'knight':    {'class': Knight,   'names': ['Longinus', 'Richard']},
            'medic':     {'class': Medic,    'names': ['Matthias', 'Luce']},
            'archer':    {'class': Archer,   'names': ['Belmont', 'Robin']},
            'paladin':   {'class': Paladin,  'names': ['Baldwin', 'Genevieve']},
            'vanguard':  {'class': Vanguard, 'names': ['Godfrey', 'Joan']},
            'brawler':   {'class': Brawler,  'names': ['Ezekiel', 'Dominic']}
        }

    def get_class_names(self):
        """
        Return a list of all available character class names.
        """
        return list(self.character_types.keys())

    def get_example_names(self, class_name):
        """
        Return the two example names for the chosen class.
        """
        return self.character_types[class_name]['names']

    def create(self, class_name, name):
        """
        Create a character of the specified class with the given name.
        """
        class_constructor = self.character_types[class_name]['class']
        return class_constructor(name)

    def create_with_example_name(self, class_name, which=0):
        """
        Create a character using one of the two example names (0 = first, 1 = second).
        """
        example_names = self.character_types[class_name]['names']
        chosen_name = example_names[which]
        return self.create(class_name, chosen_name)