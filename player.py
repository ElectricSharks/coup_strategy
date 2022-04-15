"""
Player Class

    Fields:
        name: string
        coins: int
        hidden_cards: list of cards
        revealed_cards: list of cards
        player_action_strategy: strategy_fn
        player_counter_action_strategy: strategy_fn
        player_challenge_strategy: strategy_fn
        player_influence_loss_strategy: strategy_fn
        player_exchange_strategy: strategy_fn

    Methods:
        is_alive(): bool
        reset_player():
        get_player_action(gamestate):
        get_player_counter_action(gamestate):
        lose_influence(gamestate):
        lose_both_influences():
        get_player_exchange(gamestate, cards):
        satisfy_action_requirement(action): bool
"""