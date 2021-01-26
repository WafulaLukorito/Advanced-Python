
import logging
#*Refer to Python Documentation!

#* Go to https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/10-Logging.ipynb

#* Refer to https://www.geeksforgeeks.org/logging-in-python/

# Logging in Python
# Last Updated: 08-02-2018
# Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, debugging and running. If you don’t have any logging record and your program crashes, there are very little chances that you detect the cause of the problem. And if you detect the cause, it will consume a lot of time. With logging, you can leave a trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem.
# There are a number of situations like if you are expecting an integer, you have been given a float and you can a cloud API, the service is down for maintenance and much more. Such problems are out of control and are hard to determine.

# Why Printing is not a good option?

# Some developers use the concept of printing the statements to validate if the statements are executed correctly or some error has occurred. But printing is not a good idea. It may solve your issues for simple scripts but for complex scripts, printing approach will fail.

# Python has a built-in module logging which allows writing status messages to a file or any other output streams. The file can contain the information on which part of the code is executed and what problems have been arisen.

# Levels of Log Message



# There are two built-in levels of the log message.

# Debug : These are used to give Detailed information, typically of interest only when diagnosing problems.
# Info : These are used to Confirm that things are working as expected
# Warning : These are used an indication that something unexpected happened, or indicative of some problem in the near future
# Error : This tells that due to a more serious problem, the software has not been able to perform some function
# Critical : This tells serious error, indicating that the program itself may be unable to continue running
# If required, developers have the option to create more levels but these are sufficient enough to handle every possible situation. Each built-in level has been assigned its numeric value.

