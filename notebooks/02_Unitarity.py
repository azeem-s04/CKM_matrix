# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:27:55 2026

@author: azeem
"""

#%% Preamble

from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
os.chdir(PROJECT_ROOT)


import numpy as np

import modules.ckm as ckm
import modules.unitarity as unitarity

#%% Unitarity relations

 
# From PDG2024 global fit:
theta_12 = 13.00
theta_13 = 0.214
theta_23 = 2.40
delta = 65.7

V, V_mag = ckm.CKM_matrix(theta_12, theta_13, theta_23, delta)
U = unitarity.unitarity_relations(V)

labels = ["Column 1", "Column 2", "Column 3", "Row 1", "Row 2", "Row 3"]

for label, value in zip(labels, U): # read key:value pairs of dictionary (formed using zip)
    print(f"{label:<12} {value.real:+.3e} {value.imag:+.3e}j")

print("\nMaximum residual:", np.max(np.abs(U)))

