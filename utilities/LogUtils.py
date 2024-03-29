import logging
import inspect
import os
from tests.BaseTest import BaseTest


class Logger:
    base = BaseTest()

    def logger_setup(self, loglevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(loglevel)
        # logfile_name = self.base.generate_timestamp()
        filename = os.getcwd() + "//automation.log"
        fileHandler = logging.FileHandler(filename, mode='a')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s",
                                      datefmt='%d-%m-%Y %H:%M:%S')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        return logger
