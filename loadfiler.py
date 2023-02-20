# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:54:18 2023

@author: willi
"""
import numpy as np

file = np.loadtxt("psg_trn.txt")[:, 1]
print(file)