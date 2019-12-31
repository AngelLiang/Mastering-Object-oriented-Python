"""
>>> otts = OneThreeTwoSix()
"""
import atexit
import logging
from logging.config import dictConfig
import yaml

with open('ch14_03_01.yaml', 'r', encoding='utf-8') as f:
    log_config = yaml.unsafe_load(f.read())
    dictConfig(log_config)


def logged(class_):
    """为 class_ 创建一个 logger 属性"""
    class_.logger = logging.getLogger(class_.__qualname__)
    return class_


class BettingStrategy:

    def bet(self):
        raise NotImplementedError("No bet method")

    def record_win(self) -> None:
        pass

    def record_loss(self) -> None:
        pass


@logged
class OneThreeTwoSix(BettingStrategy):
    def __init__(self):
        self.wins = 0

    def _state(self):
        return dict(wins=self.wins)

    def bet(self) -> int:
        bet = {0: 1, 1: 3, 2: 2, 3: 6}[self.wins % 4]
        self.logger.debug(f"Bet {self._state()}; based on {bet}")
        return bet

    def record_win(self) -> None:
        self.wins += 1
        self.logger.debug(f"Win: {self._state()}")

    def record_loss(self) -> None:
        self.wins = 0
        self.logger.debug(f"Loss: {self._state()}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
