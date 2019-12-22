import random
from .ch01_053 import card6
from .ch01_04_suit import Club, Diamond, Heart, Spade


class Deck3(list):
    def __init__(self, decks=1):
        super().__init__()
        for i in range(decks):
            # 调用 self.extend() 把多副牌加载到发牌机中
            self.extend(
                card6(r+1, s)
                for r in range(13)
                for s in (Club, Diamond, Heart, Spade)
            )
        random.shuffle(self)
        burn = random.randint(1, 52)
        for i in range(burn):
            self.pop()
