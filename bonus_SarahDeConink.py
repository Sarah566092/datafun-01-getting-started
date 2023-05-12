"""
Purpose: This program imports a statistics module from the Python Standard Library
and generates descriptive statistics on a list of values.

Author: Sarah DeConink

"""

import statistics

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# List of Data
data_1 = [3,90,2,5,40,28,4,6,11,13,28,97,35,44,2,3,5,66,93]

# Descriptive Statistics functions
mean_data_1 = statistics.mean(data_1)
mode_data_1 = statistics.mode(data_1)
median_data_1 = statistics.median(data_1)

# Log results
logger.info(f"The mean of the data is {round(mean_data_1,2)}")
logger.info(f"The mode of the data is {mode_data_1}")
logger.info(f"The median of the data is {median_data_1}")

# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())