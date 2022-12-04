# -*- coding: ascii -*-
import helper
import logging
# *Refer to Python Documentation!

# * Go to https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/10-Logging.ipynb

# * Refer to https://www.geeksforgeeks.org/logging-in-python/

# Logging in Python
# Last Updated: 08-02-2018
# """
# Logging is a way of tracking events that happen when some software runs. The software developer adds logging calls to their code to indicate that certain events have occurred.

# Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, debugging and running. If you dont have any logging record and your program crashes, there are very little chances that you detect the cause of the problem. And if you detect the cause, it will consume a lot of time. With logging, you can leave a trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem.

# There are a number of situations like if you are expecting an integer, you have been given a float and you call a cloud API, the service is down for maintenance and much more. Such problems are out of control and are hard to determine.

# # Why Printing is not a good option?

# # Some developers use the concept of printing the statements to validate if the statements are executed correctly or some error has occurred. But printing is not a good idea. It may solve your issues for simple scripts but for complex scripts, printing approach will fail.


# # Python has a built-in module logging which allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have been arisen.

# # Levels of Log Message


# # There are two built-in levels of the log message.

# # Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
# # Info : These are used to Confirm that things are working as expected
# # Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future
# # Error : This tells that due to a more serious problem, the software has not been able to perform some function
# # Critical : This tells serious error, indicating that the program itself may be unable to continue running
# # If required, developers have the option to create more levels but these are sufficient enough to handle every possible situation. Each built-in level has been assigned its numeric value.

# """
#import logging
#logging.debug('This is a debug message')
# logging.info('This is an info message')

# # * The default level is WARNING, which means that only messages of this level and above will be tracked or printed, unless the logging level is set to something else.

# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# import logging

# Log Levels

# *How you want the messages to be displayed. Check the documentation for more details. https://docs.python.org/3/library/logging.html#logging-levels
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')


# *It is best to create your own module for logging and import it in your other modules. This way, you can control the logging level from a single place.


# *You can also use the logging module to log messages to a file. This is useful when you want to keep a record of the messages that are being logged.

# * File Handlers
# *The FileHandler sends the messages to a file. The file can be a text file or a binary file. The FileHandler can be used to send the messages to a file. File name e.g, "logging.conf"

# import logging
# import logging.config

# logging.config.fileConfig('logging.conf')

# # create logger
# logger = logging.getLogger('simpleExample')

# logging.debug('This is a debug message')


# * Dictionary Configurations
# * The dictionary configuration is a more flexible way of configuring the logging module. It allows you to configure the logging module from a dictionary. The dictionary can be created in the code or read from a file.


# Capturing Stack Traces
# * The logging module can also capture the stack traces. This is useful when you want to know the sequence of function calls that led to the error. The stack trace can be captured by setting the exc_info parameter to True.

# * The stack trace is captured only if the level of the message is ERROR or higher.

# import logging

# try:
#     a = [1, 2, 3]
#     val = a[3]
# except IndexError as e:
#     logging.error("Exception occurred", exc_info=True)


# * Rotating File Handlers
# * The RotatingFileHandler is used to send the messages to a file. The file can be a text file or a binary file. The RotatingFileHandler can be used to send the messages to a file. The file is rotated when it reaches a certain size. The backupCount parameter specifies the number of files to which the logs are rotated. The default value is 0, which means that the file is not rotated.

# import logging
# from logging.handlers import RotatingFileHandler

# # create logger
# logger = logging.getLogger('__name__')
# logger.setLevel(logging.INFO)

# # roll over after 2KB, and keep backup logs as app.log.1, app.log.2, etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info('This is a test message')

# *Timed Rotating File Handlers
# *The TimedRotatingFileHadnler is used when app will be running for a long time. The file is rotated at certain timed intervals. The when parameter specifies the interval. The interval can be specified in seconds, minutes, hours, days, weeks, or midnights. The interval can be specified by using the S, M, H, D, W, or midnight. The backupCount parameter specifies the number of files to which the logs are rotated. The default value is 0, which means that the file is not rotated.


# import logging
# import time
# from logging.handlers import TimedRotatingFileHandler

# # create logger
# logger = logging.getLogger('__name__')
# logger.setLevel(logging.INFO)

# # rotate log file every 5 seconds
# handler = TimedRotatingFileHandler(
#     'timed_test.log', when='s', interval=5, backupCount=5)
# logger.addHandler(handler)

# for _ in range(6):
#     logger.info('This is a test message')
#     time.sleep(6)

# * In production, particularly when dealing with micro-services apps, it is recommended to use python-json-logger. It is a simple library that allows you to log in JSON format. This is useful when you want to send the logs to a centralized logging system like ELK stack or Splunk. The logs can be easily parsed and analyzed. The library can be installed using pip. pip install python-json-logger.  The following code shows how to use the library to log in JSON format. Https://github.com/madzak/python-json-logger

import logging
from pythonjsonlogger import jsonlogger
