import logging


def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")
    file_handler = logging.FileHandler("logs/app.log", mode="a",  encoding="utf-8")
    logger.addHandler(file_handler)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    file_handler.setFormatter(formatter)
