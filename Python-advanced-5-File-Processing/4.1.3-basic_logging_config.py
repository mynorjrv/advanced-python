import logging

# https://docs.python.org/3/library/logging.html#logrecord-attributes
FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logging.basicConfig(
    level=logging.CRITICAL, 
    filename='prod.log', 
    filemode='a',
    format=FORMAT
)

logger = logging.getLogger()

logger.critical('Your CRITICAL message')
logger.error('Your ERROR message')
logger.warning('Your WARNING message')
logger.info('Your INFO message')
logger.debug('Your DEBUG message')