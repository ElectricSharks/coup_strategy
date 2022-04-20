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
        get_action(gamestate):
        get_counteraction(gamestate):
            Invokes the counteraction strategy function with 'self' as the
            countering player.
        lose_influence(gamestate):
            Invoke the influence loss strategy function, to select which
            influence to lose, then remove the first instance of that influence
            from the player's hidden_influences and add it to the player's
            revealed_influences.
        get_exchange(gamestate, cards):
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
        pay_cost(cost):
            Subtract the number of coins from the player's coins, then return
            True, if the player has fewer coins than the cost, return False.
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


class Player:
    def __init__(self, name, strategy):
        self.name = name
        self.coins = 3
        self.hidden_influences = []
        self.revealed_influences = []
        self.player_strategy = strategy

    def is_alive(self):
        return len(self.hidden_influences) > 0

    def reset_player(self):
        self.coins = 3
        self.hidden_influences = []
        self.revealed_influences = []

    def get_action(self, gamestate):
        return self.player_strategy.action_strategy(gamestate)

    def get_counteraction(self, gamestate):
        return self.player_strategy.counteraction_strategy(gamestate, self)

    def lose_influence(self, gamestate):
        influence_to_lose = self.player_strategy.influence_loss_strategy(
            gamestate, self
        )
        lose_ind = self.hidden_influences.index(influence_to_lose)
        self.revealed_influences.append(self.hidden_influences.pop(lose_ind))

    def disqualify(self):
        # Add all of the players hidden influences to their revealed influences.
        self.revealed_influences.extend(self.hidden_influences)
        self.hidden_influences = []

    def get_exchange(self, gamestate, cards):
        self.hidden_influences.append(cards)
        cards_to_keep, cards_to_return = self.player_strategy.exchange_strategy(
            gamestate
        )
        self.hidden_influences = cards_to_keep
        return cards_to_return

    def satisfies_action_requirement(self, action):
        if not action.challengeable:
            return True
        return any(
            isinstance(influence, action.requirement)
            for influence in self.hidden_influences
        )

    def get_num_influences(self):
        return len(self.hidden_influences)

    def pay_cost(self, cost):
        if self.coins < cost:
            return False
        self.coins -= cost
        return True

    def print_player_state(self, hidden=False):
        print(self.name + ":")
        print("Coins: " + str(self.coins))
        if hidden:
            print(
                "Hidden Influences: "
                + str([str(influence) for influence in self.hidden_influences])
            )
        print(
            "Revealed Influences: "
            + str([str(influence) for influence in self.revealed_influences])
        )

    def replace_influence(self, gamestate, influence):
        card = gamestate.deck.draw_card()
        self.hidden_influences.append(card)
        replace_ind = self._find_influence_to_replace(influence)
        gamestate.return_card_to_deck(self.hidden_influences.pop(replace_ind))

    def _find_influence_to_replace(self, influence):
        """
        Helper function for replace_influence.

        Iterate through the player's hidden influences, and return the index
        of the first element that is an instance of influence.
        """
        for i, hidden_influence in enumerate(self.hidden_influences):
            if isinstance(hidden_influence, influence):
                return i
        return None
