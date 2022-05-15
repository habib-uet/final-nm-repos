from operator import le
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import FileSystemStorage
from sympy import li
from . import forms
from . import models
from . import bisection as b
from . import secant as s
from .import regularfalsi as regula
from .import newtonraphson as newton 
from . import gaus as ga
from . import jacobi as jac
from . import Newton_forward as forward
from . import Newton_backward as backward
from . import example as eul
from . import trapizoid as trap
from . import picards as pic
from . import forwward as newton_forwards
from . import gausforward as g
from . import stirling as stirl
from . import bessels as bese
from . import backward as back
from . import lagrange as lag
from . import boole as bole
from . import weedle as wed
from . import simpson1by3 as simpson
from . import sim3by8 as sim2
from . import newtondivided as newtondiv
from . import rungekutta as rungekut
from . import DerNBackInt as derback
from . import DerNForInt as derfront
import numpy as np
def runge(request):
    if request.method=='POST':
        x0=request.POST["text"]
        x0=float(x0)
        y0=request.POST["text-1"]
        y0=float(y0)
        atx=request.POST["text-2"]
        atx=float(atx)
        h=request.POST["text-3"]
        h=float(h)
        fx=request.POST["text-4"]
        result=rungekut.mymain(x0,y0,atx,h,fx)
        return render(request, 'runge.html',{"result":result})
    return render(request, 'runge.html')      

def callnonlinear(request):
    if request.method=='POST':
        poly=request.POST["poly"]
        methodtype=request.POST["select"]
        X0=request.POST["text-1"]
        X0=float(X0)
        X1=request.POST["text"]
        if methodtype!="Newton Raphson":X1=float(X1)
        E1=request.POST["text-2"]
        E1=float(E1)
        it=request.POST["iter"]
        it=int(it)
        if methodtype=="Bisection":
            result=b.bisection(poly,X0,X1,E1,it)
        elif methodtype=="Newton Raphson":
            result=newton.mewtonraphson(poly,X0,E1,it)
        elif methodtype=="Regula Falsi":
            result=regula.regulafalsi(poly,X0,X1,E1,it) 
        elif methodtype=="Secant":
            result=s.secant(poly,X0,X1,E1,it)
        return render(request, 'Non-Linear.html',{"id":result,"method":methodtype})
    else:
        return render(request, 'Non-Linear.html',{'id':"","method":""})      
   
def Linear(request):
    if request.method=='POST':
        methodtype=request.POST["select"]
        nofeq=request.POST["nofeq"]
        nofeq=int(nofeq)
        nofiter=int(request.POST["Equ"])
        lis=[]
        b = np.array([0.0 for x in range(nofeq)])
        guess = np.array([0.0 for x in range(nofeq)])
        
        for i in range(nofeq):
            x=list()
            for j in range(nofeq):
                x.append(float(request.POST['text{}{}'.format(i+1,j+1)]))
            lis.append(x)
            arr = np.array(lis,dtype=float)
            print("{} in {}".format(i+1,lis))
            b[i]=request.POST['text{}'.format(i+1)]
        if methodtype=="Gauss Seidal":
            sol = ga.gauss_seidel(arr,b,nofiter,x=guess)
        else: sol = jac.jacobi(arr,b,nofiter,x=guess)
        return render(request, 'Linear.html',{"id":sol,"eq":range(nofeq),"method":methodtype})
    else:
        return render(request, 'Linear.html',{'message':"You are not logged in as doctor"})      

