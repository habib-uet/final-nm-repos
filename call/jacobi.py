from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot
import numpy
def jacobi(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed                                                                                                                                                            
    if x is None:
        x = zeros(len(A[0]))

    # Create a vector of the diagonal elements of A                                                                                                                                                
    # and subtract them from A                                                                                                                                                                     
    D = diag(A)
    R = A - diagflat(D)
    #print(R)
   # previous=array([0 for x in range(variables)])
    # Iterate for N times
    result=dict()                                                                                                                                                                          
    for i in range(N):
        v=dict()
        x = (b - dot(R,x)) / D
        v["values"]=x
        v["i"]=i
        result[i]=v 
    return result



