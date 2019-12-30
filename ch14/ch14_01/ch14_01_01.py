"""
>>> p = Player(1, 2, 3)
"""
import logging


def logged(class_):
    """为class_创建一个logger属性"""
    class_.logger = logging.getLogger(class_.__qualname__)
    return class_


@logged
class Player:
    def __init__(self, bet, strategy, stake):
        self.logger.debug('init bet {0}, strategy {1}, stake {2}'.format(
            bet, strategy, stake))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
