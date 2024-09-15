import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler(sys.stdout)
                    ])
class AHTLogger:

    def __init__(self, name=None, *handlers) -> None:
        self.logger = logging.getLogger(name)
        for h in handlers:
            self.logger.addHandler(h)

    def get_logger(self):
        return self.logger

def get_default_logger():
    return AHTLogger()