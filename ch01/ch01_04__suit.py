from .ch01_03_card import AceCard, NumberCard


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


Club, Diamond, Heart, Spade = Suit('Club', '♣'), Suit(
    'Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')

cards = [AceCard('A', Spade), NumberCard('2', Spade), NumberCard('3', Spade)]
