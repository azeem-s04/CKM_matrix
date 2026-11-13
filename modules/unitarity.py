# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:48:12 2026

@author: azeem
"""

import numpy as np

def unitarity(A):
    #from numpy import matrix
    
    if np.shape(A)[0] == np.shape(A)[1]:
        #A_dagger = matrix.getH(A) # Hermitian conjugate of A
        A_dagger = A.conj().T
        
        return np.matmul(A_dagger, A) - np.identity(np.shape(A)[0])
    else:
        raise ValueError("Input must be a square matrix")
        

def unitarity_relations(V):
    
    V = np.asarray(V, dtype=complex)
    
    # Check if input is a 3x3 matrix
    if np.shape(V) == (3, 3):
        
        Vdag = V.conj().T
        
        A = np.matmul(Vdag, V)
        B = np.matmul(V, Vdag)
        
        # 3 orthogonality relations for columns of V:
            
        col_1 = A[0][1]
        col_2 = A[0][2]
        col_3 = A[1][2]
        
        # 3 orthogonality relations for rows of V:
            
        row_1 = B[0][1]
        row_2 = B[0][2]
        row_3 = B[1][2]
        
        return col_1, col_2, col_3, row_1, row_2, row_3
    
    else:
        raise ValueError("Argument must be a 3 x 3 matrix.")