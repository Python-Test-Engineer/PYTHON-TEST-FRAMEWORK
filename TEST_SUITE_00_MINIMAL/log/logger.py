"""Sample logger"""


import logging


def get_custom_logger(name: str, log_file: str = "./log/app.log"):
    """Set up logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create a formatter that includes the desired information
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)8s] [%(name)s] %(message)s (%(filename)s:%(lineno)s)",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create a stream handler and set the formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Create a file handler and set the formatter
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


# Example usage
if __name__ == "__main__":
    logger = get_custom_logger(__name__)

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
