from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
import random


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures: list[str] = ["Fire Dragon", "Goblin Warrior",
                                     "Ice wizard"]
        self.spells: list[str] = ["Lightning Bolt", "Healing Potion",
                                  "Fireball"]
        self.artifacts: list[str] = ["Mana Crystal", "Sword of Power",
                                     "Ring of Wisdom"]

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = random.choice(self.creatures)
        if name_or_power == "Fire Dragon" or name_or_power == 5:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 3)
        if name_or_power == "Goblin Warrior" or name_or_power == 2:
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)
        if name_or_power == "Ice Wizard" or name_or_power == 4:
            return CreatureCard("Ice Wizard", 4, "Rare", 3, 4)
        raise ValueError("There is no corresponding creature")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = random.choice(self.spells)
        if name_or_power == "Lightning Bolt" or name_or_power == 3:
            return SpellCard("Lightning Bolt", 3, "Common", "damage")
        if name_or_power == "Healing Potion" or name_or_power == 2:
            return SpellCard("Healing Potion", 2, "Common", "heal")
        if name_or_power == "Fireball" or name_or_power == 4:
            return SpellCard("Fireball", 4, "Uncommon", "damage")
        raise ValueError("There is no corresponding spell")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power is None:
            name_or_power = random.choice(self.artifacts)
        if name_or_power == "Mana Crystal" or name_or_power == 2:
            return ArtifactCard("Mana Crystal", 2, "Common", 5,
                                "Permanent: +1 mana per turn")
        if name_or_power == "Sword of Power" or name_or_power == 3:
            return ArtifactCard("Sword of Power", 3, "Uncommon", 3,
                                "Permanent: +2 attack to equipped creature")
        if name_or_power == "Ring of Wisdom" or name_or_power == 4:
            return ArtifactCard("Ring of Wisdom", 4, "Rare", 4,
                                "Permanent: Draw an extra card each turn")
        raise ValueError("There is no corresponding artifact")

    def create_themed_deck(self, size: int) -> dict:
        i = 0
        deck = Deck()
        while i < size:
            type = random.randrange(0, 4)
            if type == 1:
                deck.add_card(self.create_creature())
            if type == 2:
                deck.add_card(self.create_spell())
            if type == 3:
                deck.add_card(self.create_artifact())
            i += 1
        return {
            "deck": deck,
            "size": size,
            "theme": "Fantasy"
        }

    def get_supported_types(self) -> dict:
        return {'creatures': self.creatures,
                'spells': self.spells,
                'artifacts': self.artifacts}
