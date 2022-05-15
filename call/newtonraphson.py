from sympy import *
from math import *
x = Symbol('x')

def fix_power_sign(equation):
    return equation.replace("^", "**")

def eval_polynomial(equation, x_value):
    x=x_value
    return eval(equation)

def mewtonraphson(poly,guess,e,noofiter,flag=true):
    result=dict()
    for i in range(noofiter): 
        v=dict() 
        if flag==False:
            return result
        f=eval_polynomial(poly,guess)
        fd=eval_polynomial(str(diff(poly,x)),guess)
        x1=guess-(f/fd)
        v["i"]=i
        v["xi"]=guess
        v["fxi"]=f
        v["fd"]=fd
        v["xi1"]=x1
        x2=x1-guess
        if x2<0:
           x2=x2*-1
        if x2<e:
           flag=false
        else:
           guess=x1        
        result[i]=v
    return result