def interpolation(request):
    if request.method=='POST':
        methodtype=request.POST["select"]
        nofx=request.POST["text-1"]
        nofx=int(nofx)
        x=list()
        Xp=request.POST["text-6"]
        Xp=float(Xp)
        for i in range(nofx):
            x.append(float(request.POST["text{}".format(i+100)]))
        if methodtype!="Lagrange" and methodtype!="newtondivided" and methodtype!="newtonforwardderivative" and methodtype!="newtonbackwardderivative": 
            X0=request.POST["text-2"]
            X0=float(X0)
            e=request.POST["text-7"]
            e=float(e)

        if methodtype=="Newton Foraward":
            
            result=newton_forwards.mymain(X0,x,Xp,nofx,e) 
            #return render(request, 'Interpolation.html',{"x":result["xavlus"],"y":result["yvalues"],"res":result,"eq":range(len(result["differencetable"])) })
            return render(request, 'Interpolation.html',{"result":result})
        elif methodtype=="Newton Backward":
            result=back.mymain(X0,x,Xp,nofx,e) 
            return render(request, 'Interpolation.html',{"result":result})       
        elif methodtype=="Gausss Forward":
            result=g.mymain(X0,x,Xp,nofx,e) 
            #return render(request, 'Interpolation.html',{"x":result["xavlus"],"y":result["yvalues"],"res":result,"eq":range(len(result["differencetable"])) })
            return render(request, 'Interpolation.html',{"result":result})
        elif methodtype=="Stirling":
            temx=list()
            temx.append(X0)
            for i in range(1,nofx):
                temx.append(x[i-1]+e)
            result=newton_forwards.mymain(X0,x,Xp,nofx,e)
            resulted=stirl.Stirling(temx,x,Xp,nofx) 
            #return render(request, 'Interpolation.html',{"x":result["xavlus"],"y":result["yvalues"],"res":result,"eq":range(len(result["differencetable"])) })
            return render(request, 'Interpolation.html',{"ourresult":result,"values":resulted})
        elif methodtype=="Bessel":
            temx=list()
            temx.append(X0)
            for i in range(1,nofx):
                temx.append(x[i-1]+e)
            result=newton_forwards.mymain(X0,x,Xp,nofx,e)
            resulted=bese.mymain(temx,x,Xp,nofx,e) 
            #return render(request, 'Interpolation.html',{"x":result["xavlus"],"y":result["yvalues"],"res":result,"eq":range(len(result["differencetable"])) })
            return render(request, 'Interpolation.html',{"ourresult":result,"values":resulted})
        elif methodtype=="Lagrange":
            y=list()
            for i in range(nofx):
                y.append(float(request.POST["text2{}".format(i+100)]))    
            resultoflagrange=lag.mymain(x,y,nofx,Xp)
            return render(request, 'Interpolation.html',{"resultoflagrange":resultoflagrange,"x":y,"y":x,"r":range(len(x))})
        elif methodtype=="newtondivided":
            y=list()
            for i in range(nofx):
                y.append(float(request.POST["text2{}".format(i+100)]))    
            resultoflagrange=newtondiv.mymain(y,x,Xp,nofx)
            return render(request, 'Interpolation.html',{"resultofnewtondivide":resultoflagrange})
        elif methodtype=="newtonforwardderivative":
            y=list()
            for i in range(nofx):
                y.append(float(request.POST["text2{}".format(i+100)]))  
            myneb=request.POST["text-29"]  
            myneb=int(myneb)
            resultofderivative=derfront.P4(nofx,myneb,Xp,y,x)
            return render(request, 'Interpolation.html',{"resultofderivative":resultofderivative})
        elif methodtype=="newtonbackwardderivative":
            
            y=list()
            for i in range(nofx):
                y.append(float(request.POST["text2{}".format(i+100)]))  
            myneb=request.POST["text-29"]  
            myneb=int(myneb)
            resultofderivative=derback.P3(nofx,myneb,Xp,y,x)
            print(resultofderivative)
            return render(request, 'Interpolation.html',{"resultofderivative":resultofderivative})
        #result=backward.newtonbackward(nofx,1,X0,Xp,x,e)
        return render(request, 'Interpolation.html',{"x":result["xavlus"],"y":result["yvalues"],"res":result,"eq":range(len(result["differencetable"])) })
    else:
        return render(request, 'Interpolation.html',{'message':"You are not logged in as doctor"})
def Integration(request):
    if request.method=='POST':
        methodtype=request.POST["select"]
        y=list()
        x=list()
        if methodtype=="Trapizoid":
            nofx=request.POST["tried"]
            nofx=int(nofx)
            n=nofx  
        else:
            n=request.POST["text-1"] 
            n=int(n)
        a=request.POST["phone"]
        a=float(a)
        b=request.POST["text"]
        b=float(b)
        if methodtype=="Trapizoid":
            for i in range(n):
                x.append(float(request.POST["text{}".format(i+100)]))        
            for i in range(n):
                y.append(float(request.POST["text2{}".format(i+100)]))  
            #return render(request, 'Trapizoid.html',{'message':"You are not logged in as doctor"})
            result=trap.trapizoid(a,b,n,x,y)
            return render(request, 'Trapizoid.html',{"id":result["v"],"result":result["res"]  })
        elif methodtype=="Boole":
            func=request.POST["name"]
            nontrapizoid=bole.mymain(a,b,func,n)
            return render(request, 'Trapizoid.html',{"reultednontrapizoid":nontrapizoid  })
        elif methodtype=="Weedle":
            func=request.POST["name"]
            nontrapizoid=wed.mymain(a,b,func,n)
            return render(request, 'Trapizoid.html',{"reultednontrapizoid":nontrapizoid  })
        elif methodtype=="Simpson1by3":
            func=request.POST["name"]
            nontrapizoid=simpson.mymain(a,b,func,n)
            return render(request, 'Trapizoid.html',{"reultednontrapizoid":nontrapizoid  })
        elif methodtype=="Simpson3by3":
            func=request.POST["name"]
            nontrapizoid=sim2.mymain(a,b,func,n)

            return render(request, 'Trapizoid.html',{"reultednontrapizoid":nontrapizoid  })
        
        #Weedle  Simpson3by8
    else:
        return render(request, 'Trapizoid.html',{'message':"You are not logged in as doctor"})
def Euler(request):
    if request.method=='POST':
        X0=request.POST["phone"]
        X0=float(X0)
        Y0=request.POST["text"]
        Y0=float(Y0)
        n=request.POST["text-1"]
        n=int(n)
        eq=request.POST["name"]
        h=request.POST["text-2"]
        h=float(h)
        result=eul.eulere(eq,X0,h,Y0,n)
        return render(request, 'Euler.html',{"id":result  })
    else:
        return render(request, 'Euler.html',{'message':"You are not logged in as doctor"})
def Picards(request):
    if request.method=='POST':
        X0=request.POST["phone"]
        X0=float(X0)
        Y0=request.POST["text"]
        Y0=float(Y0)
        n=request.POST["text-1"]
        n=int(n)
        eq=request.POST["name"]
        result=pic.picards(eq,X0,Y0,n)
        #return render(request, 'Picards.html',{'message':"You are not logged in as doctor"})
        
        return render(request, 'Picards.html',{"id":result  })
    else:
        return render(request, 'Picards.html',{'message':"You are not logged in as doctor"})
