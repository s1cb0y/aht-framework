from aht.core.logging.logging import setup_logging
import os

CFG_PATH = os.path.dirname(os.path.abspath(__file__))

def setup_test_env():
    """sets up the test environment"""
    setup_logging(CFG_PATH + "/logging_cfg.yml")