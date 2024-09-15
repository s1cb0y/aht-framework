from aht.core.logger import *
from aht.core.log_function import *

from datetime import date
logger = AHTLogger(__file__).get_logger()
d1 = date.today().strftime("%d_%m_%Y")
file_handler = logging.FileHandler('log/'+d1+'_logfile.log')
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger_c = AHTLogger("testlogger", file_handler).get_logger()
logger_a = logging.getLogger("abc")
logger_b = logging.getLogger("asd")
logger_b.setLevel(logging.DEBUG)
class helper:
    @LogFunction(logger)
    def sum(self, a,b):
        return a+b


if __name__ == "__main__":
    h = helper()
    c = h.sum(3,3)
    logger_a.info("abc")
    logger_b.debug("asd")
    logger_c.info("asda")
