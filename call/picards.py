from sympy import *
from math import *
x = Symbol('x')

def fix_power_sign(equation):
    return equation.replace("^", "**")

def eval_polynomial(equation, x):
    equation=equation.replace("x","(x)")
    fixed_equation = fix_power_sign(equation.strip())
    parts = fixed_equation.split("+")
    x_str_value = str(x)
    parts_with_values = (part.replace("x", x_str_value) for part in parts )
    partial_values=list()
    for part in parts_with_values:
        try:
            x1=eval(part)
            partial_values.append(x1)
        except:
            return "error"
    x=x
    return eval(equation)


    


def picards(poly,x0,y0,n):
    l=list()
    intial=y0
    p=poly
    string = poly
    for i in range(n):
        p=poly.replace("y", "({})".format(y0))
        #print(p,i)
        p=integrate(p,(x))
        res=eval_polynomial(str(p),x0)
        res*=-1

        y0=str(intial)+"+"+str(p)+str(res)
       # print(type(str(p)))
         
        l.append({"i":i,"p":p})
    print(l)
    return l
#print(picards("x+y^2",0,1,4))