"""
Purpose: Illustrate basic expresssions and operators in Python.

Author: Sarah DeConink

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.
 
"""

from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)

# Declare some variables 
# TODO: Try changing the values of these variables
# TODO: Add some new variables and calculate the area of a rectangle ()
triangle_base = 7
triangle_height = 3
i = 89
j = 32
a = 1.9
b = 2.1
c = 3.5

# Try some operators (multiply, divide, add, subtract)
triangle_area = triangle_base * triangle_height / 2
sum = a + b
sum2 = c + b
product = j * a
quotient = i / c
difference = i - j

# Log some information using f-strings (formatted strings)
logger.info(f"Given base={triangle_base} and height={triangle_height}, the triangle area = {triangle_area}")
logger.info(f"Given a={a} and b={b}, the sum = {sum}")
logger.info(f"Given c={c} and b={b}, the sum2 = {sum2}")
logger.info(f"Given j={j} and a={a}, the product = {product}")
logger.info(f"Given i={i} and c={c}, the quotient = {quotient:.2f}")
logger.info(f"Given i={i} and j={j}, the difference = {difference}")


# Use built-in open() function to read the log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
