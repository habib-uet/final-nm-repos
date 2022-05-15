# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"
def dydx(x, y,eq):
    x=x
    y=y
    return eval(eq)

# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(x0, y0, x, h,eq):
    # Count number of iterations using step size or
    # step height h
    n = (int)((x - x0)/h)
    # Iterate for number of iterations
    y = y0
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y,eq)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1,eq)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2,eq)
        k4 = h * dydx(x0 + h, y + k3,eq)

        # Update next value of y
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)

        # Update next value of x
        x0 = x0 + h
    y='The value of y at {} is: '.format(x) + str(y)
    resulted={"k1":k1, "k2":k2, "k3":k3,"k4":k4,"y":y}
    return resulted

# Driver method
def mymain(x0,y0,x,h,eq):
        x0=x0
        y0=y0
        x=2
        h=h
     #   value = 'The value of y at x is:' + str()
        return (rungeKutta(x0, y0, x, h,eq))

#print(mymain(0,1,2,0.2,"(x-y)/2"))

# This code is contributed by Prateek Bhindwar
