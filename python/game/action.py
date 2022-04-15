from python.game.influence import Duke, Assassin, Contessa, Captain, Ambassador
"""
Action Class
    Fields:
        action_user: Player
        action_name: None
        action_succeeds: bool (default: True)
        target (optional): Player or None

    Methods:
        print_action():
            Print the name of the action user, the action they are attempting to
            perform and, if applicable, the target of the action.
"""
class Action:
    def __init__(self, action_user, action_name, target=None):
        self.action_user = action_user
        self.action_name = action_name
        self.action_succeeds = True
        self.target = target

    def print_action(self):
        print_string = self.action_user.name + " is attempting to use " + self.action_name
        if self.target is not None:
            print_string += " on " + self.target.name
        print(print_string)



"""
Tax - Action

    Attributes:
        action_name: Tax
        action_description: Take 3 coins from the treasury.
        action_cost: 0
        action_type: character
        action_requirement: Duke
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        action_user: Player
        action_succeeds: True

    
    Methods:
        resolve(gamestate):
            Active player gains 3 coins.

        @staticmethod
        is_legal(gamestate, user): bool
            Check that the user is the active player, checks that the user is
            alive and checks that the user currently has less than 10 coins.
"""
class Tax(Action):

    action_name = "Tax"
    action_description = "Take 3 coins from the treasury."
    action_cost = 0
    action_type = "character"
    action_requirement = Duke
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)
    
    def resolve(self, gamestate):
        self.action_user.coins += 3

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)


"""
Assassinate - Action
    Attributes:
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

    Fields:
        action_user: Player
        action_succeeds: True

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
    
    action_name = "Assassinate"
    action_description = "Pay 3 coins to the Treasury and launch an assassination attempt against another player. If successful that player immediately loses an influence (can be blocked by the Contessa)."
    action_cost = 3
    action_type = "character"
    action_requirement = Assassin
    blockable = True
    challengeable = True
    has_target = True

    def __init__(self, action_user, target):
        super().__init__(action_user, self.action_name, target)

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
        action_name: Steal
        action_description: Take 2 coins from another player, if they have one
                            coin, take 1 coin from them.
        action_cost: 0
        action_type: character
        action_requirement: Captain
        blockable: True
        challengeable: True
        has_target: True

    Fields:
        action_user: Player
        action_succeeds: True

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
        
    action_name = "Steal"
    action_description = "Take 2 coins from another player, if they have one, take 1 coin from them."
    action_cost = 0
    action_type = "character"
    action_requirement = Captain
    blockable = True
    challengeable = True
    has_target = True

    def __init__(self, action_user, target):
        super().__init__(action_user, self.action_name, target)

    def resolve(self, gamestate):
        if self.target.coins > 1:
            self.target.coins -= 2
            self.action_user.coins += 2
        elif self.target.coins == 1:
            self.target.coins -= 1
            self.action_user.coins += 1

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

    Fields:
        action_user: Player
        action_succeeds: True

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
        
    action_name = "Exchange"
    action_description = "Exchange cards with the Court deck. First take two random cards from the Court deck. Choose which, if any to exchange with your face-down cards. Then return two cards to the Court deck."
    action_cost = 0
    action_type = "character"
    action_requirement = Ambassador
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        exchange_cards = [gamestate.draw_card(), gamestate.draw_card()]
        cards_to_return = self.action_user.get_player_exchange(gamestate, exchange_cards)
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

    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is an Assassination action,
            its action_succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is an assasination action with the user
            as the target, checks that the user is alive.
"""
class BlockAssassination(Action):
        
    action_name = "Block Assassination"
    action_description = "The player who is being assassinated may claim the Contessa and counteract to block the assassination. The assasination attempt fails but the fee paid by the player for the assassin remains spent."
    action_cost = 0
    action_type = "counteraction"
    action_requirement = Contessa
    blockable = True
    challengeable = True
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), Assassinate):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.action_succeeds = False
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
        action_name: Block Foreign Aid
        action_description: Any player claiming the Duke may counteract and
                            block a player attempting to collect foreign aid.
        action_cost: 0
        action_type: counteraction                   
        action_requirement: Duke
        blockable: False
        challengeable: True
        has_target: False
    
    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a foreign aid action, its
            action_succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is a foreign aid action, checks that the
            user is alive.
"""
class BlockForeignAid(Action):        
    action_name = "Block Foreign Aid"
    action_description = "Any player claiming the Duke may counteract and block a player attempting to collect foreign aid."
    action_cost = 0
    action_type = "counteraction"
    action_requirement = Duke
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), ForeignAid):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.action_succeeds = False
            gamestate.action_stack.push(blocked_action)

    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), ForeignAid))

"""
Block Stealing Ambassador - Action
    Attributes:
        action_name: Block Stealing
        action_description: The player who is being stolen from may claim the
                            Ambassador and counteract to block the steal. The
                            player trying to steal receives no coins that turn.
        action_cost: 0
        action_type: counteraction
        action_requirement: Ambassador
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a steal action, its 
            action_succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is a steal action, checks that the user
            is alive.
