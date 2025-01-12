from Suit import Suit
from Ranks import Rank

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        self._value = self._calculate_value()


    @property
    def value(self):
        return self._value


    def set_ace_value(self):
        value_to_set: int = 11
        print("What value do you want to set the ace to? (1 or 11): ")
        while True:
            try:
                new_value = int(input())
                if new_value == 1 or new_value == 11:
                    value_to_set = new_value
                else:
                    raise ValueError("Value must be 1 or 11")
                break
            except ValueError as error:
                print(error)
                continue

        self._value = value_to_set


    def _calculate_value(self):
        value_to_set: int = 0
        match self.rank:
            case Rank.JACK | Rank.QUEEN | Rank.KING:
                value_to_set = 10
            case _:
                if type(self.rank) is Rank:
                    value_to_set = self.rank.value
                else:
                    raise ValueError(f"Rank must be of type Rank, got {type(self.rank)} instead.")

        return value_to_set