from python.game.influence import Duke, Assassin, Contessa, Captain, Ambassador
"""
Action Class
    Fields:
        user: Player
        name: None
        succeeds: bool (default: True)
        target (optional): Player or None

    Methods:
        print_action():
            Print the name of the action user, the action they are attempting to
            perform and, if applicable, the target of the action.
"""
class Action:
    def __init__(self, user, name, target=None):
        self.user = user
        self.name = name
        self.succeeds = True
        self.target = target

    def print_action(self):
        print_string = self.user.name + " is attempting to use " + self.name
        if self.target is not None:
            print_string += " on " + self.target.name
        print(print_string)



"""
Tax - Action

    Attributes:
        name: Tax
        description: Take 3 coins from the treasury.
        cost: 0
        type: character
        requirement: Duke
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        user: Player
        succeeds: True

    
    Methods:
        resolve(gamestate):
            Active player gains 3 coins.

        @staticmethod
        is_legal(gamestate, user): bool
            Check that the user is the active player, checks that the user is
            alive and checks that the user currently has less than 10 coins.
"""
class Tax(Action):

    name = "Tax"
    description = "Take 3 coins from the treasury."
    cost = 0
    type = "character"
    requirement = Duke
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)
    
    def resolve(self, gamestate):
        self.user.coins += 3

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)


"""
Assassinate - Action
    Attributes:
        name: Assassinate
        description: Pay 3 coins to the Treasury and launch an
                            assassination attempt against another player. If
                            successful that player immediately loses an
                            influence (can be blocked by the Contessa).
        cost: 3
        type: character
        requirement: Assassin
        blockable: True
        challengeable: True
        has_target: True

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            Target player must choose an influnce to lose.

        @staticmethod
        is_legal(gamestate, user, target): bool
            Checks that the user is the active player, checks that the user is
            alive, checks that the target of the user is not the user and is
            alive, checks that the user has less than 10 coins and checks that
            the user has 3 or more coins.
"""
class Assassinate(Action):
    
    name = "Assassinate"
    description = "Pay 3 coins to the Treasury and launch an assassination attempt against another player. If successful that player immediately loses an influence (can be blocked by the Contessa)."
    cost = 3
    type = "character"
    requirement = Assassin
    blockable = True
    challengeable = True
    has_target = True

    def __init__(self, user, target):
        super().__init__(user, self.name, target)

    def resolve(self, gamestate):
        self.target.lose_influence(gamestate)

    @staticmethod
    def is_legal(gamestate, user, target):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                target != user and
                target.alive and
                user.coins >= 3 and
                user.coins < 10)

"""
Steal - Action
    Attributes:
        name: Steal
        description: Take 2 coins from another player, if they have one
                            coin, take 1 coin from them.
        cost: 0
        type: character
        requirement: Captain
        blockable: True
        challengeable: True
        has_target: True

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            If the target player has 2 or more coins, they lose 2 coins, if they
            have 1 coin they lose that 1 coin. Active player gains the lost
            coins. If the target has no coins, the steal action cannot target
            them.

        @staticmethod
        is_legal(gamestate, user, target): bool
            Checks that the user is the active player, checks that the user is
            alive, checks that the target of the user is not the user, has more
            than 0 coins and is alive and checks that the user has less than 10
            coins.
"""
class Steal(Action):
        
    name = "Steal"
    description = "Take 2 coins from another player, if they have one, take 1 coin from them."
    cost = 0
    type = "character"
    requirement = Captain
    blockable = True
    challengeable = True
    has_target = True

    def __init__(self, user, target):
        super().__init__(user, self.name, target)

    def resolve(self, gamestate):
        if self.target.coins > 1:
            self.target.coins -= 2
            self.user.coins += 2
        elif self.target.coins == 1:
            self.target.coins -= 1
            self.user.coins += 1

    @staticmethod
    def is_legal(gamestate, user, target):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                target != user and
                target.alive and
                target.coins > 0 and
                user.coins < 10)


