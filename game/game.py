from python.game.gamestate import GameState
"""
Game Class
    
    Fields:
        gamestate: GameState

    
    Methods:
        __init__(players):
        reset():
            Resets the initial game state.
        play():
            Iterate through the players calling handle_turn until the game is
            over. 
        handle_turn():
            Get the active player's action, if the action has a cost this is
            where the player must pay it. If the player chooses an action which
            costs more than they can afford, they are disqualified.
            Iterate through the other players to see if any of them wish to
            make a counteraction.
            If a counteraction other than a challenge is made, iterate through
            the players (other than the player who made the counteraction) to
            see if any of them wish to make a second counteraction.
            Resolve the action stack.
        _get_counteraction(acting_player): (Action, Player) or (None, None)
            Iterate through the players not including the acting_player, and
            check if any of them wish to make a counteraction. If so  return the
            counteraction and the player who played it otherwise return None,
            None.
"""
class Game:
    def __init__(self, players):
        self.gamestate = GameState(players)
        self.reset()
    
    def reset(self):
        self.gamestate.reset()
    
    def play(self):
        while not self.gamestate.is_game_over():
            self.handle_turn()
            self.gamestate.next_turn()
        winner = self.gamestate.get_winner()
        print(f"The winner is {winner.name}!")
    
    def handle_turn(self):
        """
        Get the active player's action, if the action has a cost this is
        where the player must pay it. If the player chooses an action which
        costs more than they can afford, they are disqualified.
        Iterate through the other players to see if any of them wish to
        make a counteraction.
        If a counteraction other than a challenge is made, iterate through
        the players (other than the player who made the counteraction) to
        see if any of them wish to make a second counteraction.
        Resolve the action stack.
        """
        active_player = self.gamestate.get_active_player()
        action = active_player.get_action(self.gamestate)
        if action.cost:
            cost_paid = active_player.pay_cost(action.cost)
            if not cost_paid:
                active_player.disqualify()
        # Play the action.
        self.gamestate.play(action)

        # Iterate through the players not equal to the active player to see if
        # any of them wish to make a counteraction.
        counteraction, counter_player = self._get_counteraction(active_player)
        if counteraction:
            self.gamestate.play(counteraction)
            # Iterate through the players other than the counter_player to see
            # if any of them wish to make a second counteraction.
            counteraction, counter_player = self._get_counteraction(counter_player)
            if counteraction:
                self.gamestate.play(counteraction)
        self.gamestate.resolve_action_stack()
    
    def _get_counteraction(self, acting_player):
        """
        Iterate through the players not including the acting_player, and
        check if any of them wish to make a counteraction. If so  return the
        counteraction and the player who played it otherwise return None,
        None.
        """
        for player in self.gamestate.players:
            if player != acting_player:
                counteraction = player.get_counteraction(self.gamestate)
                if counteraction:
                    return counteraction, player
        return None, None