from abc import abstractmethod, ABC


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        super().__init__()
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self.cost:
            return True
        return False
