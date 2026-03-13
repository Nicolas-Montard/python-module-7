from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info['type'] = 'Creature'
        card_info['attack'] = 7
        card_info['health'] = 5
        return card_info

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

    def attack_target(self, target: "CreatureCard") -> dict:
        if not isinstance(target, CreatureCard):
            raise TypeError("the target need to be a creature card")
        if self.attack < 0 or target.health < 0:
            raise ValueError("The attack or health cannot be negative")
        target.health -= self.attack
        return {'attacker': self.name, 'target': target.name,
                'damage_dealt': self.attack, 'combat_resolved': True}
