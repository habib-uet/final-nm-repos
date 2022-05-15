# Python3 program to Implement Weedle's Rule

# A sample function f(x) = 1/(1+x^2)
from  math import *
def y(x,eq):
    x=x
    return eval(eq)

# Function to find the integral value
# of f(x) with step size h, with
# initial lower limit and upper limit
# a and b
def WeedleRule(a, b,eq,n):
	
	# Find step size h
	h = (b - a) / n;
	
	# To store the final sum
	sum = 0;
	
	# Find sum using Weedle's Formula
	sum = sum + (((3 * h) / 10) * (y(a,eq)
			+ y(a + 2 * h,eq)
			+ 5 * y(a + h,eq)
			+ 6 * y(a + 3 * h,eq)
			+ y(a + 4 * h,eq)
			+ 5 * y(a + 5 * h,eq)
			+ y(a + 6 * h,eq)));

	# Return the final sum
	return sum;

# Driver Code
def mymain(a,b,eq,n):
		num = WeedleRule(a, b,eq,n);
		return "f(x) = "+ "{0:.6f}".format(num);



# This code is contributed by sapnasingh4991
