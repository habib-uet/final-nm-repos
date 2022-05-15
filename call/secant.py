from sympy import *
from math import *
def fix_power_sign(equation):
    return equation.replace("^", "**")
def eval_polynomial(equation, x_value):
    x=x_value
    return eval(equation)
def secant(poly,x0,x1,e,noofiter,flag=true):
    result=dict()
    for i in range(noofiter):  
        v=dict()
        if flag==true:
            f0=eval_polynomial(poly,x0)
            f1=eval_polynomial(poly,x1)
            denom=f1-f0
            temp=denom
            v["f0"]=f0
            v["f1"]=f1
            v["x0"]=x0
            v["x1"]=x1
            v["i"]=i
            if temp<0:
                temp*=-1
            if temp<e:
                flag=false
                break
            x2=((x0*f1)-(x1*f0))/denom
            v["x2"]=x2
            x3=x2-x1
            if x3<0:x3=x3*-1
            if x3<e:
                flag=false
                break
            x0=x1
            x1=x2
            result[i]=v
    return result
    
