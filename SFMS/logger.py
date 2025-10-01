import logging
import os
from enum import Enum, auto

#Logger config
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "app.log")

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')

class LogLevel(Enum):
    INFO = auto()
    WARNING = auto()
    ERROR = auto()
    DEBUG = auto()

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def writelog(self, message, level = LogLevel.INFO):
        if level == LogLevel.INFO:
            self.logger.info(message)
        elif level == LogLevel.WARNING:
            self.logger.warning(message)
        elif level == LogLevel.ERROR:
            self.logger.error(message)
        elif level == LogLevel.DEBUG:
            self.logger.debug(message)
        else:
            self.logger.info(message)