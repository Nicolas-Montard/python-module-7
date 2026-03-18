from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    print("\nRegistering Tournament Cards...")
    platform = TournamentPlatform()
    tournamentCard1 = TournamentCard(
        "Fire Dragon", 5, "Legendary", 7, 5, 1200, "dragon_001", 1200)
    tournamentCard2 = TournamentCard("Ice Wizard", 4, "Rare", 3, 4, 1150,
                                     "wizard_001", 1150)
    print(f"\n{platform.register_card(tournamentCard1)}")
    print(f"\n{platform.register_card(tournamentCard2)}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(
        tournamentCard1.id, tournamentCard2.id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for i, card in enumerate(platform.get_leaderboard()):
        print(
            f"{i + 1}. {card.name} - Rating: {card.rating} "
            f"({card.nb_wins}-{card.nb_losses})")

    print(f"\n{platform.generate_tournament_report()}")

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
