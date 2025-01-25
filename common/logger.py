import logging


def info(msg):
    logger = logging.getLogger('common')
    logger.info(msg)

def error(msg):
    logger = logging.getLogger('common')
    logger.error(msg)