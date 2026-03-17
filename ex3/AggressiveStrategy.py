from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list[Card], battlefield: list)\
            -> dict:
        target_attacked = set()
        card_played = []
        total_damage = 0
        mana_used = 0
        ally_creatures: list[CreatureCard] = battlefield[0]
        enemy_creatures: list[CreatureCard] = battlefield[1]

        can_play = True
        sorted(hand, key=lambda card: card.cost)
        while can_play is True:
            can_play = False
            hand = sorted(hand, key=lambda card: card.cost)
            for card in hand:
                if card.cost <= battlefield[2]['mana']:
                    if isinstance(card, SpellCard):
                        if card.effect_type == "damage":
                            card_played.append(card.name)
                            mana_used += card.cost
                            targets = self.prioritize_targets(enemy_creatures)
                            targets_name = [target.name for target in targets]
                            card.play(battlefield[2])
                            card.resolve_effect(targets)
                            total_damage += card.cost * len(targets)
                            can_play = True
                            target_attacked.update(targets_name)
                            hand.remove(card)
                    if isinstance(card, CreatureCard):
                        card.play(battlefield[2])
                        mana_used += card.cost
                        card_played.append(card.name)
                        ally_creatures.append(card)
                        can_play = True
                        hand.remove(card)

        for creature in ally_creatures:
            targets: list[CreatureCard] = self.prioritize_targets(
                enemy_creatures)
            attack_stat = creature.attack_target(targets[0])
            total_damage += attack_stat['damage_dealt']
            target_attacked.add(targets[0].name)

        return {'cards_played': card_played,
                'mana_used': mana_used,
                'targets_attacked': target_attacked,
                'damage_dealt': total_damage}

    def get_strategy_name(self) -> str:
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list[CreatureCard])\
            -> list[CreatureCard]:
        targets = sorted(available_targets, key=lambda card: card.health)
        targets = [target for target in targets if target.health > 0]
        return targets
