import logging
import inspect

from tests.BaseTest import BaseTest


class Logger:
    base = BaseTest()

    def logger_setup(self, loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        # logfile_name = self.base.generate_timestamp()
        fileHandler = logging.FileHandler(f".//logs//automation.log", mode='a')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s",
                                      datefmt='%d-%m-%Y %H:%M:%S')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
