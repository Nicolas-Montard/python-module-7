

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str, effect_type: str)\
            -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            raise ValueError("There is no 'mana' key in game_state")
        if not isinstance(game_state["mana"], int):
            raise ValueError("The value of mana in game_state is not an int")
        if not self.is_playable(game_state['mana']):
            raise ValueError(f"Not enough mana ({game_state['mana']}) "
                             f"to play {self.name}")
        game_state['mana'] -= self.cost
        if self.effect_type == "damage":
            return {
                "card_played": self.name,
                'mana_used': self.cost,
                'effect': f"Deal {self.cost} damage to target"
            }
        elif self.effect_type == "heal":
            return {
                "card_played": self.name,
                'mana_used': self.cost,
                'effect': f"heal {self.cost} health to target"
            }
        elif self.effect_type == "buff":
            return {
                "card_played": self.name,
                'mana_used': self.cost,
                'effect': f"add {self.cost // 2} attack to target"
            }
        elif self.effect_type == "debuff":
            return {
                "card_played": self.name,
                'mana_used': self.cost,
                'effect': f"remove {self.cost // 2} attack to target"
            }
        return {"card_played": self.name, 'mana_used': self.cost,
                'effect': self.effect_type}

    def resolve_effect(self, targets: list):
        if self.effect_type == "damage":
            for target in targets:
                target.health -= self.cost
            return {
                "effect_type": "damage",
                "targets": targets,
                "damage_dealt": self.cost
            }
        elif self.effect_type == "heal":
            for target in targets:
                target.health += self.cost
            return {
                "effect_type": "heal",
                "targets": targets,
                "health_restored": self.cost
            }
        elif self.effect_type == "buff":
            for target in targets:
                target.attack += self.cost // 2
            return {
                "effect_type": "buff",
                "targets": targets,
                "stat_bonus": f"+{self.cost // 2} attack"
            }
        elif self.effect_type == "debuff":
            for target in targets:
                target.attack -= self.cost // 2
            return {
                "effect_type": "debuff",
                "targets": targets,
                "stat_penalty": f"-{self.cost // 2} attack"
            }
        else:
            return {
                "effect_type": self.effect_type,
                "targets": targets,
            }
