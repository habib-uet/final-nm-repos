# Python3 code to implement
# Simpson's rule

# Given function to be
# integrated
from  math import *
def func(x,eq):
    x=x
    return eval(eq)


# Function to perform calculations
def calculate(lower_limit, upper_limit, interval_limit,eq ):
    
    interval_size = (float(upper_limit - lower_limit) / interval_limit)
    sum = func(lower_limit,eq) + func(upper_limit,eq);

    # Calculates value till integral limit
    for i in range(1, interval_limit ):
        if (i % 3 == 0):
            sum = sum + 2 * func(lower_limit + i * interval_size,eq)
        else:
            sum = sum + 3 * func(lower_limit + i * interval_size,eq)
    
    return ((float( 3 * interval_size) / 8 ) * sum )

# driver function

def mymain(a,b,eq,n):
    return calculate(a, b, n,eq)

# rounding the final answer to 6 decimal places

# This code is contributed by Saloni.
