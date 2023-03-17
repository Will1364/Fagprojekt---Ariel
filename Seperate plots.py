# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:59:25 2023

@author: willi
"""
import numpy as np
import math
import matplotlib.pyplot as plt
from binData import binData
from Chi_squared import chiSquared
from BIC_funktion import BIC
from SignalSim import SignalSimulater

# Her beskrives de farver som bruges i plottet
colours = ["r","b","g","y","c","m","k"]

# Her definerer vi en liste med navne på hvert datasæt til vores plot
planets = ["Trappist 1b", "Trappist 1c", "Trappist 1e"]



# I nedestående loop plottes hvert datasæt et efter et

for i in range(0,len(planets)):
    Wavelength_t = np.loadtxt("psg_" + planets[i] + "_c")[:, 0] # Datapunkternes bølgelængder læses fra filen
    Spectrum = np.loadtxt("psg_" + planets[i] + "_c")[:, 1]*10**6 # Værdien af datapunkterne aflæses
    error = np.loadtxt("psg_" + planets[i] + "_c")[:, 2]*10**6
    flatModel = np.loadtxt("psg_" + planets[i] + "_f")[:, 1]*10**6

    
    Signal = SignalSimulater(Spectrum, error)
    chi = chiSquared(Signal, Spectrum, flatModel, error)
    deltaBIC = BIC(chi[0],chi[1],len(Signal))
    
    
   
    print("dBIC for " + labels[i] + "er" + str(deltaBIC))
    
    #binnedData = binData(Wavelength, Signal, error, 8)
    
    plt.figure(1)
    plt.errorbar(Wavelength, Signal, yerr=error, label='both limits (default)')
    plt.plot(Wavelength, Signal, "bo", label = planets[i]) # Datasæt "i" plottes
    plt.plot(Wavelength, Spectrum, color[i])
    plt.title("Transmittance spektrum " + planets[i]) # plottets titel defineres
    plt.xlabel("wavelength [um]")                       # x-aksens titel defineres
    plt.ylabel("Transmittance [ppm]")                         # y-aksens titel defineres 
    plt.show
   
    
    
