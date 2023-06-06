# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math

def SN(Signal,Model,Uncertainty):
    
    SN = math.sqrt(sum(((Signal-Model)/Uncertainty)**2))       # S/N for spektret
    
    return SN
