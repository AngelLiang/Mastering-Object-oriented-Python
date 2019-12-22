import abc
from abc import abstractmethod


class BettingStrategy2(metaclass=abc.ABCMeta):
    """
    1. 阻止对抽象基类 BettingStrategy2 的实例化
    2. 任何没有提供 bet() 方法实现的子类也是不能被实例化的。
    """

    @abstractmethod
    def bet(self):
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass


class Flat2(BettingStrategy2):
    def bet(self):
        return super().bet()
