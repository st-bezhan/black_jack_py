from Deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()

    def deal(self):
        self.deck.shuffle()
        return self.deck.cards.pop()

    def restart(self):
        self.deck = Deck()