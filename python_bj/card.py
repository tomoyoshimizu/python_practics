import random

class Deck:
    def __init__(self, cards = []):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)


class Card:
    def __init__(self, suit, rank):
        self._suit = suit
        self._rank = rank
        self.is_open = False

    @property
    def info(self):
        mark = {
            "spades": "♠",
            "hearts": "♥",
            "diams":  "♦",
            "clubs":  "♣"
        }
        if self.is_open:
            return mark[self._suit] + str(self._rank)
        else:
            return '???'

    @property
    def rank(self):
        return self._rank if self.is_open else None
