from aht.core.io.io_pin import IO_Pin
from aht.core.logging.log_decorators import LogFunction
from abc import ABC, abstractmethod

class IO_Base(ABC):
    """
    Base class for all IO devices
    """
    def __init__(self, name="io_device"):
        self.name = name

    @abstractmethod
    @LogFunction()
    def set_pin(self, pin : IO_Pin, state : IO_Pin.State):
        pass