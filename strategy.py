"""
Honest Action Strategy Function
    Inputs:
        - gamestate: GameState
    Outputs:
        - action: Action

    Description:
        Find the active player, if they have enough coins to use the Coup action
        return the Coup action with the target being the player with the most
        remaining influences (if there is a tie, choose the player with the most
        coins, if there is still a tie, choose randomly).
        
        If they don't have enough coins to use the Coup action, but they do have
        the Duke card use the Tax action.

        If they don't have the Duke card, return the Income action. 
"""