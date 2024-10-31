import os
import logging

def get_logger(name="QnA", log_format='%(asctime)s - %(filename)s - line %(lineno)d - %(levelname)s - %(message)s'):
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get("LOG_LEVEL", "info"))
    formatter = logging.Formatter(log_format)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger