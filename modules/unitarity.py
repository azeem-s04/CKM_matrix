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