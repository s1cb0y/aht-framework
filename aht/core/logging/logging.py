import os
import logging.config
from config.defines import *
import yaml

def setup_logging(
    default_path = os.path.join(CFG_PATH, 'logging_cfg.yml'),
    default_level = logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)