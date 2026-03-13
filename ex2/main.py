from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===")

    print("\nEliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print("\nPlaying Arcane Warrior (Elite Card):")
    spells = []
    spells.append(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    spells.append(SpellCard("Meteor", 8, "Legendary", "damage"))
    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 10)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
    elite_card = EliteCard("Stone Golem", 6, "Rare", 5, 8, 9, spells)
    game_state = {'mana': 10}
    try:
        elite_card.play(game_state)
    except ValueError as error:
        print(f"Error: {error}")

    print("\nCombat phase:")
    try:
        print(f"Attack result: {elite_card.attack(dragon)}")
        print(f"Defense result: {elite_card.defend(5)}")
    except Exception as error:
        print(f"Error: {error}")

    print("\nMagic phase:")
    try:
        print(f"Spell cast: "
              f"{elite_card.cast_spell('Lightning Bolt', [dragon, goblin])}")
        print(f"Mana channel: {elite_card.channel_mana(3)}")
    except Exception as error:
        print(f"Error: {error}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
