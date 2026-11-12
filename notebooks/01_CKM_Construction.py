# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:33:07 2026

@author: azeem
"""

#%% Correct directory for importing custom modules
from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parent
os.chdir(PROJECT_ROOT)

#%% Imports
import numpy as np

import modules.ckm as ckm
import modules.unitarity as unitarity

#%% CKM matrix

# CKM matrix construction
# Accepts the 4 CKM parameters (PDG) and returns the matrix



V = ckm.CKM_matrix(13, 2.4, 0.214, 65.7)


        
deviation_U = unitarity.unitarity(V[0])

print(np.abs(deviation_U), 
      "\n ------------------------------------------------------------ \n" +
      "Max.deviation: \n",
      np.max(np.abs(deviation_U))) # absolute deviation from unitarity


    
    
    

