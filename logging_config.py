import logging

def setup_logger(name="QnA", format="%(asctime)s - %(name)s - %(levelname)s - %(filename)s - Line: %(lineno)d - %(message)s"):
    logger = logging.getLogger("QnA")
    if not logger.handlers:
        formatter = logging.Formatter('%(asctime)s - %(filename)s - line %(lineno)d - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

logger = setup_logger()