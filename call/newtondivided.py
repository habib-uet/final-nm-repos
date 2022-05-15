# Python3 program for implementing 
# Newton divided difference formula 
  
# Function to find the product term 
def proterm(i, value, x): 
    pro = 1; 
    for j in range(i): 
        pro = pro * (value - x[j]); 
    return pro; 
  
# Function for calculating 
# divided difference table 
def dividedDiffTable(x, y, n):
  
    for i in range(1, n): 
        for j in range(n - i): 
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
  
# Function for applying Newton's 
# divided difference formula 
def applyFormula(value, x, y, n): 
  
    sum = y[0][0]; 
  
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]); 
      
    return sum; 
  
# Function for displaying divided 
# difference table 
def printDiffTable(y, n): 
    stri=str()
    for i in range(n): 
        for j in range(n - i): 
            stri+=str(round(y[i][j], 4)) + "\t"; 
        stri+="\n" 
    return stri
# Driver Code
def mymain(x0,yvalue,xp,n):
    n = n;
    x=x0
# y[][] is used for difference table
# with y[][0] used for input
    y = [[0 for i in range(n)] 
        for j in range(n)]; 
    for i in range(n):
         y[i][0]=yvalue[i]  
    y=dividedDiffTable(x, y, n); 
    stri=printDiffTable(y, n);
    value = xp;
# printing the value 
    value="\nValue at" + str( value) + "is" + str(round(applyFormula(value, x, y, n), 2))
    myresult ={"result": value,"table":stri}
    return myresult

# number of inputs given 

# y[][] is used for divided difference 
# table where y[][0] is used for input 

# calculating divided difference table 
  
# displaying divided difference table 
 
  
# value to be interpolated 

  
# This code is contributed by mit