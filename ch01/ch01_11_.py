class Hand3:
    def __init__(self, *args, **kw):
        """
        1. 从已有的 Hand3 对象创建
        2. Hand3 对象的创建基于 Card 实例
        """
        if len(args) == 1 and isinstance(args[0], Hand3):
            other = args[0]
            self.dealer_card = other.dealer_card
            self.cards = other.cards
        else:
            dealer_card, *cards = args
            self.dealer_card = dealer_card
            self.cards = list(cards)
