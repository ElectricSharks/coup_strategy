from action import BlockStealingCaptain, Tax, BlockForeignAid, Assassinate, BlockAssasination, Steal, BlockStealingAmbassador, BlockStealingCaptain, Exchange

"""
Duke:
    name: Duke
    actions: [Tax, Block Foreign Aid]
"""
class Duke:
    name = "Duke"
    actions = [Tax, BlockForeignAid]

"""
Assassin:
    name: Assassin
    actions: [Assassinate]
"""
class Assassin:
    name = "Assassin"
    actions = [Assassinate]

"""
Captain:
    name: Captain
    actions: [Steal, Block Stealing]
"""
class Captain:
    name = "Captain"
    actions = [Steal, BlockStealingCaptain]

"""
Ambassador:
    name: Ambassador
    actions: [Exchange, Block Stealing]
"""
class Ambassador:
    name = "Ambassador"
    actions = [Exchange, BlockStealingAmbassador]

"""
Contessa:
    name: Contessa
    actions: [Block Assasination]
"""
class Contessa:
    name = "Contessa"
    actions = [BlockAssasination]
