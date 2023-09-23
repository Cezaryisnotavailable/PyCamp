import logging

# Create a logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.ERROR)

# Create a file handler
file_handler = logging.FileHandler('my_log.txt')

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log some messages
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')
logger.critical('Critical message')
