import logging

# set name of the logger module
# logger = logging.getLogger(__name__)
# #logger.propagate = False
# logger.info("Hello from info")

# # *The logger module is a singleton, which means that it will be created only once. If you create a logger with the same name, it will return the same logger object. This is useful when you want to use the same logger in multiple modules.

# # *The propagate attribute is set to True by default. This means that the messages will be passed to the parent logger. If you set it to False, the messages will not be passed to the parent logger.

# * Log handlers are used to send the log messages to the desired output destination via http or otherwise. The logging module has a number of handlers that can be used to send the messages to different output destinations. The most commonly used handlers are StreamHandler and FileHandler.

# *The StreamHandler sends the messages to the output stream like the console or terminal. The FileHandler sends the messages to a file.

logger = logging.getLogger(__name__)

# create a file handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# set the log level for the handlers and format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

stream_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add the formatter to the handlers
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)

# add the handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning')
logger.error('This is an error')

# * File Handlers
# *The FileHandler sends the messages to a file. The file can be a text file or a binary file. The FileHandler can be used to send the messages to a file. File name e.g, "logging.conf"
