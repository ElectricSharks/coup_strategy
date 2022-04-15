"""
Tax
    action_name: Tax
    action_description: Take 3 coins from the treasury.
    action_cost: 0
    action_type: character
    action_requirement: Duke
    blockable: False
    challengeable: True
"""

"""
Assassinate
    action_name: Assassinate
    action_description: Pay 3 coins to the Treasury and launch an assassination
                        attempt against another player. If successful that
                        player immediately loses an influence (can be blocked by
                        the Contessa).
    action_cost: 3
    action_type: character
    action_requirement: Assassin
    blockable: True
    challengeable: True
"""


"""
Steal
    action_name: Steal
    action_description: Take 2 coins from another player, if they have one coin,
                        take 1 coin from them.
    action_cost: 0
    action_type: character
    action_requirement: Captain
    blockable: True
    challengeable: True
"""

"""
Exchange
    action_name: Exchange
    action_description: Exchange cards with the Court deck. First take two
                        random cards from the Court deck. Choose which, if any
                        to exchange with your face-down cards. Then return two
                        cards to the Court deck.
    action_cost: 0
    action_type: character
    action_requirement: Ambassador
    blockable: False
    challengeable: True
"""

"""
Block Assasination
    action_name: Block Assasination
    action_description: The player who is being assasinated may claim the
                        Contessa and counteract to block the assassination. The
                        assasination attempt fails but the fee paid by the
                        player for the assassin remains spent.
    action_cost: 0
    action_type: counteraction
    action_requirement: Contessa
    blockable: True
    challengeable: True
"""

"""
Block Foreign Aid
    action_name: Block Foreign Aid
    action_description: Any player claiming the Duke may counteract and block a
                        player attempting to collect foreign aid.
    action_cost: 0
    action_type: counteraction                   
    action_requirement: Duke
    blockable: False
    challengeable: True
"""

"""
Block Stealing
    action_name: Block Stealing
    action_description: The player who is being stolen from may claim either the
                        Ambassador or the Captain and counteract to block the
                        steal. The player trying to steal receives no coins that
                        turn.
    action_cost: 0
    action_type: counteraction
    action_requirement: Ambassador or Captain
    blockable: False
    challengeable: True
"""

"""
Income
    action_name: Income
    action_description: Take 1 coin from the treasury.
    action_cost: 0
    action_type: general
    action_requirement: None
    blockable: False
    challengeable: False
"""

"""
Foreign Aid
    action_name: Foreign Aid
    action_description: Take 2 coins from the treasury (can be blocked by the
                        Duke).
    action_cost: 0
    action_type: general
    action_requirement: None
    blockable: True
    challengeable: False
"""

"""
Coup
    action_name: Coup
    action_description: Pay 7 coins to the Treasury and launch a Coup against
                        another player. That player immediately loses an
                        influence. A Coup is always successful. If you start
                        your turn with 10 (or more) coins you are required to
                        launch a Coup.
    action_cost: 7
    action_type: general
    action_requirement: None
    blockable: False
    challengeable: False
"""

"""
Challenge
    action_name: Challenge
    action_description: If a player is challenged they must prove they had the
                        required influence by showing the relevant character is
                        one of their face-down cards. If they can't, or do not
                        wish to, prove it, they lose the challenge. If they can,
                        the challenger loses.
                        Whoever loses the challenge immediately loses an influence.
                        If a player wins a challenge by showing the relevant
                        character card, they first return that card to the Court
                        deck, re-shuffle the Court deck and take a random
                        replacement card.
    action_cost: 0
    action_type: challenge
    action_requirement: None
    blockable: False
    challengeable: False
"""