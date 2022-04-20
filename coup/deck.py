from random import shuffle
from coup.influence import Duke, Ambassador, Captain, Assassin, Contessa

"""
Deck Class
    
    Fields:
        deck: list of cards

    Methods:
        __init__():
        shuffle():
        draw_card():
        draw_cards(num):
        return_cards(cards):
        reset():

    Description:
        The deck contains three of each type of card (Duke, Assassin, Captain,
        Ambassador, Contessa).
"""


class Deck:
    def __init__(self):
        self.deck = []
        self.reset()

    def shuffle(self):
        shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def draw_cards(self, num):
        return [self.draw_card() for _ in range(num)]

    def return_cards(self, cards):
        self.deck.extend(cards)
        self.shuffle()

    def return_card(self, card):
        self.deck.append(card)
        self.shuffle()

    def reset(self):
        self.deck = [
            Duke(),
            Duke(),
            Duke(),
            Assassin(),
            Assassin(),
            Assassin(),
            Captain(),
            Captain(),
            Captain(),
            Ambassador(),
            Ambassador(),
            Ambassador(),
            Contessa(),
            Contessa(),
            Contessa(),
        ]
        self.shuffle()
