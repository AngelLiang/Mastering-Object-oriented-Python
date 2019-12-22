from .ch01_07_1 import Deck
from .ch01_08 import Hand2


class Table:
    def __init__(self):
        self.deck = Deck()

    def place_bet(self, amount):
        print('Bet', amount)

    def get_hand(self):
        d = self.deck
        try:
            self.hand = Hand2(d.pop(), d.pop(), d.pop())
            self.hole_card = d.pop()
        except IndexError:
            self.deck = Deck()
            return self.get_hand()
        print('Deal', self.hand)
        return self.hand

    def can_insure(self, hand):
        return hand.dealer_card.insure
