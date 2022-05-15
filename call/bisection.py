import string
from unittest import result
from sympy import *
from math import *

def eval_polynomial(equation, x_value):
    x=x_value
    return eval(equation)
def bisection(poly,x1,x2,e,noofiter,flag=true):
    result=dict()
    
    for i in range(noofiter):  
        v=dict()
        if flag==true:
            temp=x2-x1
            if temp<0:
               temp*=-1
            if temp<e:
               flag=false
               break
            v["x0"]=x1
            v["x1"]=x2
            f1=eval_polynomial(poly,x1)
            f2=eval_polynomial(poly,x2)
            v["fx0"]=f1
            v["fx1"]=f2
            f3=f1*f2
            x3=(x1+x2)/2
            v["x2"]=x3
            f3=eval_polynomial(poly,x3)
            v["fx2"]=f3
            if f3==0:
                v["i"]=i+1
                v["root"]=x3
            f=f1*f3
            if f<0:
                x2=x3
            else:
                f=f2*f3
                if f<0:
                   x1=x3
            v["i"]=i+1
            v["root"]=x1
        
        result[i]=v
        
        #result.append(a)
       # print(result)
        
    
    #print(result)    
    return result


    