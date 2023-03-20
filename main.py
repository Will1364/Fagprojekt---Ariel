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
colours = ["r","y","m","k"]

# Her definerer vi en liste med navne på hvert datasæt til vores plot
planets = ["trappist1b", "trappist1c", "trappist1e"]



# I nedestående loop plottes hvert datasæt et efter et

for i in range(0,len(planets)):
    Wavelength = np.loadtxt("psg_" + planets[i] + "_c.txt")[:, 0] # Datapunkternes bølgelængder læses fra filen
    Spectrum = np.loadtxt("psg_" + planets[i] + "_c.txt")[:, 1]*10**6 # Værdien af datapunkterne aflæses
    error = np.loadtxt("psg_" + planets[i] + "_c.txt")[:, 2]*10**6
    flatModel = np.loadtxt("psg_" + planets[i] + "_f.txt")[:, 1]*10**6

    
    Signal = SignalSimulater(Spectrum, error)
    chi = chiSquared(Signal, Spectrum, flatModel, error)
    deltaBIC = BIC(chi[0],chi[1],len(Signal))
    
    #avgBIC = np.array([])
    #for j in range(1000):
    #    Signal = SignalSimulater(Spectrum, error)
    #    chi = chiSquared(Signal, Spectrum, flatModel, error)
    #    deltaBIC = BIC(chi[0],chi[1],len(Signal))
    #    avgBIC = np.append(avgBIC,deltaBIC) 
    #deltaBIC = np.mean(avgBIC)
    
    
   
    print("dBIC for " + planets[i] + " er " + str(deltaBIC))
    
    #binnedData = binData(Wavelength, Signal, error, 8)
    
    plt.figure()
    plt.errorbar(Wavelength, Signal, yerr=error, label='both limits (default)')
    plt.plot(Wavelength, Signal, "bo", label = planets[i]) # Datasæt "i" plottes
    plt.plot(Wavelength, Spectrum, colours[i])
    plt.title("Transmittance spektrum " + planets[i]) # plottets titel defineres
    plt.xlabel("wavelength [um]")                       # x-aksens titel defineres
    plt.ylabel("Transmittance [ppm]")                         # y-aksens titel defineres 
    plt.show
   
    
    
