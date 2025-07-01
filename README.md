# Turn-Based RPG Battle System

This is a Python-based turn-based RPG (role-playing game) battle module. It allows you to create a party of heroes (such as Medics, Knights, etc.) and battle against an enemy wizard in a console-based interface. The system supports both player-controlled and AI-controlled characters, with unique abilities and attack logic for different classes.

## Features

- **Turn-based battle system**: Heroes and enemies take turns attacking or using special abilities.
- **Player and AI characters**: The player controls their character while allies act automatically.
- **Custom character classes**: Includes classes like `Knight, Medic, and Archer`, each with unique abilities (e.g., healing allies).
- **Battle logic**: Damage, healing, and targeting are managed dynamically each turn.
- **Console interface**: Player chooses actions via simple text menus.

## Getting Started

### File Structure

```
characters/
    archer.py              # Archer character class
    brawler.py             # Brawler character class
    character_factory.py   # Factory for creating character instances
    character.py           # Base class for all characters
    evil_wizard.py         # EvilWizard (enemy) class
    knight.py              # Knight character class
    medic.py               # Medic character class
    paladin.py             # Paladin character class
    vanguard.py            # Vanguard character class
battle.py                 # Main battle system/loop and logic
main.py                   # Entry point for th
```

- Each character class (`archer.py`, `brawler.py`, etc.) defines a unique hero type with its own abilities.
- `character.py` provides the base class that all heroes inherit from.
- `character_factory.py` simplifies the process of creating character instances.
- `evil_wizard.py` defines the main enemy class.
- `battle.py` contains the main battle loop and mechanics.
- `main.py` is the entry point, handling user interaction and game setup.

### Running the Game

1. Clone or download the repository.
2. Ensure your directory structure matches the example above.
3. Run the main script:
   ```bash
   python main.py
   ```

Follow the on-screen prompts to control your party and battle the evil wizard!

## Example Usage

When you run the game, you’ll see options each turn, such as:

```
Your turn: Robin the Medic
1. Attack
2. Use Special Ability
Choose an action:
```

Allies will act automatically, and the wizard will attack after your party’s turn.

## Customization

- Add new character classes by creating new files in the `characters/` directory and inheriting from the `Character` base class.
- Modify or expand abilities and logic as desired.
- Adjust stats, enemy types, and game flow to suit your needs.
