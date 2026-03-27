import logging
import inspect


class logger_class:
    @staticmethod
    def get_logger():
        logger = logging.getLogger("OrangeHRM")
        logger.setLevel(logging.INFO)
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(funcName)s : %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(".\\Logs\\OrangeHRM.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger