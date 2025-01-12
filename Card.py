from Suit import Suit
from Ranks import Rank

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        self._value = 0

    @property
    def value(self):
        match self.rank:
            case Rank.ACE:
                print("11 or 1?: ")
                while True:
                    try:
                        new_value = int(input())
                        if new_value == 1 or new_value == 11:
                            self._value = new_value
                        else:
                            raise ValueError("Value must be 1 or 11")
                        break
                    except ValueError as error:
                        print(error)
                        continue
            case Rank.JACK | Rank.QUEEN | Rank.KING:
                self._value = 10
            case _:
                if type(self.rank) is Rank:
                    self._value = self.rank.value
                else:
                    raise ValueError(f"Rank must be of type Rank, got {type(self.rank)} instead.")

        return self._value