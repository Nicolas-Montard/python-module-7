from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int, mana: int, spells: list[SpellCard]) -> None:
        super().__init__(name, cost, rarity)
        self.attack_value = attack
        self.health_value = health
        self.mana = mana
        self.spells: list[SpellCard] = spells

    def attack(self, target: CreatureCard) -> dict:
        if not isinstance(target, CreatureCard):
            raise TypeError("the target need to be a creature card")
        if self.attack_value < 0 or target.health < 0:
            raise ValueError("The attack or health cannot be negative")
        target.health -= self.attack_value
        return {'attacker': self.name, 'target': target.name,
                'damage_dealt': self.attack_value, 'combat_type': 'melee'}

    def defend(self, incoming_damage: int) -> dict:
        if self.health_value <= 0:
            raise ValueError("The health cannot be negative")
        if incoming_damage <= 0:
            raise ValueError("The incoming damage cannot be inferior to 1")
        true_damage = incoming_damage - (self.attack_value // 2)
        self.health_value -= true_damage
        if self.health_value < 1:
            still_alive = False
        else:
            still_alive = True
        return {'defender': self.name,
                'damage_taken': true_damage,
                'damage_blocked': self.attack_value // 2,
                'still_alive': still_alive}

    def get_combat_stats(self) -> dict:
        return {'health': self.health_value,
                'attack': self.attack_value}

    def cast_spell(self, spell_name: str, targets: list[CreatureCard]) -> dict:
        spell: SpellCard | None = next((s for s in self.spells
                                        if s.name == spell_name), None)
        if spell is None:
            raise ValueError("This spell do not exist")
        if self.mana < spell.cost:
            raise ValueError(f"{self.name} do not have enought"
                             "mana to cast a spell")
        targets_name = [target.name for target in targets]
        self.mana -= spell.cost
        spell.resolve_effect(targets)
        return {'caster': self.name,
                'spell': spell_name,
                'targets': targets_name,
                'mana_used': spell.cost}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {'channeled': amount,
                'total_mana': self.mana}

    def get_magic_stats(self) -> dict:
        return {'mana': self.mana, 'spells': self.spells}

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
