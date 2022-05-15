# Python code for simpson's 1 / 3 rule
from  math import *


def eval_polynomial(equation, x_value):
        x=x_value
        return eval(equation)
# Function to calculate f(x)
# Function for approximate integral
def simpsons_( ll, ul, n,eq ):
    # Calculating the value of h
    h = ( ul - ll )/n
    # List for storing value of x and f(x)
    x = list()
    fx = list()
    # Calculating values of x and f(x)
    i = 0
    while i<= n:
        x.append(ll + i * h)
        fx.append(float(eval_polynomial(eq,x[i])))
        i += 1

    # Calculating result
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res


def mymain(a,b,eq,n):
    return  str( simpsons_(a, b, n,eq))

    		

