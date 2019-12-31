"""
>>> main = Main()
>>> main.run()
"""

import logging
from logging.config import dictConfig
from collections import Counter
import yaml


logging.basicConfig(level=logging.INFO)
with open('ch14_03.yaml', 'r', encoding='utf-8') as f:
    log_config = yaml.unsafe_load(f.read())
    # print(log_config)
    dictConfig(log_config)


class Main:
    def __init__(self):
        self.balance = Counter()
        self.log = logging.getLogger(self.__class__.__qualname__)

    def run(self):
        self.log.info('Start')

        # Some processing
        self.balance['count'] += 1
        self.balance['balance'] += 3.14

        self.log.info('Counts {0}'.format(self.balance))

        for k in self.balance:
            self.log.info('{0:.<16s} {1:n}'.format(k, self.balance[k]))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
