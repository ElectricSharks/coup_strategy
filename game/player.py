"""
Player Class

    Fields:
        name: string
        coins: int
        hidden_influences: list of influences
        revealed_influences: list of influences
        player_strategy: Strategy
            Which should implement the following methods:
                action_strategy(gamestate):
                counter_action_strategy(gamestate):
                influence_loss_strategy(gamestate):
                exchange_strategy(gamestate):

    Methods:
        is_alive(): bool
        reset_player():
        get_player_action(gamestate):
        get_player_counter_action(gamestate):
        lose_influence(gamestate):
        lose_both_influences():
        get_player_exchange(gamestate, cards):
        satisfy_action_requirement(action): bool
        get_num_influences(): int
            Returns the number of hidden influences the player has.
        get_num_coins(): int
        print_player_state(hidden=False):
            Format and print the players name, their coins and their revealed
            influences. If the hidden tag is set to true, additionally print
            their hidden influences.
"""