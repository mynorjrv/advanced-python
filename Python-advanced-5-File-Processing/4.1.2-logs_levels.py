import logging

logging.basicConfig()

# __name__ is the current module name
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')