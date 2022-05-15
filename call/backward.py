# calculating u mentioned in the formula
from unittest import result


def u_cal(u, n):

	temp = u;
	for i in range(1, n):
		temp = temp * (u + i);
	return temp;

# calculating factorial of given number n
def fact(n):
	f = 1;
	for i in range(2, n + 1):
		f *= i;
	return f;

def mymain(x0,yvalue,xp,n,h):
    n = n;
    x=list()
    x.append(x0)
    for i in range(1,n):
        x.append(x[i-1]+h)
# y[][] is used for difference table
# with y[][0] used for input
    y = [[0 for i in range(n)]
        for j in range(n)];
    for i in range(n):
        y[i][0]=yvalue[i]
# Calculating the forward difference
# table
    for i in range(1, n):
        j=n-1
        while j>=i:
            y[j][i] = y[j][i - 1] - y[j - 1][i - 1];
            j=j-1
# Displaying the f
# Displaying the forward difference table
# Displaying the forward difference table


	
    stri=""
    mylist=list()
    for i in range(n):
        stri+=str(x[i])+"\t"
        let=str()
        j=0
        while j<=i:
            let+=str(y[i][j])+"\t"
            stri+=str(y[i][j])+"\t"
            j=j+1
        ty={"val":round(x[i],4)  ,"remain":let}
        mylist.append(ty) 
        stri+="\n"
    
# Value to interpolate at
    value = xp;
 
# initializing u and sum
    sum = y[n-1][0];
    u = (value - x[n - 1]) / (x[1] - x[0]);
    for i in range(1,n):
        sum = sum + (u_cal(u, i) * y[n - 1][i])/ fact(i);
    result="Value at"+" "+ str( value)+ " "+ "is "+  str(round(sum, 6))
    print(result);
    myresult ={"result": result,"table":mylist}
    return myresult
# This code is contributed by mits
mymain(1891,[46,66,81,93,101],1925,5,10)    