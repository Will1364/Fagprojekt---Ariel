# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 13:36:34 2023

@author: willi
"""
"""
Formålet med dette script er at udregne chi i anden fordelingen, 
som bruges til at sammenholde vores signal med hhv. modellen af spectret fra modellen atmosfæren og spektret fra den flade model.
"""
import math

def chiSquared(Signal,Model,flatModel,Uncertainty):
    
    chi_m = sum(((Signal-Model)/Uncertainty)**2)       #chi i anden udregnes for spektret
    chi_f = sum(((Signal-flatModel)/Uncertainty)**2)   #chi i anden udregnes for den flade model
    
    return chi_m, chi_f
