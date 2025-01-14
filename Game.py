from functools import reduce

from Card import Card
from Deck import Deck
from Ranks import Rank


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.__first_deal = True

    def play(self):
        hand = []
        print("New game starts!")
        try:
            while True:
                input("Press Enter to deal.")

                new_cards = self.deal()  # Deal one or two cards
                for card in new_cards:
                    if card.rank is Rank.ACE:
                        card.set_ace_value()
                    hand.append(card)

                for card in hand:
                    print(card.value, card.suit.name, card.rank.name)

                hand_score = reduce(lambda x, y: x + y.value, hand, 0)

                if hand_score > 21:
                    print(f"You lose! Score: {hand_score}.")
                    break
                elif hand_score == 21:
                    print(f"You win! Score: {hand_score}.")
                    break
                else:
                    print(f"Your hand: {hand_score}")
                    print(f"Press Ctrl + C to finish or Enter to deal another card.")

        except KeyboardInterrupt as interrupt:
            # Here must be logic for counting score and comparing score with dealer
            self.restart()

    def deal(self) -> [Card]:
        """First deal must be 2 cards, others are 1 card."""

        if self.deck.cards is None or not self.deck.cards:
            raise ValueError("No cards in deck.")

        if self.__first_deal:
            self.__first_deal = False
            return [self.deck.cards.pop(), self.deck.cards.pop()]  # Deal 2 cards
        else:
            return [self.deck.cards.pop()]  # Deal 1 card



    def restart(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.__first_deal = True