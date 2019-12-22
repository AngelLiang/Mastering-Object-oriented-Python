from functools import partial

from .ch01_03_card import AceCard, NumberCard, FaceCard
from .ch01_04_suit import Club, Diamond, Heart, Spade


def card4(rank, suit):
    """使用映射实现的版本"""
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
              13: FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)


def card5(rank, suit):
    """并行映射"""
    class_ = {1: AceCard, 11: FaceCard, 12: FaceCard,
              13: FaceCard}.get(rank, NumberCard)
    rank_str = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}.get(
        rank, str(rank))
    return class_(rank_str, suit)


def card6(rank, suit):
    """映射到一个牌面值的元组"""
    class_, rank_str = {
        1: (AceCard, 'A'),
        11: (FaceCard, 'J'),
        12: (FaceCard, 'Q'),
        13: (FaceCard, 'K'),
    }.get(rank, (NumberCard, str(rank)))
    return class_(rank_str, suit)


def card7(rank, suit):
    """partial映射"""
    part_class = {
        1: partial(AceCard, 'A'),
        11: partial(AceCard, 'J'),
        12: partial(AceCard, 'Q'),
        13: partial(AceCard, 'K'),
    }.get(rank, partial(NumberCard, str(rank)))
    return part_class(suit)


class CardFactory:
    def rank(self, rank):
        self.class_, self.rank_str = {
            1: (AceCard, 'A'),
            11: (FaceCard, 'J'),
            12: (FaceCard, 'Q'),
            13: (FaceCard, 'K'),
        }.get(rank, (NumberCard, str(rank)))
        return self

    def suit(self, suit):
        return self.class_(self.rank_str, suit)


card8 = CardFactory()
deck8 = [
    card8.rank(r+1).suit(s)
    for r in range(13)
    for s in (Club, Diamond, Heart, Spade)
]
