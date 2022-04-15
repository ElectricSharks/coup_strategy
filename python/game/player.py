"""
Player Class

    Fields:
        name: string
        coins (initially 3): int
        hidden_influences: list of influences
        revealed_influences: list of influences
        player_strategy: Strategy

    Methods:
        is_alive(): bool
            Returns true if the player has at least one hidden influence.
        reset_player():
        get_player_action(gamestate):
        get_player_counter_action(gamestate):
            Invokes the counter action strategy function with 'self' as the
            countering player.
        lose_influence(gamestate):
            Invoke the influence loss strategy function, to select which
            influence to lose, then remove the first instance of that influence
            from the player's hidden_influences and add it to the player's
            revealed_influences.
        get_player_exchange(gamestate, cards):
            Append the player's hidden influences to the list of cards, then
            invoke the player exchange strategy function, this will return a
            list of cards to keep and a list of cards to return to the deck.
            Then set the player's hidden_influences to the list of cards to keep
            and return the list of cards to return to the deck. 
        satisfies_action_requirement(action): bool
            If the action isn't challengeable return true. If the action is 
            challengeable, return true if an instance of the action's action
            requirement is in the player's hidden influences.
        get_num_influences(): int
            Returns the number of hidden influences the player has.
        get_num_coins(): int
        print_player_state(hidden=False):
            Format and print the players name, their coins and their revealed
            influences. If the hidden tag is set to true, additionally print
            their hidden influences.
        replace_influence(gamestate, influence):
            Draw a card from the deck.
            Then remove the first instance of the influence from the player's
            hidden_influences and return it to the deck.
            Then add the new influence to the player's hidden_influences.
"""