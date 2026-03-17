from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.Deck import Deck


class GameEngine:

    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy)\
            -> None:
        self.factory = factory
        self.strategy = strategy
        self.deck: Deck = self.factory.create_themed_deck(10)['deck']
        self.battlefield = [[], [], {'mana': 10}]
        self.battlefield[1].append(self.factory.create_creature())
        self.battlefield[1].append(self.factory.create_creature())
        self.battlefield[1].append(self.factory.create_creature())
        self.battlefield[1].append(CreatureCard("Enemy player", 0, "Unique",
                                                0, 50))
        self.game_report = {'turns_simulated': 0,
                            'strategy_used': self.strategy.get_strategy_name(),
                            'total_damage': 0,
                            'cards_created': 14}

    def simulate_turn(self) -> dict:
        if not isinstance(self.strategy, GameStrategy):
            raise ValueError("You need to configure the engine")
        if not isinstance(self.factory, CardFactory):
            raise ValueError("You need to configure the engine")
        print(f'Strategy: {self.strategy.get_strategy_name()}')
        hand: list[Card] = []
        hand.append(self.deck.draw_card())
        hand.append(self.deck.draw_card())
        hand.append(self.deck.draw_card())
        hand.append(self.deck.draw_card())
        hand.append(self.deck.draw_card())
        hand_state = [card.name for card in hand]
        actions = self.strategy.execute_turn(hand, self.battlefield)
        self.game_report['turns_simulated'] += 1
        self.game_report['total_damage'] += actions['damage_dealt']
        return {'hand': hand_state, 'actions': actions}

    def get_engine_status(self) -> dict:
        return self.game_report
