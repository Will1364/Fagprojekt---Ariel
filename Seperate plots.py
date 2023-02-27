# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:59:25 2023

@author: willi
"""
import numpy as np
import math
import matplotlib.pyplot as plt

# Her beskrives de farver som bruges i plottet
colours = ["r.","b.","g.","y.","c.","m.","k."]


###############################################################################
#CO2 baserede atmosfærer
###############################################################################

# Her Skriver vi en liste over filnavne
filenames = ["psg_rad_1b.txt","psg_rad_1c.txt", "psg_rad_1e.txt"]

# Her definerer vi en liste med navne på hvert datasæt til vores plot
#labels = ["1 bar H20 (N=50)", "1 bar H20 cloudy (N=90)", "10 bar CO2 (N=30)", "10 bar Venus (N=120)"]
labels = ["Trappist 1b", "Trappist 1c", "Trappist 1e"]



# I nedestående loop plottes hvert datasæt et efter et

for i in range(0,len(filenames)):
    Wavelength = np.loadtxt(filenames[i])[:, 0] # Datapunkternes bølgelængder læses fra filen
    Transmittance = np.loadtxt(filenames[i])[:, 1]*10**6 # Værdien af datapunkterne aflæses
    error = np.loadtxt(filenames[i])[:, 2]*10**6
    plt.figure()
    
    plt.errorbar(Wavelength, Transmittance, yerr=error, label='both limits (default)')
    plt.plot(Wavelength, Transmittance, colours[i], label = labels[i]) # Datasæt "i" plottes
    plt.title("Transmittance spektrum " + labels[i]) # plottets titel defineres
    plt.xlabel("wavelength [um]")                       # x-aksens titel defineres
    plt.ylabel("Transmittance [ppm]")                         # y-aksens titel defineres 
    plt.show
