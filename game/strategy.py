"""
Honest Strategy Class
    Methods:
        action_strategy:
            Inputs:
                - gamestate: GameState
            Outputs:
                - action: Action

            Description:
                Find the active player, if they have enough coins to use the
                Coup action return the Coup action with the target being the
                player with the most remaining influences (if there is a tie,
                choose the player with the most coins, if there is still a tie,
                choose randomly).
                
                If they don't have enough coins to use the Coup action, but they
                do have the Duke card use the Tax action.

                If they don't have the Duke card, return the Income action.

        counter_action_strategy:
            Inputs:
                - gamestate: GameState
                - countering_player: Player
            Outputs:
                - action: Action or None
            
            Description:
                The honest strategy class always returns None for this action.
        
        influence_loss_strategy:
            Inputs:
                - gamestate: GameState
                - target_player : Player
            Outputs:
                - action: Influence
            
            Description:
                The target player returns a random influence from their hidden
                influences, unless they have a single Duke card in their hidden,
                influences in which case they return the other card.
        
        player_exchange_strategy:
            Inputs:
                - gamestate: GameState
                - influence_cards: list of cards
            Outputs:
                - cards_to_keep: list of cards to keep
                - cards_to_return: list of cards to return to the deck

            Description:
                Selects two cards at random from the list of influence cards,
                returns these two cards in a new list of cards_to_return, and
                returns the remaining influence cards as the cards to keep.

        _get_coup_target:
            Inputs:
                - gamestate: Gamestate
            Outputs:
                - target_player: Player
            
            Description:
                Iterates through the players in the gamestate, excluding the
                active player, and finds the player with the most influences, in
                the case of a tie, the player with the most coins is chosen, if
                there is still a tie a random choice between the tied players is
                made.
"""


"""
Manual Input Strategy Class
    Methods:
        action_strategy:
            Inputs:
                - gamestate: GameState
            Outputs:
                - action: Action

            Description:
                Print the game state, then get a list of legal actions and ask
                the user to choose one. Return the chosen action.

        counter_action_strategy:
            Inputs:
                - gamestate: GameState
                - countering_player: Player
            Outputs:
                - action: Action or None
            
            Description:
                Print the game state then get a list of legal actions and ask
                the user to choose one. Return the chosen action.
        
        influence_loss_strategy:
            Inputs:
                - gamestate: GameState
                - target_player : Player
            Outputs:
                - action: Influence
            
            Description:
                Print the game state, then if the user has more than one hidden
                influence ask them to choose one. Return the chosen influence.
                If the user has only one hidden influence, return it.
        
        player_exchange_strategy:
            Inputs:
                - gamestate: GameState
                - influence_cards: list of cards
            Outputs:
                - cards_to_keep: list of cards to keep
                - cards_to_return: list of cards to return to the deck

            Description:
                Print the game state, then print the influence cards and ask the
                user to choose two of them. Return the chosen cards as the cards to return
                and the unchosen card/(s) as cards to keep.
"""