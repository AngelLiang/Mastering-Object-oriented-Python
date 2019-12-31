"""Loggers的默认行为会将一条日志记录从命名的Logger一直往上经过所有父级Loggers
传到根Logger。我们可以在更底层的Loggers中包含一些特殊的行为，但是需要在根Logge中
定义所有Loggers的默认行为。

由于日志记录的传播性，根日志记录器也需要处理来自我们定义的底层Loggers的日志记录。
如果子日志记录器定义了输出并且允许传播。当子日志记录器生成输出时，如果我们想要避免重复，
我们必须关闭底层日志记录器的传播特性。
"""

import yaml
import logging
from logging import config

with open('ch14_01_07.yaml', 'r', encoding='utf-8') as f:
    log_config = yaml.unsafe_load(f.read())
config.dictConfig(log_config)

verbose = logging.getLogger('verbose.example.ComeClass')
audit = logging.getLogger('audit.example.ComeClass')
verbose.info('Verbose information')
audit.info('Audit record with before and after')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
