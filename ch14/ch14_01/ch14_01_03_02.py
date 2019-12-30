import sys
import yaml
import logging
import atexit


logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


class Main:
    def __init__(self):
        pass

    def run(self):
        return 0


if __name__ == "__main__":
    logging.config.dictConfig(yaml.load('log_config.yaml'))
    # 用atexit handle来关闭logging
    atexit.register(logging.shutdown)
    try:
        application = Main()
        status = application.run()
    except Exception as e:
        logging.exception(e)
        status = 2
    sys.exit(status)
