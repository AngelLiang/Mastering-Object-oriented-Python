"""定义指向多个目标输出的handler
"""

import yaml
import logging
from logging import config

with open('log_config.yaml', 'r', encoding='utf-8') as f:
    log_config = yaml.unsafe_load(f.read())
config.dictConfig(log_config)

verbose = logging.getLogger('verbose.example.ComeClass')
audit = logging.getLogger('audit.example.ComeClass')
verbose.info('Verbose information')
audit.info('Audit record with before and after')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
