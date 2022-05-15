# Python3 program for implementation
# of Lagrange's Interpolation

# To represent a data point corresponding to x and y = f(x)
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# function to interpolate the given data points
# using Lagrange's formula
# xi -> corresponds to the new data point
# whose value is to be obtained
# n -> represents the number of known data points
def interpolate(f: list, xi: int, n: int) -> float:
    l=list()
    # Initialize result
    result = 0.0
    for i in range(n):

        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
                l.append(term)

        # Add current term to result
        result += term
        tem="Value of f {} is :".format(xi)+str(result)
        resulted={"result":tem,"terms":l}
    return resulted



def mymain(y,x,n,xp):
        print(x)
        f=list()
        for i in range(n):
                f.append(Data(x[i],y[i]))
        return  interpolate(f, xp, n)            
# Driver Code
