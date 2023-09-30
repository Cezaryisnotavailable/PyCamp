import logging
from datetime import datetime


def get_logger():
    # Define the log file name with a timestamp
    log_file = f"password_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create a file handler to save log messages to the specified file
    file_handler = logging.FileHandler(log_file)

    # Create a formatter to include date and time in the log messages
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger



