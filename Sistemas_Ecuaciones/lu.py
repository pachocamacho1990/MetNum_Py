import numpy as np

def lu_fac(matriz):
    A = np.array(matriz)
    epsilon = np.finfo(np.float).eps
    dims = A.shape
    L = np.zeros(dims)
    U = np.zeros(dims)
    for j in range(dims[0]):
        if abs(A[j,j]) < epsilon:
            print('ERROR: pivote nulo')
            return None
        L[j,j] = 1.0
        for i in range(j+1,dims[0]):
            L[i,j] = A[i,j]/A[j,j]
            for k in range(j+1,dims[0]):
                A[i,k] = A[i,k] - L[i,j]*A[j,k]
        for k in range(j,dims[0]):
            U[j,k] = A[j,k]

    return L, U
