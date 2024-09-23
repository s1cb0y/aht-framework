
from aht import *
from app.config.defines import CFG_PATH

if __name__ == "__main__":

    setup_logging(os.path.join(CFG_PATH, "logging_cfg.yml"))

    crio = IO_Crio("newCrio")
    crio.set_pin(IO_Pin("crioPin"), IO_Pin.State.ACTIVE)

