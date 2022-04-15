"""
Action Class
    Methods:
        print_action():
            Print the name of the action user, the action they are attempting to
            perform and, if applicable, the target of the action.
        is_legal(gamestate, action, user): bool
            pass
"""



"""
Tax - Action
    
    Fields:
        action_user: Player
        action_name: Tax
        action_description: Take 3 coins from the treasury.
        action_cost: 0
        action_type: character
        action_requirement: Duke
        blockable: False
        challengeable: True
        has_target: False
        action_succeeds: True

    
    Methods:
        resolve(gamestate):
            Active player gains 3 coins.
"""

"""
Assassinate - Action
    Fields:
        action_user: Player
        action_name: Assassinate
        action_description: Pay 3 coins to the Treasury and launch an
                            assassination attempt against another player. If
                            successful that player immediately loses an
                            influence (can be blocked by the Contessa).
        action_cost: 3
        action_type: character
        action_requirement: Assassin
        blockable: True
        challengeable: True
        has_target: True
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Target player must choose an influnce to lose.
"""


"""
Steal - Action
    Fields:
        action_user: Player
        action_name: Steal
        action_description: Take 2 coins from another player, if they have one
                            coin, take 1 coin from them.
        action_cost: 0
        action_type: character
        action_requirement: Captain
        blockable: True
        challengeable: True
        has_target: True
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Target player loses up to 2 coins, without going below 0.
            Active player gains those lost coins.
"""

"""
Exchange - Action
    Fields:
        action_user: Player
        action_name: Exchange
        action_description: Exchange cards with the Court deck. First take two
                            random cards from the Court deck. Choose which, if
                            any to exchange with your face-down cards. Then
                            return two cards to the Court deck.
        action_cost: 0
        action_type: character
        action_requirement: Ambassador
        blockable: False
        challengeable: True
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Two cards are drawn from the deck, the active player then must
            resolve which card/card(s) they want to keep (get_player_exchange).
            The remaining cards are returned to the deck.

"""

"""
Block Assassination - Action
    Fields:
        action_user: Player
        action_name: Block Assassination
        action_description: The player who is being assassinated may claim the
                            Contessa and counteract to block the assassination.
                            The assasination attempt fails but the fee paid by
                            the player for the assassin remains spent.
        action_cost: 0
        action_type: counteraction
        action_requirement: Contessa
        blockable: True
        challengeable: True
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Target player must choose an influence to lose.
"""

"""
Block Foreign Aid - Action
    Fields:
        action_user: Player
        action_name: Block Foreign Aid
        action_description: Any player claiming the Duke may counteract and
                            block a player attempting to collect foreign aid.
        action_cost: 0
        action_type: counteraction                   
        action_requirement: Duke
        blockable: False
        challengeable: True
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a foreign aid action, its
            action_succeeds field is set to False.
"""

"""
Block Stealing - Action
    Fields:
        action_user: Player
        action_name: Block Stealing
        action_description: The player who is being stolen from may claim either
                            the Ambassador or the Captain and counteract to
                            block the steal. The player trying to steal receives
                            no coins that turn.
        action_cost: 0
        action_type: counteraction
        action_requirement: Ambassador or Captain
        blockable: False
        challengeable: True
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a steal action, its 
            action_succeeds field is set to False.
"""

"""
Income - Action
    Fields:
        action_user: Player
        action_name: Income
        action_description: Take 1 coin from the treasury.
        action_cost: 0
        action_type: general
        action_requirement: None
        blockable: False
        challengeable: False
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Active player gains 1 coin.
"""

"""
Foreign Aid - Action
    Fields:
        action_user: Player
        action_name: Foreign Aid
        action_description: Take 2 coins from the treasury (can be blocked by
                            the Duke).
        action_cost: 0
        action_type: general
        action_requirement: None
        blockable: True
        challengeable: False
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Active player gains 2 coins.
"""

"""
Coup - Action
    Fields:
        action_user: Player
        action_name: Coup
        action_description: Pay 7 coins to the Treasury and launch a Coup
                            against another player. That player immediately
                            loses an influence. A Coup is always successful.
                            If you start your turn with 10 (or more) coins you
                            are required to launch a Coup.
        action_cost: 7
        action_type: general
        action_requirement: None
        blockable: False
        challengeable: False
        has_target: True
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Target player must choose an influence to lose.
"""

"""
Challenge - Action
    Fields:
        action_user: Player
        action_name: Challenge
        action_description: If a player is challenged they must prove they had
                            the required influence by showing the relevant
                            character is one of their face-down cards. If they
                            can't, or do not wish to, prove it, they lose the
                            challenge. If they can, the challenger loses.
                            Whoever loses the challenge immediately loses an
                            influence. If a player wins a challenge by showing
                            the relevant character card, they first return that
                            card to the Court deck, re-shuffle the Court deck
                            and take a random replacement card.
        action_cost: 0
        action_type: challenge
        action_requirement: None
        blockable: False
        challengeable: False
        has_target: False
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the challenged player satisfies the action requirement, the
            challenger must lose an influence; and the challenged player must
            draw a new influence from the deck and then return the influence
            that satisfied the action requirement to the deck.

            If the challenged player does not satisfy the action requirement,
            they must lose an influence and the action_succeeds field of the
            top action in the action stack is set to False.
"""