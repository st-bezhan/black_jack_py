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
        while True:  # Loop to handle restarting the game
            hand = []
            self.__first_deal = True  # Reset first deal for new game
            print("Starting a new game!")

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
                        print(f"Blackjack! You win! Score: {hand_score}.")
                        break
                    else:
                        print(f"Your hand: {hand_score}")
                        print(f"Press Ctrl + C to finish or Enter to continue.")

                # Game ended; ask to restart or exit
                if not self.ask_restart():
                    break

            except KeyboardInterrupt:
                print("\nGame interrupted. Dealer's turn!")
                self.dealer_turn(hand)
                if not self.ask_restart():
                    break

    def dealer_turn(self, player_hand):
        """Handles the dealer's turn after the player interrupts."""
        dealer_hand = []
        while True:
            dealer_score = reduce(lambda x, y: x + y.value, dealer_hand, 0)
            if dealer_score >= 17:
                break
            dealer_hand.append(self.deck.cards.pop())

        # Show dealer's cards
        print("\nDealer's cards:")
        for card in dealer_hand:
            print(card.value, card.suit.name, card.rank.name)

        dealer_score = reduce(lambda x, y: x + y.value, dealer_hand, 0)
        player_score = reduce(lambda x, y: x + y.value, player_hand, 0)

        # Compare scores
        if dealer_score > 21 or dealer_score < player_score:
            print(f"You win! Dealer score: {dealer_score}, Your score: {player_score}.")
        elif dealer_score == player_score:
            print(f"It's a tie! Dealer score: {dealer_score}, Your score: {player_score}.")
        else:
            print(f"Dealer wins! Dealer score: {dealer_score}, Your score: {player_score}.")

    def deal(self) -> [Card]:
        """First deal must be 2 cards, others are 1 card."""

        if self.deck.cards is None or not self.deck.cards:
            raise ValueError("No cards in deck.")

        if self.__first_deal:
            self.__first_deal = False
            return [self.deck.cards.pop(), self.deck.cards.pop()]  # Deal 2 cards
        else:
            return [self.deck.cards.pop()]  # Deal 1 card

    def ask_restart(self):
        """Prompt the player to restart or exit."""
        while True:
            choice = input("Do you want to play again? (Y/N): ").strip().upper()
            if choice == 'Y':
                self.restart()
                return True
            elif choice == 'N':
                print("Thanks for playing!")
                return False
            else:
                print("Invalid input. Please press 'Y' to restart or 'N' to exit.")

    def restart(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.__first_deal = True