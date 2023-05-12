"""
Purpose: This program asks for sales data and gives some descriptive statistics.
It also makes employment and inventory recommendations.

Author: Sarah DeConink

"""

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

print("Weekly Ice Cream Statistics")


# Get sales information from the user
num_1 = int(input("How many single scoop ice cream cones were sold this week: "))
num_2 = int(input("How many double scoop ice cream cones were sold this week: "))
num_3 = int(input("How many triple scoop ice cream cones were sold this week: "))

# Create a list of data
number_list = [num_1, num_2, num_3]


# Calculate several statistics
total_sales = sum(number_list)
count_1 = len(number_list)
average = total_sales / count_1
nice_average = round(average)
product_scoops = num_1 + 2 * num_2 + 3 * num_3
smallest = min(number_list)
largest = max(number_list)


# Log the results
logger.info(f"This week we sold {num_1} single scoop cones, {num_2} double scoop cones, \
and {num_3} triple scoop cones, for a total of {total_sales} cones.")
logger.info(f"The types of cones sold range from {smallest} to {largest}, while the average \
of all types sold was {nice_average}.")
logger.info(f"The total number of ice cream scoops served was {product_scoops}")


# Recommendations based on results
if total_sales >= 1000:
    logger.info("Hire two new ice cream scoopers.")
elif total_sales >= 500:
    logger.info("Hire one new ice cream scooper")
elif total_sales >= 200:
    logger.info("No employment changes are needed.")
else:
    logger.info("Fire one ice cream scooper.")

if product_scoops >= 400:
    logger.info("Check ice cream tub inventory.")


# Use built-in open() function to read log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())