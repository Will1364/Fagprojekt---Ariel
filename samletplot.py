# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:54:18 2023

@author: William Hedegaard Langvad
"""
"""
Formålet med dette script er at kunen sammenligne flere simuleringer i et samlet plot.
Vil man eksempelvis vise spektret på både Trappist 1c og trappist 1e i et plot kan man bruge dette script.
"""
import numpy as np
import math
import matplotlib.pyplot as plt
# Her beskrives de farver som bruges i plottet
colours = ["ro","bo","go","yo","co","mo","ko"]


###############################################################################
#CO2 baserede atmosfærer
###############################################################################

# Her Skriver vi en liste over filnavne
filenames = ["psg_rad_1b.txt","psg_rad_1c.txt", "psg_rad_1e.txt"]

# Her definerer vi en liste med navne på hvert datasæt til vores plot
#labels = ["1 bar H20 (N=50)", "1 bar H20 cloudy (N=90)", "10 bar CO2 (N=30)", "10 bar Venus (N=120)"]
labels = ["Trappist 1b", "Trappist 1c", "Trappist 1d", "Trappist 1e", "Trappist 1f"]




# I nedestående loop plottes hvert datasæt et efter et
plt.figure()
for i in range(0,len(filenames)):
    Wavelength = np.loadtxt(filenames[i])[:, 0] # Datapunkternes bølgelængder læses fra filen
    Transmittance = np.loadtxt(filenames[i])[:, 1]*10**6 # Værdien af datapunkterne aflæses
    error = np.loadtxt(filenames[i])[:, 2]*10**6
    
    plt.errorbar(Wavelength, Transmittance, yerr=error)
    plt.plot(Wavelength, Transmittance, colours[i], label = labels[i]) # Datasæt "i" plottes

plt.title("Transmittance spektrum CO2 baseret atmosfærer") # plottets titel defineres
plt.xlabel("wavelength [um]")                       # x-aksens titel defineres
plt.ylabel("Transmittance [ppm]")                         # y-aksens titel defineres
plt.legend()                            # legend med titel 
plt.show
