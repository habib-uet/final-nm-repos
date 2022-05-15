# Python3 code for Gauss's Forward Formula
# importing library
import numpy as np
from decimal import *
# function for calculating coefficient of Y
def p_cal(p, n):

    temp = p;
    for i in range(1, n):
        if(i%2==1):
            temp * (p - i)
        else:
            temp * (p + i)
    return temp;
# function for factorial
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

# storing available data
def mymain(x0,yvalue,xp,n,h):
    n = n;
    x=list()
    stri=str()
    x.append(x0)
    for i in range(1,n):
        x.append(x[i-1]+h)
# y[][] is used for difference table
# with y[][0] used for input
    y = [[0 for i in range(n)]
        for j in range(n)];
    for i in range(n):
         y[i][0]=yvalue[i]
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = np.round((y[j + 1][i - 1] - y[j][i - 1]),4);
    mylist=list()
    for i in range(n):
        stri+=str(x[i])+"\t"
        let=str()
        for j in range(n - i):
            let+=str(y[i][j])+"\t"
            stri+=str(y[i][j])+"\t"
        ty={"val":round(x[i],4),"remain":let}
        mylist.append(ty) 
        stri+="\n"
# Value of Y need to predict on
    value = xp;

# implementing Formula
    sum = y[int(n/2)][0];
    p = (value - x[int(n/2)]) / (x[1] - x[0])

    for i in range(1,n):
    # print(y[int((n-i)/2)][i])
        sum = sum + (p_cal(p, i) * y[int((n-i)/2)][i]) / fact(i)
    result="Value at " + str( value)+" is " + str( round(sum, 4))
    
    myresult ={"result": result,"table":mylist}
    return myresult
# This code is contributed by mits
#mymain(1,[2.7183,2.8577,3.0042,3.1582,3.3201,3.4903,3.6693,3.6693],1.17,8,0.05)
