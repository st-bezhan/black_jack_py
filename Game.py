from Card import Card
from Deck import Deck
from Ranks import Rank


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self):
        current_hand: [Card] = []
        try:
            while True:
                input("Press enter to deal.")
                new_card = self.deal()
                if new_card.rank is Rank.ACE:
                    new_card.set_ace_value()

                current_hand.append(new_card)
                for card in current_hand:
                    print(card.value, card.suit.name, card.rank.name)

        except KeyboardInterrupt as interrupt:
            print(interrupt)

    def deal(self) -> [Card]:
        """First deal must be 2 cards, others are 1 card."""

        if self.deck.cards is None or self.deck.cards == []:
            raise ValueError("No cards in deck.")

        try:
            return self.deck.cards.pop()
        except Exception as error:
            print(error)



    def restart(self):
        self.deck = Deck()
        self.deck.shuffle()