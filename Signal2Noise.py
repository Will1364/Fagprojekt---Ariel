# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math

def chiSquared(Signal,Model,flatModel,Uncertainty):
    
    SN_m = sum((Signal-Model)/Uncertainty)       #chi i anden udregnes for spektret
    SN_f = sum((Signal-flatModel)/Uncertainty)   #chi i anden udregnes for den flade model
    
    return SN_m, SN_f
