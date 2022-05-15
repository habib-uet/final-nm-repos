# Python3 program to implement Boole's Rule
# on the given function

# In order to represent the implementation,
# a function f(x) = 1/(1 + x) is considered
# in this program

# Function to return the value of f(x)
# for the given value of x
from  math import *
def y(x,eq):
    x=x
    return eval(eq)

# Function to computes the integrand of y
# at the given intervals of x with
# step size h and the initial limit a
# and final limit b
def BooleRule(a, b,eq,n):
	
	# Number of intervals

	# Computing the step size
	h = ((b - a) / n)
	sum = 0

	# Substituing a = 0, b = 4 and h = 1
	bl = (7 * y(a,eq) + 32 * y(a + h,eq) + 12 *
		y(a + 2 * h,eq)+32 * y(a + 3 * h,eq)+7 *
		y(a + 4 * h,eq))* 2 * h / 45

	sum = sum + bl
	return sum

# Driver code
def mymain(a,b,eq,n):
	lowlimit = a
	upplimit = b
	return "f(x) =" + str(round(BooleRule(a, b,eq,n),4))

# This code is contributed by Surendra_Gangwar
