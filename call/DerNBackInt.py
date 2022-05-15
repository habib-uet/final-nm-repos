def P3(values,degree,xp,x,fx):    
    degree=degree
    values=values
    actual_degree=0
    xp=xp
    x=x
    fx=fx
    h=0
    p=-2
    nebla=[0,0,0,0,0,0,0,0,0,0]
    class NewBackDiff:
        def __init_(self):
            print("\n\t\tFROM NEWTON'S BACKWARD DIFFERENCE FORMULA\n\n")

        def result(self):

            stri=""
            stri+="X\t"
            for i in range(values):
                stri+="\t"+ str(x[i])
            stri+=("\n")
            stri+="\nF(x)\t"
            for i in range(values):
                stri+="\t"+str(fx[i])
            stri+="\n"
            p=-2
            h=x[1]-x[0]
            temp=-1
            for j in reversed(range(values)):
                if (p<0 or p>1):
                    p=(xp-x[j])/h
                    temp=j         
            pvalue="\nValue of P is :\t" + str(p) +"\n"
            j=values
            table=""
            for actual_degree in range(1, (degree+1)):
                if (j>1):
                    table+="\n\nNebla power" + str(actual_degree) + ":\t"
                    for k in range(j-1):
                        fx[k]=fx[k+1]-fx[k]
                        table+=str(fx[k]) + "\t"
                    nebla[actual_degree-1]=fx[temp-actual_degree]
                    #print(nebla[actual_degree-1])
                    j-=1
            #print(table)
            parray1=[1,2*p+1,3*p*p+6*p+2,2*p*p*p+9*p*p+11*p+3]
            div1=[1,2,6,12]
            ans1=0
            for i in range(actual_degree):
                ans1+=nebla[i]*parray1[i]/div1[i]
            fdash="f`(" + str(xp) +"):\t"+ str(ans1/h)

            parray2=[1,p+1,6*p*p+18*p+11]
            div2=[1,1,12]
            ans2=0
            for i in range(1,actual_degree):
                ans2+=nebla[i]*parray2[i-1]/div2[i-1]
            fdouble="f``(" + str(xp)+"):\t"+ str(ans2/(h*h))
            resulted={"table":table,"pvalue":pvalue,"fdash":fdash,"fddash":fdouble,"string":stri}
            return resulted
    obj=NewBackDiff()
    return obj.result()
#P3(5,4,.25,[0,0.5,1,1.5,2],[2.0286,2.4043,2.7637,3.1072,3.435])

