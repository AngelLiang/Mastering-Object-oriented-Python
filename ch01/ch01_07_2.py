import random
from .ch01_053 import card6
from .ch01_04_suit import Club, Diamond, Heart, Spade


class Deck2(list):
    def __init__(self):
        super().__init__(
            card6(r+1, s)
            for r in range(13)
            for s in (Club, Diamond, Heart, Spade)
        )
        random.shuffle(self)
