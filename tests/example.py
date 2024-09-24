
from aht import *
from app.config.defines import CFG_PATH
import logging

if __name__ == "__main__":
   # print(CFG_PATH)
    setup_logging(CFG_PATH, "logging_cfg.yml")
    crio = IO_Crio("newCrio")
    crio.set_pin(IO_Pin("crioPin"), IO_Pin.State.ACTIVE)