"""
Exchange - Action
    Attributes:
        name: Exchange
        description: Exchange cards with the Court deck. First take two
                            random cards from the Court deck. Choose which, if
                            any to exchange with your face-down cards. Then
                            return two cards to the Court deck.
        cost: 0
        type: character
        requirement: Ambassador
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            Draw two cards from the deck, then invoke the get_player_exchange
            function on the active player to get the cards they wish to return
            to the deck. Then return those cards to the deck.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is the active player, checks that the user is
            alive, checks that the user has less than 10 coins.
"""
class Exchange(Action):
        
    name = "Exchange"
    description = "Exchange cards with the Court deck. First take two random cards from the Court deck. Choose which, if any to exchange with your face-down cards. Then return two cards to the Court deck."
    cost = 0
    type = "character"
    requirement = Ambassador
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        exchange_cards = [gamestate.draw_card(), gamestate.draw_card()]
        cards_to_return = self.user.get_player_exchange(gamestate, exchange_cards)
        for card in cards_to_return:
            gamestate.return_card(card)

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)

"""
Block Assassination - Action
    Attributes:
        name: Block Assassination
        description: The player who is being assassinated may claim the
                            Contessa and counteract to block the assassination.
                            The assasination attempt fails but the fee paid by
                            the player for the assassin remains spent.
        cost: 0
        type: counteraction
        requirement: Contessa
        blockable: True
        challengeable: True
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is an Assassination action,
            its succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is an assasination action with the user
            as the target, checks that the user is alive.
"""
class BlockAssassination(Action):
        
    name = "Block Assassination"
    description = "The player who is being assassinated may claim the Contessa and counteract to block the assassination. The assasination attempt fails but the fee paid by the player for the assassin remains spent."
    cost = 0
    type = "counteraction"
    requirement = Contessa
    blockable = True
    challengeable = True
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), Assassinate):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.succeeds = False
            gamestate.action_stack.push(blocked_action)


    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), Assassinate) and
                gamestate.action_stack.peek().target == user)

"""
Block Foreign Aid - Action
    Attributes:
        name: Block Foreign Aid
        description: Any player claiming the Duke may counteract and
                            block a player attempting to collect foreign aid.
        cost: 0
        type: counteraction                   
        requirement: Duke
        blockable: False
        challengeable: True
        has_target: False
    
    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a foreign aid action, its
            succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is a foreign aid action, checks that the
            user is alive.
"""
class BlockForeignAid(Action):        
    name = "Block Foreign Aid"
    description = "Any player claiming the Duke may counteract and block a player attempting to collect foreign aid."
    cost = 0
    type = "counteraction"
    requirement = Duke
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), ForeignAid):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.succeeds = False
            gamestate.action_stack.push(blocked_action)

    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), ForeignAid))

"""
Block Stealing Ambassador - Action
    Attributes:
        name: Block Stealing
        description: The player who is being stolen from may claim the
                            Ambassador and counteract to block the steal. The
                            player trying to steal receives no coins that turn.
        cost: 0
        type: counteraction
        requirement: Ambassador
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a steal action, its 
            succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is a steal action, checks that the user
            is alive.
"""
class BlockStealingAmbassador(Action):
    name = "Block Stealing"
    description = "The player who is being stolen from may claim the Ambassador and counteract to block the steal. The player trying to steal receives no coins that turn."
    cost = 0
    type = "counteraction"
    requirement = Ambassador
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), Steal):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.succeeds = False
            gamestate.action_stack.push(blocked_action)

    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), Steal))

"""
Block Stealing Captain - Action
    Attributes:
        name: Block Stealing
        description: The player who is being stolen from may claim the
                            Captain and counteract to block the steal. The
                            player trying to steal receives no coins that turn.
        cost: 0
        type: counteraction
        requirement: Captain
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a steal action, its 
            succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is a steal action, checks that the user
            is alive.
"""
class BlockStealingCaptain(Action):
    name = "Block Stealing"
    description = "The player who is being stolen from may claim the Captain and counteract to block the steal. The player trying to steal receives no coins that turn."
    cost = 0
    type = "counteraction"
    requirement = Captain
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), Steal):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.succeeds = False
            gamestate.action_stack.push(blocked_action)

    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), Steal))

"""
Income - Action
    Attributes:
        name: Income
        description: Take 1 coin from the treasury.
        cost: 0
        type: general
        requirement: None
        blockable: False
        challengeable: False
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            Active player gains 1 coin.
        
        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is the active player, checks that the user is
            alive and checks that the user currently has less than 10 coins.
"""
class Income(Action):
    name = "Income"
    description = "Take 1 coin from the treasury."
    cost = 0
    type = "general"
    requirement = None
    blockable = False
    challengeable = False
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        self.user.coins += 1

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)

