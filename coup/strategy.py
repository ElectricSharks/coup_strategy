from coup.influence import *
from coup.action import *
from random import choice, choices

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

        counteraction_strategy:
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
                influences, unless they have a single Duke card in their hidden
                influences in which case they return the other card.
        
        player_exchange_strategy:
            Inputs:
                - gamestate: GameState
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


class HonestStrategy:
    def action_strategy(self, gamestate):
        active_player = gamestate.get_active_player()
        if active_player.coins >= 7:
            target_player = self._get_coup_target(gamestate)
            return Coup(active_player, target_player)
        elif active_player.satisfies_action_requirement(Tax):
            return Tax(active_player)
        else:
            return Income(active_player)

    def counteraction_strategy(self, gamestate, countering_player):
        return None

    def influence_loss_strategy(self, gamestate, target_player):
        """
        The target player returns a random influence from their hidden
        influences, unless they have a single Duke card in their hidden
        influences in which case they return the other card.
        """
        if len(target_player.hidden_influences) == 1:
            return target_player.hidden_influences[0]
        if self._has_single_duke(target_player):
            for influence in target_player.hidden_influences:
                if not isinstance(influence, Duke):
                    return influence
        return choice(target_player.hidden_influences)

    def player_exchange_strategy(self, gamestate):
        """
        Selects two cards at random from the list of influence cards, returns
        these two cards in a new list of cards_to_return, and returns the
        remaining influence cards as the cards to keep.
        """
        cards_to_keep = []
        cards_to_return = []
        player = gamestate.get_active_player()
        for _ in range(2):
            card_to_return = choice(player.hidden_influences)
            cards_to_return.append(card_to_return)
            player.hidden_influences.remove(card_to_return)
        for card in player.hidden_influences:
            cards_to_keep.append(card)
        return cards_to_keep, cards_to_return

    def _get_coup_target(self, gamestate):
        """
        Iterates through the players in the gamestate, excluding the
        active player, and finds the player with the most hidden influences, in
        the case of a tie, the player with the most coins is chosen, if
        there is still a tie a random choice between the tied players is
        made.
        """
        active_player = gamestate.get_active_player()
        max_influences = max(
            player.get_num_influences()
            for player in gamestate.players
            if player != active_player
        )
        max_influence_players = [
            player
            for player in gamestate.players
            if player != active_player and player.get_num_influences() == max_influences
        ]
        max_coins = max(player.coins for player in max_influence_players)
        max_coin_players = [
            player for player in max_influence_players if player.coins == max_coins
        ]
        return choice(max_coin_players)

    def _has_single_duke(self, player):
        """
        Returns true if one and only one of the player's hidden influences is a
        Duke.
        """
        dukes = 0
        for influence in player.hidden_influences:
            if isinstance(influence, Duke):
                dukes += 1
        return dukes == 1


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

        counteraction_strategy:
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
            Outputs:
                - cards_to_keep: list of cards to keep
                - cards_to_return: list of cards to return to the deck

            Description:
                Print the game state, then print the influence cards and ask the
                user to choose two of them. Return the chosen cards as the cards to return
                and the unchosen card/(s) as cards to keep.
"""


class ManualInputStrategy:
    def action_strategy(self, gamestate):
        active_player = gamestate.get_active_player()
        gamestate.print_game_state(active_player)
        legal_actions = [
            action for action in gamestate.get_legal_actions(active_player)
        ]
        # Get the user's choice
        return self._get_user_choice(legal_actions, message="Choose an action: ")

    def counteraction_strategy(self, gamestate, countering_player):
        gamestate.print_game_state(countering_player)
        legal_actions = [
            action for action in gamestate.get_legal_actions(countering_player)
        ]
        legal_actions.append(None)
        # Get the user's choice
        return self._get_user_choice(
            legal_actions, message="Would you like to make a counteraction:"
        )

    def influence_loss_strategy(self, gamestate, target_player):
        gamestate.print_game_state(target_player)
        if len(target_player.hidden_influences) > 1:
            # Get the user's choice
            return self._get_user_choice(
                target_player.hidden_influences, message="Choose an influence to lose: "
            )
        else:
            return target_player.hidden_influences[0]

    def player_exchange_strategy(self, gamestate):
        gamestate.print_game_state()
        active_player = gamestate.get_active_player()
        # Get the user's choice
        print("Choose two of your influence cards to return to the deck.")
        first_card = self._get_user_choice(
            active_player.hidden_influences, message="First influnce card to return."
        )
        second_card = self._get_user_choice(
            active_player.hidden_influences, message="Second influence card to return."
        )
        return [first_card, second_card], [
            card
            for card in active_player.hidden_influences
            if card not in [first_card, second_card]
        ]

    def _get_user_choice(self, options, message="Choose an option:"):
        print(message)
        for i, option in enumerate(options):
            print(f"{i}: {option}")
        choice = None
        while choice not in {i for i in range(len(options))}:
            choice = int(input("Enter the index of your choice: "))

        # Return the chosen option
        return options[choice]
