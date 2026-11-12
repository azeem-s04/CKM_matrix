# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:33:07 2026

@author: azeem
"""

#%% Correct directory for importing custom modules
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
os.chdir(PROJECT_ROOT)

#%% Imports
import numpy as np

import modules.ckm as ckm
import modules.unitarity as unitarity

#%% CKM matrix

# CKM matrix construction
# Accepts the 4 CKM parameters (PDG) and returns the matrix

# From PDG2024 global fit:
theta_12 = 13.00
theta_13 = 0.214
theta_23 = 2.40
delta = 65.7

V, V_mag = ckm.CKM_matrix(theta_12, theta_13, theta_23, delta)

print(V)

#%% Unitarity check

deviation_U = unitarity.unitarity(V)

print(np.abs(deviation_U), 
      "\n ------------------------------------------------------------ \n" +
      "Max.deviation: \n",
      np.max(np.abs(deviation_U))) # absolute deviation from unitarity

#%% Jarlskog invariant calculation

J = ckm.Jarlskog(theta_12, theta_13, theta_23, delta)

J_exp_max = ckm.Jarlskog(theta_12, theta_13, theta_23, 90) # delta is unconstrained

print(f"{'Experimental J:':<20} {J:.6e}")
print(f"{'Experimental Jmax:':<20} {J_exp_max:.6e}")

    
    

