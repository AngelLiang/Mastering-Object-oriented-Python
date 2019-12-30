import sys
import yaml
import logging


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class Main:
    def __init__(self):
        pass

    def run(self):
        return 0


if __name__ == "__main__":
    logging.config.dictConfig(yaml.load('log_config.yaml'))
    try:
        application = Main()
        status = application.run()
    except Exception as e:
        logging.exception(e)
        status = 2
    finally:
        logging.stutdown()  # 注意这里
    sys.exit(status)
