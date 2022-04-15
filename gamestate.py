"""
GameState Class

    Container for the current state of the game.

    Fields:
        - players: list of players
        - action_stack: action stack
        - turn: int
        - deck: list of cards
    
    Methods:
        is_game_over(): bool
        setup_players():
        get_active_player():
        resolve_action_stack():
        print_game_state():
            Iterate through the players, invoking print_state. Print the active
            player's state in red with the hidden tag set to true. Then print
            the action stack's state.
        next_turn():
        get_legal_actions():
            Iterate through all of the actions, checking whether they are legal
            for the active player.
"""
