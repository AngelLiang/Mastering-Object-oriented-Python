from .ch01_07_1 import Deck


class Hand:
    def __init__(self, dealer_card):
        self.dealer_card = dealer_card
        self.cards = []

    def hard_total(self):
        return sum(c.hard for c in self.cards)

    def soft_total(self):
        return sum(c.soft for c in self.cards)


d = Deck()
h = Hand(d.pop())
h.cards.append(d.pop())
h.cards.append(d.pop())


class Hand2:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def hard_total(self):
        return sum(c.hard for c in self.cards)

    def soft_total(self):
        return sum(c.soft for c in self.cards)


d = Deck()
h = Hand2(d.pop())
h.cards.append(d.pop())
h.cards.append(d.pop())

# 使用 *cards 参数一次加载多张牌
d = Deck()
h = Hand2(d.pop(), d.pop(), d.pop())
