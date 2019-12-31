import sys
import yaml
import logging
from logging import config


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class Main:
    def __init__(self):
        pass

    def run(self):
        return 0


if __name__ == "__main__":
    with open('log_config.yaml', 'r', encoding='utf-8') as f:
        log_config = yaml.unsafe_load(f.read())
    config.dictConfig(log_config)
    try:
        application = Main()
        status = application.run()
    except Exception as e:
        logging.exception(e)
        status = 2
    finally:
        logging.shutdown()  # 注意这里
    sys.exit(status)
