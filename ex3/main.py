from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main():
    print("=== DataDeck Game Engine ===")

    print("\nConfiguring Fantasy Card Game...")
    strategy = AggressiveStrategy()
    factory = FantasyCardFactory()
    game_engine = GameEngine()
    try:
        print("Factory: FantasyCardFactory")
        print(f"Strategy: {strategy.get_strategy_name()}")
        print(f"available types: {factory.get_supported_types()}")
        game_engine.configure_engine(factory, strategy)

        print("\nSimulating aggressive turn...")
        turn_result = game_engine.simulate_turn()
        print(f'Hand: {turn_result["hand"]}')

        print('\nTurn execution')
        print(f'Strategy: AgressiveStrategy')
        print(f'Action: {turn_result["actions"]}')

        print('\nGame report:')
        print(game_engine.get_engine_status())
    except Exception as error:
        print(f"Error: {error}")

    print('\nAbstract Factory + Strategy Pattern: '
          'Maximum flexibility achieved!')


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
