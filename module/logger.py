import logging
from logging.handlers import RotatingFileHandler

class Logger:
    _instance = None

    def __new__(cls, log_file='app.log'):
        
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._initialize_logger(log_file)
        return cls._instance

    @classmethod
    def _initialize_logger(cls, log_file):
        cls.logger = logging.getLogger('AppLogger')
        cls.logger.setLevel(logging.DEBUG)

        file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5) 
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        cls.logger.addHandler(file_handler)

    def set_log_level(self, level):
        level_dict = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        self.logger.setLevel(level_dict.get(level, logging.DEBUG))

    def set_log_format(self, format_string):
        formatter = logging.Formatter(format_string)
        for handler in self.logger.handlers:
            handler.setFormatter(formatter)

    def debug(self, message, extra=None):
        self.logger.debug(message, extra=extra if extra else {})

    def info(self, message, extra=None):
        self.logger.info(message, extra=extra if extra else {})

    def warning(self, message, extra=None):
        self.logger.warning(message, extra=extra if extra else {})

    def error(self, message, extra=None):
        self.logger.error(message, extra=extra if extra else {})

    def critical(self, message, extra=None):
        self.logger.critical(message, extra=extra if extra else {})
