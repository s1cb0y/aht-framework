from aht.core.io.io_base import IO_Base
from aht.core.io.io_pin import IO_Pin
import logging

class IO_Crio(IO_Base):
    def __init__(self, name:str="IO_Crio"):
        super().__init__(name)
        self.logger = logging.getLogger(__name__)

    def set_pin(self, pin : IO_Pin, state : IO_Pin.State):
        self.logger.debug("set pin {} to state {}".format(pin.get_name(), state))