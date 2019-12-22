from .ch01_03_card import AceCard, NumberCard, FaceCard
from .ch01_04_suit import Club, Diamond, Heart, Spade


def card3(rank, suit):
    """没有使用映射Card工厂类的实现"""
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank <= 11:
        return NumberCard(str(rank), suit)
    elif rank == 11:
        return FaceCard('J', suit)
    elif rank == 12:
        return FaceCard('Q', suit)
    elif rank == 13:
        return FaceCard('K', suit)
    else:
        raise Exception('Rank out of range')


deck3 = [
    card3(rank, suit)
    for rank in range(1, 14)
    for suit in (Club, Diamond, Heart, Spade)
]