"""
class BlockStealingAmbassador(Action):
    action_name = "Block Stealing"
    action_description = "The player who is being stolen from may claim the Ambassador and counteract to block the steal. The player trying to steal receives no coins that turn."
    action_cost = 0
    action_type = "counteraction"
    action_requirement = Ambassador
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), Steal):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.action_succeeds = False
            gamestate.action_stack.push(blocked_action)

    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), Steal))

"""
Block Stealing Captain - Action
    Attributes:
        action_name: Block Stealing
        action_description: The player who is being stolen from may claim the
                            Captain and counteract to block the steal. The
                            player trying to steal receives no coins that turn.
        action_cost: 0
        action_type: counteraction
        action_requirement: Captain
        blockable: False
        challengeable: True
        has_target: False

    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            If the top action in the action stack is a steal action, its 
            action_succeeds field is set to False.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is not the active player, checks that the last
            action in the action stack is a steal action, checks that the user
            is alive.
"""
class BlockStealingCaptain(Action):
    action_name = "Block Stealing"
    action_description = "The player who is being stolen from may claim the Captain and counteract to block the steal. The player trying to steal receives no coins that turn."
    action_cost = 0
    action_type = "counteraction"
    action_requirement = Captain
    blockable = False
    challengeable = True
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        if isinstance(gamestate.action_stack.peek(), Steal):
            blocked_action = gamestate.action_stack.pop()
            blocked_action.action_succeeds = False
            gamestate.action_stack.push(blocked_action)

    @staticmethod
    def is_legal(gamestate, user):
        return (user != gamestate.get_active_player() and
                user.is_alive() and
                isinstance(gamestate.action_stack.peek(), Steal))

"""
Income - Action
    Attributes:
        action_name: Income
        action_description: Take 1 coin from the treasury.
        action_cost: 0
        action_type: general
        action_requirement: None
        blockable: False
        challengeable: False
        has_target: False

    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Active player gains 1 coin.
        
        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is the active player, checks that the user is
            alive and checks that the user currently has less than 10 coins.
"""
class Income(Action):
    action_name = "Income"
    action_description = "Take 1 coin from the treasury."
    action_cost = 0
    action_type = "general"
    action_requirement = None
    blockable = False
    challengeable = False
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        self.action_user.coins += 1

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)

"""
Foreign Aid - Action
    Attributes:
        action_name: Foreign Aid
        action_description: Take 2 coins from the treasury (can be blocked by
                            the Duke).
        action_cost: 0
        action_type: general
        action_requirement: None
        blockable: True
        challengeable: False
        has_target: False

    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Active player gains 2 coins.

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the user is the active player, checks that the user is
            alive and checks that the user currently has less than 10 coins.
"""
class ForeignAid(Action):
    action_name = "Foreign Aid"
    action_description = "Take 2 coins from the treasury (can be blocked by the Duke)."
    action_cost = 0
    action_type = "general"
    action_requirement = None
    blockable = True
    challengeable = False
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        self.action_user.coins += 2

    @staticmethod
    def is_legal(gamestate, user):
        return (user == gamestate.get_active_player() and
                user.is_alive() and
                user.coins < 10)

"""
Coup - Action
    Attributes:
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

    Fields:
        action_user: Player
        action_succeeds: True

    Methods:
        resolve(gamestate):
            Target player must choose an influence to lose.

        @staticmethod
        is_legal(gamestate, user, target): bool
            Checks that the user is the active player, checks that the user is
            alive and checks that the user currently has 7 or more coins.
"""
class Coup(Action):
    action_name = "Coup"
    action_description = "Pay 7 coins to the Treasury and launch a Coup against another player. That player immediately loses an influence. A Coup is always successful. If you start your turn with 10 (or more) coins you are required to launch a Coup."
    action_cost = 7
    action_type = "general"
    action_requirement = None
    blockable = False
    challengeable = False
    has_target = True

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

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

    Fields:
        action_user: Player
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

        @staticmethod
        is_legal(gamestate, user): bool
            Checks that the action stack is not empty, that the user is alive,
            that the top action in the action stack is challengeable and that
            the user is not the action_user for the top action in the action
            stack.
"""
class Challenge(Action):
    action_name = "Challenge"
    action_description = "If a player is challenged they must prove they had the required influence by showing the relevant character is one of their face-down cards. If they can't, or do not wish to, prove it, they lose the challenge. If they can, the challenger loses. Whoever loses the challenge immediately loses an influence. If a player wins a challenge by showing the relevant character card, they first return that card to the Court deck, re-shuffle the Court deck and take a random replacement card."
    action_cost = 0
    action_type = "challenge"
    action_requirement = None
    blockable = False
    challengeable = False
    has_target = False

    def __init__(self, action_user):
        super().__init__(action_user, self.action_name)

    def resolve(self, gamestate):
        challenged_action = self.gamestate.action_stack.peek()
        challenged_player = challenged_action.action_user
        if challenged_player.satisfies_action_requirement(challenged_action):
            self.action_user.lose_influence(gamestate)
            challenged_player.replace_influence(gamestate, challenged_action.action_requirement)
        else:
            challenged_action.action_succeeds = False
            challenged_player.lose_influence(gamestate)

    @staticmethod
    def is_legal(gamestate, user):
        return (not gamestate.action_stack.is_empty() and
                user.is_alive() and
                gamestate.action_stack.peek().challengeable and
                user != gamestate.action_stack.peek().action_user)

