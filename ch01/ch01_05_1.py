from .ch01_03_card import AceCard, NumberCard, FaceCard
from .ch01_04_suit import Club, Diamond, Heart, Spade


def card2(rank, suit):
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank <= 11:
        return NumberCard(str(rank), suit)
    else:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)


deck2 = [
    card2(rank, suit)
    for rank in range(1, 14)
    for suit in (Club, Diamond, Heart, Spade)
]
