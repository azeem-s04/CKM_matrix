# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:34:15 2026

@author: azeem
"""
import numpy as np

def CKM_matrix(theta_12, theta_13, theta_23, delta):
    
    # Convert from degrees to radians
    theta_12 = np.deg2rad(theta_12)
    theta_13 = np.deg2rad(theta_13)
    theta_23 = np.deg2rad(theta_23)
    delta = np.deg2rad(delta)
    
    # Plain 3 x 3 matrix
    V_CKM = np.zeros((3,3), dtype=complex)
    
    # PDG representation
    
    c12 = np.cos(theta_12)
    s12 = np.sin(theta_12)
    c13 = np.cos(theta_13)
    s13 = np.sin(theta_13)
    c23 = np.cos(theta_23)
    s23 = np.sin(theta_23)
    
    # Matrix elements
    
    V_CKM[0,0] = c12*c13
    V_CKM[0,1] = s12*c13
    V_CKM[0,2] = s13*np.exp(-delta*1j)
    
    V_CKM[1,0] = -(c23*s12) - (c12*s23*s13*np.exp(delta*1j))
    V_CKM[1,1] = (c12*c23) - (s12*s23*s13*np.exp(delta*1j))
    V_CKM[1,2] = c13*s23
    
    V_CKM[2,0] = (s12*s23) - (c12*c23*s13*np.exp(delta*1j))
    V_CKM[2,1] = -(c12*s23) - (c23*s12*s13*np.exp(delta*1j))
    V_CKM[2,2] = c13*c23
    
    V_mag = np.abs(V_CKM) # absolute values of elements
    
    return V_CKM, V_mag

def Jarlskog(theta_12, theta_13, theta_23, delta):
    # Convert from degrees to radians
    theta_12 = np.deg2rad(theta_12)
    theta_13 = np.deg2rad(theta_13)
    theta_23 = np.deg2rad(theta_23)
    delta = np.deg2rad(delta)
    
    # PDG representation
    
    c12 = np.cos(theta_12)
    s12 = np.sin(theta_12)
    c13 = np.cos(theta_13)
    s13 = np.sin(theta_13)
    c23 = np.cos(theta_23)
    s23 = np.sin(theta_23)
    
    J = c12*c23*(c13**2)*s12*s23*s13 * np.sin(delta)
    return J
