from Card import Card
from Ranks import Rank
from Suit import Suit
import random

class Deck:
    def __init__(self):
        self.cards = []
        for rank in Rank:
            for suit in Suit:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cards)