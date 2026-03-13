from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


def main():
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck = Deck()
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Common", 5,
                               "Permanent: +1 mana per turn"))
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    print(deck.get_deck_stats())

    game_state = {'mana': 1000}

    print("\nDrawing and playing cards:")
    for i in range(len(deck.cards)):
        try:
            card = deck.draw_card()
            print(f"\nDrew: {card.name}")
            print(f"Play result: {card.play(game_state)}")
        except Exception as error:
            print(f"Error: {error}")

    print("\nPolymorphism in action: Same interface, "
          "different card behaviors!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
