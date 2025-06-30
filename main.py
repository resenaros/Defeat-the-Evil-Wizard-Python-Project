from characters.character_factory import CharacterFactory
from characters.evil_wizard import EvilWizard
from battle import battle
import random

def player_character_selection(factory):
    """
    Ask the user to choose a character class and a name.
    Returns the chosen class name (string) and the created character object.
    """
    print("\nYou have arrived at Dante's inferno!")
    print("Welcome to the Final Battle!\n")

    # Get the list of available character class names
    class_names = factory.get_class_names()
    print("Choose your character class from the options below:")
    for number, class_name in enumerate(class_names, start=1):
        print(f"{number}. {class_name.capitalize()}")

    # Let the user select a class by number, ensure valid input
    while True:
        class_input = input("Enter the number of your class choice (1-6): ").strip()
        if class_input.isdigit():
            choice_number = int(class_input)
            if 1 <= choice_number <= len(class_names):
                chosen_class = class_names[choice_number - 1]
                break
        print("Invalid choice. Please enter a number between 1 and 6.")

    # Get the two example names for this class
    example_name_1, example_name_2 = factory.get_example_names(chosen_class)
    print(f"\nChoose your character's name:")
    print(f"1. {example_name_1}")
    print(f"2. {example_name_2}")
    print("3. Enter a custom name")

    # Let the user select a name or type a custom one
    while True:
        name_choice = input("Choose 1, 2, or 3: ").strip()
        if name_choice == '1':
            chosen_name = example_name_1
            break
        elif name_choice == '2':
            chosen_name = example_name_2
            break
        elif name_choice == '3':
            chosen_name = input("Enter your custom name: ").strip()
            if chosen_name:
                break
            print("Name cannot be empty.")
        else:
            print("Invalid choice. Try again.")

    # Create the character object
    player_character = factory.create(chosen_class, chosen_name)
    return chosen_class, player_character

def build_party(factory):
    """
    Build the party of three characters: the user and two randomly chosen teammates.
    Returns a list of three character objects.
    """
    # Get the player's character first
    player_class, player_character = player_character_selection(factory)
    all_class_names = factory.get_class_names()
    # Remove the chosen class from the list
    teammate_class_names = []
    for class_name in all_class_names:
        if class_name != player_class:
            teammate_class_names.append(class_name)
    # Randomly pick two different classes for teammates
    teammate_classes = random.sample(teammate_class_names, 2)
    # Create the teammate character objects (using example name 2 for variety)
    teammate_1 = factory.create_with_example_name(teammate_classes[0], which=1)
    teammate_2 = factory.create_with_example_name(teammate_classes[1], which=1)
    # Return the full party as a list
    return [player_character, teammate_1, teammate_2]

def main():
    """
    Main entry point: builds the party, introduces the party, creates the wizard,
    and starts the battle.
    """
    factory = CharacterFactory()
    party = build_party(factory)
    print("\nYour party members are:")
    for character in party:
        print(f"- {character.name} the {character.__class__.__name__}")
    evil_wizard = EvilWizard("Dante")
    battle(party, evil_wizard)

if __name__ == "__main__":
    main()