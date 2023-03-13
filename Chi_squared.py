# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:36:34 2023

@author: willi
"""

import math

def chiSquared(Signal,Model,flatModel,Uncertainty):
    chi_m = sum(((Signal-Model)/Uncertainty)**2)      
    chi_f = sum(((Signal-flatModel)/Uncertainty)**2)
    
    return chi_m, chi_f
