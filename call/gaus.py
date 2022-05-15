import numpy as np
def gauss_seidel(A, b,max_iterations, x):
    #x is the initial condition
    iter1 = 0
    #Iterate
    v=dict()
    for k in range(max_iterations):
        result=dict()
        iter1 = iter1 + 1
 #       print ("The solution vector in iteration", iter1, "is:", x)    
        x_old  = x.copy()
        
        #Loop over rows
        for i in range(A.shape[0]):
            x[i] = (b[i] - np.dot(A[i,:i], x[:i]) - np.dot(A[i,(i+1):], x_old[(i+1):])) / A[i ,i]
        result["values"]=x
        result["i"]=k
        v[k]=result 
        #Stop condition 
        
        #LnormInf corresponds to the absolute value of the greatest element of the vector.
        
    return v
