
class BettingStrategy:
    def bet(self):
        """在基类函数中抛出异常，用以标识要在子类中提供实现"""
        raise NotImplementedError('No bet method')

    def record_win(self):
        pass

    def record_loss(self):
        pass


class Flat(BettingStrategy):
    def bet(self):
        return 1
