"""
>>> p = Player(1, 2, 3)
"""
import logging


class Player:
    def __init__(self, bet, strategy, stake):
        self.logger = logging.getLogger(self.__class__.__qualname__)
        self.logger.debug('init bet {0}, strategy {1}, stake {2}'.format(
            bet, strategy, stake))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
