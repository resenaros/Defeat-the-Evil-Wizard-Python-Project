import random
from characters.medic import Medic

def display_all_stats(party, wizard, turn=None):
    # Only show stats at the start of each turn, with turn number
    if turn is not None:
        print(f"\n--- Turn {turn} ---")
    print("\n--- Party Stats ---")
    for member in party:
        member.display_stats()
    print("\n--- Enemy Stats ---")
    wizard.display_stats()

def player_action_menu(player, wizard, party):
    while True:
        print(f"\nYour turn: {player.name} the {player.__class__.__name__}")
        print("1. Attack")
        print("2. Use Special Ability")
        # Heal and View Stats removed from menu
        choice = input("Choose an action: ").strip()
        if choice == '1':
            if hasattr(player, "regular_attack"):
                if isinstance(player, Medic):
                    player.regular_attack(wizard, party)
                else:
                    player.regular_attack(wizard)
            else:
                player.attack(wizard)
            break
        elif choice == '2':
            if hasattr(player, "special_ability"):
                if isinstance(player, Medic):
                    player.special_ability(party)
                else:
                    player.special_ability(wizard)
            else:
                player.attack(wizard)
            break
        else:
            print("Invalid choice. Try again.")

def auto_party_action(player, wizard, party):
    if player.health <= 0:
        return
    roll = random.random()
    if hasattr(player, "special_ability") and roll < 0.2:
        if isinstance(player, Medic):
            player.special_ability(party)
        else:
            player.special_ability(wizard)
    else:
        if hasattr(player, "regular_attack"):
            if isinstance(player, Medic):
                player.regular_attack(wizard, party)
            else:
                player.regular_attack(wizard)
        else:
            player.attack(wizard)

def battle(party, wizard):
    turn = 1
    print("\nDante the Evil Wizard: I have given you enough time to prepare!\nDante has stepped up and off his throne and is ready for battle!\nThe battle begins!")
    player = party[0]  # User's character
    while wizard.health > 0 and any(p.health > 0 for p in party):
        # Show stats with turn number at top of each turn, only ONCE
        display_all_stats(party, wizard, turn=turn)
        # No display_team here, so stats are not repeated

        for idx, member in enumerate(party):
            if member.health <= 0:
                continue
            if idx == 0:
                player_action_menu(member, wizard, party)
            else:
                print(f"\n{member.name}'s turn (auto):")
                auto_party_action(member, wizard, party)
            if wizard.health <= 0:
                print(f"\n🎉 {member.name} has defeated the evil wizard! Your team has vanquished the accuser!")
                display_all_stats(party, wizard)
                return

        # Wizard's turn
        wizard.regenerate()
        living_party = [p for p in party if p.health > 0]
        if living_party:
            target = random.choice(living_party)
            print(f"\n{wizard.name} targets {target.name}!")
            wizard.wizard_attack(target)
            if target.health <= 0:
                print(f"💀 {target.name} has been defeated!")

        # No display_all_stats here (so stats are only shown ONCE per turn)

        if all(p.health <= 0 for p in party):
            print(f"\n💀 All party members have been defeated by {wizard.name}. Evil prevails!")
            display_all_stats(party, wizard)
            return

        turn += 1

    if wizard.health <= 0:
        print(f"\n🎉 The party has defeated the evil wizard! Victory is yours!")
        display_all_stats(party, wizard)
    else:
        print(f"\n💀 All party members have been defeated by {wizard.name}. Evil prevails!")
        display_all_stats(party, wizard)