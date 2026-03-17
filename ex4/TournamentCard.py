from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, rating: int, id: str, base_rating: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_value = attack
        self.health = health
        self.nb_wins = 0
        self.nb_losses = 0
        self.rating = rating
        self.id = id
        self.base_rating = base_rating

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            raise ValueError("There is no 'mana' key in game_state")
        if not isinstance(game_state["mana"], int):
            raise ValueError("The value of mana in game_state is not an int")
        if not self.is_playable(game_state['mana']):
            raise ValueError(f"Not enough mana ({game_state['mana']}) "
                             f"to play {self.name}")
        game_state["mana"] -= self.cost
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def attack(self, target: "TournamentCard") -> dict:
        if not isinstance(target, TournamentCard):
            raise TypeError("the target need to be a Tournament card")
        if self.attack_value < 0 or target.health < 0:
            raise ValueError("The attack or health cannot be negative")
        target.health -= self.attack_value
        return {'attacker': self.name, 'target': target.name,
                'damage_dealt': self.attack_value, 'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> dict:
        if self.health <= 0:
            raise ValueError("The health cannot be negative")
        if incoming_damage <= 0:
            raise ValueError("The incoming damage cannot be inferior to 1")
        true_damage = incoming_damage - (self.attack_value // 2)
        self.health -= true_damage
        if self.health < 1:
            still_alive = False
        else:
            still_alive = True
        return {'defender': self.name,
                'damage_taken': true_damage,
                'damage_blocked': self.attack_value // 2,
                'still_alive': still_alive}

    def get_combat_stats(self) -> dict:
        return {'health': self.health,
                'attack': self.attack_value}

    def calculate_rating(self) -> int:
        self.rating = (self.base_rating + (self.nb_wins * 16)) - \
            (self.nb_losses * 16)
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.nb_wins += wins
        self.calculate_rating()

    def update_losses(self, losses: int) -> None:
        self.nb_losses += losses
        self.calculate_rating()

    def get_rank_info(self) -> dict:
        return {
            'rating': self.rating,
            'nb_wins': self.nb_wins,
            'nb_losses': self.nb_losses
        }
