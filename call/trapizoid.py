import numpy as np
from math import *
def fix_power_sign(equation):
    return equation.replace("^", "**")

def eval_polynomial(equation, x_value):
    x=x_value
    return eval(equation)
def trapizoid(a,b,n,fx,x):
    
    a = a
    b = b
    n = n  
    h = (b - a) / (n-1)
    f=np.zeros(n,dtype=float)
    temp=a
    v=list()
    for i in range(n):

        f[i]=fx[i]
        v.append({"i":i,"x":x[i],"fx":f[i]})
        temp+=h
    myres=0
    for x in range(1,n-1):
        myres+=fx[x]
        

    I_trap = (h/2)*(f[0]+ f[n-1] + 
          2 * myres)
    print(h)
    k=dict()
    k["v"]=v
    k["res"]=(I_trap) 
    k["x"]=x
    
    return k
    #err_trap = 2 - I_trap

#trapizoid(0,np.pi,11,"sin(x)")
