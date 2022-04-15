"""
Game Class
    
    Fields:
        game_state: GameState

    
    Methods:
        __init__(players):
        setup_game():
            Create the inital game state.
        play():
            Iterate through the players calling handle_turn until the game is
            over. 
        handle_turn(player):
            Get the active player's action, if the action has a cost this is
            where the player must pay it. If the player chooses an action which
            costs more than they can afford, they lose both influences
            immediately.
            Iterate through the other player's to see if any of them wish to
            make a counteraction.
            If a counteraction other than a challenge is made, iterate through
            the players (other than the player who made the counteraction) to
            see if any of them wish to make a second counteraction.
            Resolve the action stack. 
"""