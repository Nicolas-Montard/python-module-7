from ex0.CreatureCard import CreatureCard


def main():
    dragon = CreatureCard("Fire Dragon", 5, "Legendary",  7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common",  2, 1)
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    try:
        print("\nCreatureCard Info:")
        print(dragon.get_card_info())
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    game_state = {'mana': 6}
    try:
        print("\nPlaying Fire Dragon with 6 mana available:")
        print(f"playable: {dragon.is_playable(game_state['mana'])}")
        print(f"Play result: {dragon.play(game_state)}")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    try:
        print("\nFire Dragon attacks Goblin Warrior:")
        print(f"attack result: {dragon.attack_target(goblin)}")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")

    try:
        print(f"\nTesting insufficient mana ({game_state['mana']} available):")
        print(f"Playable: {dragon.is_playable(game_state['mana'])}")
    except (ValueError, TypeError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
