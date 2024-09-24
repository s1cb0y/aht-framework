import os
import logging.config
import yaml


def setup_logging(
    default_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging_cfg.yml'),
    default_level = logging.INFO,
    env_key='LOG_CFG' # env variable can be used to define config yml path
):
    """
    Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
        print("using ENV VAR to setup logging")
    if os.path.exists(path):
        print("using logging config path: " + path)
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        print("using default config")
        logging.basicConfig(level=default_level)