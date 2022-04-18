from python.game.action_stack import ActionStack
from python.game.deck import Deck
from python.game.action import *
"""
GameState Class

    Container for the current state of the game.

    Fields:
        - players: list of Player objects
        - player_turn_tracker: list of Player objects
        - action_stack: ActionStack
        - deck: Deck
    
    Methods:
        __init__(self, players):
        is_game_over(): bool
            Returns True if the number of players in the player_turn_tracker is
            less than or equal to 1.
        reset():
            Reset the deck, set the player_turn_tracker equal to a copy of the
            players list.
            Iterate through the players, invoking the reset_player method on
            each of them, and setting their hidden_influences to a list of 
            two cards popped from the deck.
        get_active_player(): Player or None
            Return the first element of the player_turn_tracker, or none if the
            player_turn_tracker is empty.
        resolve_action_stack():
        print_game_state(current_player):
            Iterate through the players, invoking print_state on each of them,
            print the current player's state with hidden=True. Then print the
            action stack's state.
        next_turn():
            Move the first player to the back of the player_turn_tracker, then
            iterate through the player_turn_tracker only keeping the players
            who are still alive.
        get_legal_actions(player): list(Action, Target or None)
            Iterate through all of the actions, checking whether they are legal
            for the active player. Return a list of tuples of the form (action,
            target), where target is a different player or None. 
        draw_card(): Influence
        return_card_to_deck(card):
        play(action):
            Add the action to the action_stack.
"""
class GameState:
    def __init__(self, players):
        self.players = players
        self.player_turn_tracker = players[:]
        self.action_stack = ActionStack()
        self.deck = Deck()
        self.reset()
    
    def is_game_over(self):
        return len(self.player_turn_tracker) <= 1
    
    def reset(self):
        self.deck.reset()
        self.player_turn_tracker = self.players[:]
        for player in self.players:
            player.reset_player()
            player.hidden_influences = self.deck.draw_cards(2)
    
    def get_active_player(self):
        if not self.is_game_over():
            return self.player_turn_tracker[0]
        return None
    
    def resolve_action_stack(self):
        self.action_stack.resolve(self)
    
    def print_game_state(self, current_player):
        for player in self.players:
            player.print_player_state(hidden=(player == current_player))
        self.action_stack.print_state()
    
    def next_turn(self):
        self.player_turn_tracker.append(self.player_turn_tracker.pop(0))
        self.player_turn_tracker = [player for player in self.player_turn_tracker if player.is_alive()]
    
    def get_legal_actions(self, player):
        actions_with_targets = [Assassinate, Coup, Steal]
        actions_without_targets = [
            Tax, Exchange, BlockAssassination, BlockForeignAid,
            BlockStealingAmbassador, BlockStealingCaptain, Income,
            ForeignAid, Challenge
        ]
        opposing_players = [p for p in self.players if p != player]
        legal_actions = [action(player) for action in actions_without_targets if action.is_legal(self.gamestate, player)]
        for target in opposing_players:
            legal_actions.extend([action(player, target) for action in actions_with_targets if action.is_legal(self.gamestate, player, target)])
        
        return legal_actions
    
    def draw_card(self):
        return self.deck.draw_card()
    
    def return_card_to_deck(self, card):
        self.deck.return_card(card)

    def play(self, action):
        self.action_stack.push(action)
    
    def get_winner(self):
        if len(self.player_turn_tracker) == 1:
            return self.player_turn_tracker[0]
        return None