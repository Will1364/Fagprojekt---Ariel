# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math

def SN(Signal,Model,flatModel,Uncertainty):
    
    SN = sum((Signal-Model)/Uncertainty)       # S/N for spektret
    
    return SN
