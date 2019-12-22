"""如何把初始化职责分发到各自的子类中"""


class Card:
    pass


class NumberCard(Card):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.hard = self.soft = rank


class AceCard(Card):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = 'A'
        self.hard, self.soft = 1, 11


class FaceCard(Card):
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        self.hard = self.soft = 10
