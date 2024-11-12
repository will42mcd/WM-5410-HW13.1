# Code taken From: http://openbookproject.net/thinkcs/python/english3e/recursion.html
# Author: Peter Wentworth
# License: None listed
# Acessed on: 11/11/2024
# Changelog:
#   - added def koch_snowflake(t, order, size):

def koch(t, order, size):
    """
       Make turtle t draw a Koch fractal of 'order' and 'size'.
       Leave the turtle facing the same direction.
    """

    if order == 0:          # The base case is just a straight line
        t.forward(size)
        
    else:
        koch(t, order-1, size/3)   # Go 1/3 of the way
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch(t, order, size)
        t.right(120)