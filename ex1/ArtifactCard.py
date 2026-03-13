from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            raise ValueError("There is no 'mana' key in game_state")
        if not isinstance(game_state["mana"], int):
            raise ValueError("The value of mana in game_state is not an int")
        if not self.is_playable(game_state['mana']):
            raise ValueError(f"Not enough mana ({game_state['mana']}) "
                             f"to play {self.name}")
        game_state['mana'] -= self.cost
        return {"card_played": self.name, 'mana_used': self.cost,
                'effect': self.effect}

    def activate_ability(self) -> dict:
        self.durability -= 1
        return {
            'effect': self.effect
        }
