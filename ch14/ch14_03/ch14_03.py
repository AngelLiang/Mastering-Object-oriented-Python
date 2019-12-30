"""
>>> main = Main()
>>> main.run()
"""

import sys
import logging
from collections import Counter

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class Main:
    def __init__(self):
        self.balance = Counter()
        self.log = logging.getLogger(self.__class__.__qualname__)

    def run(self):
        self.log.info('start')

        # Some processing
        self.balance['count'] += 1
        self.balance['balance'] += 3.14

        self.log.info('Counts {0}'.format(self.balance))

        for k in self.balance:
            self.log.info('{0:.<16s} {1:n}'.format(k, self.balance[k]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
