# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import math

def SN(flatmodel,Model,Uncertainty):
    
    SN = math.sqrt(sum(((Model-flatmodel)/Uncertainty)**2))       # S/N for spektret
    
    return SN
