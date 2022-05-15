# math AAT (Alternative Assessment Tool)
# python math project - chapter 2 - numerical methods
# Newton's Forward Interpolation Formula
# 16th October, 2015

import string
import time
from typing import OrderedDict


# deliberately not importing math.
def factorialfunc(n):
    '''
    Returns the factorial of a positive integer.
    '''
    assert type(n) == type(1) or type(n) == type(1.0), "n is not a number."
    n = int(n)
    assert n > 0, "Can not find factorial of a negative number."
    if n == 1:
        return 1
    else:
        return n * factorialfunc(n-1)


def diffgen(diff_file):
    '''
    Finds the first, second, third (and so on) difference of given y values.
    '''
    diff=OrderedDict()
    # time.sleep is used to make output on terminal more pleasant
    diff_file = open('NewtonFIF.txt', 'r')
    filevals = list(diff_file.readlines()[-1].split())
    diffvals = [(float(filevals[i+1]) - float(filevals[i])) for i in range(len(filevals) - 1)]
    # prints diffvals
    l=list()
    for val in diffvals:
        l.append(val)
    diff[1]=l
    diff_file = open('NewtonFIF.txt', 'a')
    diff_file.writelines([" ".join(str(val) for val in diffvals)])
    diff_file.write('\n')
    iternum = len(filevals) - 2  # 1 because it has been done above
    for i in range(iternum):
        diff_file = open('NewtonFIF.txt', 'r')
        filevals = list(diff_file.readlines()[-1].split())
        diffvals = [(float(filevals[i+1]) - float(filevals[i])) for i in range(len(filevals) - 1)]
        # prints diffvals
        l=list()
        for val in diffvals:
            l.append(val)
        diff[i+2]=l
        diff_file = open('NewtonFIF.txt', 'a')
        diff_file.writelines([" ".join(str(val) for val in diffvals)])
        diff_file.write('\n')
        diff_file.close()
        
    return diff.copy()
pvaluedic=OrderedDict()
pwithoutval=OrderedDict()
pterms=""
def genpterm(p, iternum, y0terms):
    '''
    Generates the value of p term for terms in the main equation.
    '''
    global pterms
    pterm = 1
    global pvaluedic
    for i in range(iternum+1):
        rese=""
        rese+=('pterm = {} * ({} - {})'.format(pterm, p, i))
        pterm *= p - i
        rese+=('= {}'.format(pterm))
        pvaluedic[i]=rese
    
    return pterm


def ypgen(diff_file, p):
    '''
    Calculates value of yp by finding and adding all the terms.
    '''
    diff_file = open('NewtonFIF.txt', 'r')
    content = diff_file.readlines()
    y0terms = []
    for i in content:
        y0terms.append(i.split()[0])
    y0terms = [float(term) for term in y0terms]
    yp = y0terms[0]
    y0terms = y0terms[1:]
    iternum = len(y0terms)
    global pwithoutval
    #print('\nAs p = {}'.format(p))
    for i in range(iternum):
        pwithoutval[i]='{} term of yp is (pterm * {}) / {}!'.format(i + 2, y0terms[i], i + 1)
        time.sleep(1)
        yp += float(genpterm(p, i, y0terms) * y0terms[i]) / float(factorialfunc(i+1))
    diff_file.close()
    return yp

def newtonforward(n,h1,X00,Xpp,y2,decimaldigitaccuracy):
    #print("What is the number of values of x?")
    diff_file = open('NewtonFIF.txt', 'w')
    diff_file.close()

    res=OrderedDict()
    n = n
    #print('\n')
    #h = input('Are the values equally spaced?\nIf yes enter value of \'h\'. If no, press \'n\': ')
    h=h1
    x0 = X00
    xvals = [(x0 + (i * h)) for i in range(n)]
    xp = Xpp
    p = (float(xp - x0)) / float(h)
    res["p"]='Value of p is: {}'.format(p)
    
    res["xavlus"]=xvals
    yvals = [None] * n
    yvals=y2
    with open('NewtonFIF.txt', 'a') as diff_file:
        diff_file.write(' '.join([str(val) for val in yvals]))
        diff_file.write('\n')
    res["yvalues"]=yvals
    xtoymap = {}
    for i in range(n):
        xtoymap[xvals[i]] = yvals[i]
    diff_file = open('NewtonFIF.txt', 'a')
    res["differencetable"]=diffgen(diff_file)
    diff_file.close()
    yp = ypgen(diff_file, p)
    decimalval =decimaldigitaccuracy
    yp = round(yp, decimalval)
    res["yp"]=('Value of yp = y({}) = {}'.format(xp, yp))
    at=OrderedDict()
    i=0
    global pvaluedic
    global pwithoutval

    for k, k2 in zip(pwithoutval,pvaluedic):
        at[i]=pwithoutval[k]+ " " +pvaluedic[k2]
        i+=1
    res["pval"]=at
    tem=""
    f = open("NewtonFIF.txt", "r")
    Lines = f.readlines()
    l=list()
    tr=""
    for y in xvals:
        tr+=str(y)+" "
    l.append(tr)
    for line in Lines:
        l.append("{}".format(line.strip()))
    res["file"]=l



#open and read the file after the appending:
    
    return res