from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:

    def __init__(self) -> None:
        self.cards: list[TournamentCard] = []
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards.append(card)
        result = f"{card.name} (ID: {card.id})\n" +\
            "- Interfaces: [Card, Combatable, Rankable]" +\
            f"\n- Rating: {card.rating}" +\
            f"\n- Record: {card.nb_wins}-{card.nb_losses}"
        return result

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = None
        card2 = None
        for card in self.cards:
            if card.id == card1_id:
                card1 = card
                break
        for card in self.cards:
            if card.id == card2_id:
                card2 = card
                break
        if card1 is None or card2 is None:
            raise ValueError("This card ID do not exist")
        winner = random.randint(1, 2)
        if winner == 1:
            winner = card1
            loser = card2
        else:
            winner = card2
            loser = card1
        winner.update_wins(1)
        loser.update_losses(1)
        return {'winner': winner.id, 'loser': loser.id,
                'winner_rating': winner.rating, 'loser_rating': loser.rating}

    def get_leaderboard(self) -> list[TournamentCard]:
        cards = sorted(self.cards, key=lambda card: card.rating, reverse=True)
        return cards

    def generate_tournament_report(self) -> dict:
        return {
            'total_cards': len(self.cards),
            'matches_played': self.match_played,
            'avg_rating':
            sum(card.rating for card in self.cards) / len(self.cards),
            'platform_status': 'active'
        }
