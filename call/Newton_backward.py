# math AAT (Alternative Assessment Tool)
# python math project - chapter 2 - numerical methods
# Newton's Backward Interpolation Formula
# 18th October, 2015

import time

diff_file = open('NewtonBIF.txt', 'w')
diff_file.close()


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
    print('\nCreating difference table for difference 1')
    # time.sleep is used to make output on terminal more pleasant
    time.sleep(1)
    diff_file = open('NewtonBIF.txt', 'r')
    filevals = list(diff_file.readlines()[-1].split())
    diffvals = [(float(filevals[i+1]) - float(filevals[i])) for i in range(len(filevals) - 1)]
    # prints diffvals
    for val in diffvals:
        print(val)
    diff_file = open('NewtonBIF.txt', 'a')
    diff_file.writelines([" ".join(str(val) for val in diffvals)])
    diff_file.write('\n')
    iternum = len(filevals) - 2  # 1 because it has been done above
    for i in range(iternum):
        print('\nCreating difference table for difference {}'.format(i+2))
        time.sleep(1)
        diff_file = open('NewtonBIF.txt', 'r')
        filevals = list(diff_file.readlines()[-1].split())
        diffvals = [(float(filevals[i+1]) - float(filevals[i])) for i in range(len(filevals) - 1)]
        # prints diffvals
        for val in diffvals:
            print(val)
        diff_file = open('NewtonBIF.txt', 'a')
        diff_file.writelines([" ".join(str(val) for val in diffvals)])
        diff_file.write('\n')
        diff_file.close()
    print('\n')


def genpterm(p, iternum, ynterms):
    '''
    Generates the value of p term for terms in the main equation.
    '''
    pterm = 1
    print('\nCalculating pterm of {} term'.format(iternum + 2))
    for i in range(iternum+1):
        print('\tpterm = {} * ({} - {})'.format(pterm, p, i))
        pterm *= p + i
        print('\tpterm is {}'.format(pterm))
    return pterm


def ypgen(diff_file, p):
    '''
    Calculates value of yp by finding and adding all the terms.
    '''
    diff_file = open('NewtonBIF.txt', 'r')
    content = diff_file.readlines()
    ynterms = []
    for i in content:
        ynterms.append(i.split()[-1])
    ynterms = [float(term) for term in ynterms]
    yp = ynterms[0]
    ynterms = ynterms[1:]
    iternum = len(ynterms)
    print('\nAs p = {}'.format(p))
    for i in range(iternum):
        print("\n")
        print('{} term of yp is (pterm * {}) / {}!'.format(i + 2, ynterms[i], i + 1))
        time.sleep(1)
        yp += float(genpterm(p, i, ynterms) * ynterms[i]) / float(factorialfunc(i+1))
    print('returning yp = {}'.format(yp))
    diff_file.close()
    return yp

def newtonbackward(n1,h1,X00,Xpp,y,decimaldigitaccuracy):
    #print("What is the number of values of x?")
    n = n1
    res=""
    h = h1 
    x0 = X00
    xvals = [(x0 + (i * h)) for i in range(n)]
    
    res+="The values of x are: "
    for x in xvals:
        res+=str(x)
    res+='\n'
    xn = xvals[-1]
    xp = Xpp
    res+="Finding the value of p."
    res+="Using the formula xp = xn + ph"
    res+="Here {} = {} + p * {}".format(xp, xn, h)
    p = (float(xp - xvals[-1])) / float(h)
    res+='Value of p is: {}'.format(p)
    yvals = [None] * n
    yvals=y
    with open('NewtonBIF.txt', 'a') as diff_file:
        diff_file.write(' '.join([str(val) for val in yvals]))
        diff_file.write('\n')
    res+='\nValues of y are {}'.format(yvals)
    xtoymap = {}
    for i in range(n):
        xtoymap[xvals[i]] = yvals[i]
    res+='\nx values & corresponding y values are:'
    res+='\nx values            y values'
    for key in xvals:
        res+='\n{}                 {}'.format(key, xtoymap[key])
    diff_file = open('NewtonBIF.txt', 'a')
    diffgen(diff_file)
    diff_file.close()
    yp = ypgen(diff_file, p)
    decimalval = decimaldigitaccuracy
    yp = round(yp, decimalval)
    res+='Value of yp = y({}) = {}'.format(xp, yp)
    res+='\n'
    res+="See NewtonBIF.txt for y difference values."
    return res