"""
Foreign Aid - Action
    Attributes:
        name: Foreign Aid
        description: Take 2 coins from the treasury (can be blocked by
                            the Duke).
        cost: 0
        type: general
        requirement: None
        blockable: True
        challengeable: False
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            Active player gains 2 coins.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is the active player, checks that the user is
            alive and checks that the user currently has less than 10 coins.
"""
class ForeignAid(Action):
    name = "Foreign Aid"
    description = "Take 2 coins from the treasury (can be blocked by the Duke)."
    cost = 0
    type = "general"
    requirement = None
    blockable = True
    challengeable = False
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        self.user.coins += 2

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)

"""
Coup - Action
    Attributes:
        name: Coup
        description: Pay 7 coins to the Treasury and launch a Coup
                            against another player. That player immediately
                            loses an influence. A Coup is always successful.
                            If you start your turn with 10 (or more) coins you
                            are required to launch a Coup.
        cost: 7
        type: general
        requirement: None
        blockable: False
        challengeable: False
        has_target: True

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            Target player must choose an influence to lose.

        @staticmethod
        is_legal(gamestate, user, target): bool
            Checks that the user is the active player, checks that the user is
            alive and checks that the user currently has 7 or more coins.
"""
class Coup(Action):
    name = "Coup"
    description = "Pay 7 coins to the Treasury and launch a Coup against another player. That player immediately loses an influence. A Coup is always successful. If you start your turn with 10 (or more) coins you are required to launch a Coup."
    cost = 7
    type = "general"
    requirement = None
    blockable = False
    challengeable = False
    has_target = True

    def __init__(self, user, target):
        super().__init__(user, self.name, target)

    def resolve(self, gamestate):
        self.target.lose_influence(gamestate)

    @staticmethod
    def is_legal(gamestate, user, target):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins >= 7)

"""
Challenge - Action
    Attributes:
        name: Challenge
        description: If a player is challenged they must prove they had
                            the required influence by showing the relevant
                            character is one of their face-down cards. If they
                            can't, or do not wish to, prove it, they lose the
                            challenge. If they can, the challenger loses.
                            Whoever loses the challenge immediately loses an
                            influence. If a player wins a challenge by showing
                            the relevant character card, they first return that
                            card to the Court deck, re-shuffle the Court deck
                            and take a random replacement card.
        cost: 0
        type: challenge
        requirement: None
        blockable: False
        challengeable: False
        has_target: False

    Fields:
        user: Player
        succeeds: True

    Methods:
        resolve(gamestate):
            If the challenged player satisfies the action requirement, the
            challenger must lose an influence; and the challenged player must
            draw a new influence from the deck and then return the influence
            that satisfied the action requirement to the deck.

            If the challenged player does not satisfy the action requirement,
            they must lose an influence and the succeeds field of the
            top action in the action stack is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the action stack is not empty, that the user is alive,
            that the top action in the action stack is challengeable and that
            the user is not the user for the top action in the action
            stack.
"""
class Challenge(Action):
    name = "Challenge"
    description = "If a player is challenged they must prove they had the required influence by showing the relevant character is one of their face-down cards. If they can't, or do not wish to, prove it, they lose the challenge. If they can, the challenger loses. Whoever loses the challenge immediately loses an influence. If a player wins a challenge by showing the relevant character card, they first return that card to the Court deck, re-shuffle the Court deck and take a random replacement card."
    cost = 0
    type = "challenge"
    requirement = None
    blockable = False
    challengeable = False
    has_target = False

    def __init__(self, user):
        super().__init__(user, self.name)

    def resolve(self, gamestate):
        challenged_action = self.gamestate.action_stack.peek()
        challenged_player = challenged_action.user
        if challenged_player.satisfies_requirement(challenged_action):
            self.user.lose_influence(gamestate)
            challenged_player.replace_influence(gamestate, challenged_action.requirement)
        else:
            challenged_action.succeeds = False
            challenged_player.lose_influence(gamestate)

    @staticmethod
    def is_legal(gamestate, user):
        return (not gamestate.action_stack.is_empty() and
                user.is_alive() and
                gamestate.action_stack.peek().challengeable and
                user != gamestate.action_stack.peek().user)

