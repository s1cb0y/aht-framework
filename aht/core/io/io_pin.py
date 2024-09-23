from enum import Enum
class IO_Pin:
    """
    Base class for all io pins used by classes derived by 'IO'
    """
    class State(Enum):
        """
        Enum class for io pin states
        """
        INACTIVE=1
        ACTIVE=2
        UNDEF=3
    class Polarity(Enum):
        """
        Enum class for io pin polarity
        """
        ACTIVE_HIGH=1
        ACTIVE_LOW=2

    def __init__(self, name:str="io_pin", polarity=Polarity.ACTIVE_HIGH):
        self.name = name
        self.polarity = polarity

    def get_name(self) -> str:
        return self.name;

    def get_polarity(self):
        return self.polarity