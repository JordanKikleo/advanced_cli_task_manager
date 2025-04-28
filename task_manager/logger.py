import logging
import os
from task_manager.config import Config

config = Config()
config.load_config()

def setup_logger(log_file=None):
    if log_file is None:
        log_file = config.log_file
    
    log_directory = os.path.dirname(log_file)
    if log_directory and not os.path.exists(log_directory):
        os.makedirs(log_directory)
    
    logger = logging.getLogger("task_manager")
    logger.setLevel(getattr(logging, config.log_level))
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger 