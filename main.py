from aht.core.logging.logging import *
from aht.core.logging.log_decorators import *


class helper:
    @LogFunction()
    def sum(self, a,b):
        return a+b


if __name__ == "__main__":
    setup_logging()
    h = helper()
    c = h.sum(3,3)

