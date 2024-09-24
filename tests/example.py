
from aht import *
from config.setup_env import *
import logging


if __name__ == "__main__":
    setup_test_env()

    crio = IO_Crio("newCrio")
    crio.set_pin(IO_Pin("crioPin"), IO_Pin.State.ACTIVE)

