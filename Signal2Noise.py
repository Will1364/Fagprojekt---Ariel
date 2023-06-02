# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math

def SignalToNoise(Signal,Model,flatModel,Uncertainty):
    
    SN_m = sum((Signal-Model)/Uncertainty)       # S/N for spektret
    SN_f = sum((Signal-flatModel)/Uncertainty)   # S/N for den flade model
    
    return SN_m, SN_f
