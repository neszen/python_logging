"""
Internal Module that handles Logging
"""
import logging
import sys
from logging.handlers import RotatingFileHandler


FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = 'helper.log'

def get_console_handler():
   """
   Function to create and return a console handler.
   The console handler outputs logs to the terminal.
   """
   console_handler = logging.StreamHandler(sys.stdout)
   console_handler.setFormatter(FORMATTER)
   return console_handler

def get_file_handler():
   """
   Function to create and return a file handler.
   The file handler outputs logs to a file and rotates the file when it exceeds 10 MB.
   """
   file_handler = RotatingFileHandler(LOG_FILE, mode="a", maxBytes=1024, backupCount=5)
   file_handler.setFormatter(FORMATTER)
   return file_handler

def get_logger(logger_name):
   """
   Function to create and configure a logger.
   This logger outputs logs to both the console and a file.
   """
   logger = logging.getLogger(logger_name)
   logger.setLevel(logging.DEBUG) 
   logger.addHandler(get_console_handler())
   logger.addHandler(get_file_handler())
   logger.propagate = False
   return logger



log = get_logger("loggy")
log.debug("This is a debug message")
log.info("This is an info message")
log.warning("This is a warning message")
log.error("This is an error message")
log.critical("This is a critical message")






