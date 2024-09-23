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
    if os.path.exists(path):
        print("using path: " + path)
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)