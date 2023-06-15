# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:59:25 2023

"""
import numpy as np
import math
import matplotlib.pyplot as plt
from binData import binData
from Chi_squared import chiSquared
from BIC_funktion import BIC
from SignalSim import SignalSimulater
from Signal2Noise import SN

# Her beskrives de farver som bruges i plottet
colours = ["r","y","m","k","g","c"]

# Her definerer vi en liste med navne på hvert datasæt til vores plot
planets = ["trappist1b", "trappist1c", "trappist1e"]
#planets = ["LTT1445Ab_2","LTT1445Ab_5","LTT1445Ab_10"]
#planets = ["GJ1214b_2","GJ1214b_5","GJ1214b_10"]

atmospheres = ["CO2"]
#atmospheres = ["CO2","C02_clouds","O2_outgassing","Aqua"]
#atmospheres = ["CO2","CO2_clouds","O2_outgassing","vand","Neptun"]



for i in range(0,len(planets)):
    for j in range(len(atmospheres)):
        Wavelength = np.loadtxt("psg_" + planets[i] + "_" + atmospheres[j] + "_c.txt")[:, 0] # Datapunkternes bølgelængder læses fra filen
        Spectrum = np.loadtxt("psg_" + planets[i] + "_" + atmospheres [j] + "_c.txt")[:, 1]*10**6 # Spektret læses fra filen
        error = np.loadtxt("psg_" + planets[i] + "_" + atmospheres [j] + "_c.txt")[:, 2]*10**6 #Støjen læses fra filen
        flatModel = np.mean(Spectrum) #den flade model som bruges til at regne S/N defineres som en flad linje med middelværdi magen til spektrets.
        
        S2N = SN(flatModel, Spectrum, error) #S/N udregnes for spektret.
    
        print("S/N for " + planets[i] + "med" + atmospheres[j] + "atmosfæretype er " + str(S2N)) 
        
        
        Signal = SignalSimulater(Spectrum, error) # Et signal simuleres ud fra spektret og det forventede støjniveau
        binnedData = binData(Wavelength, Signal, error, 14) # Signalet binnes
    
        diff = max(Spectrum)-min(Spectrum) #Højden af spektret udregnes, da det skal bruges til at skalere y-aksen på graferne
        
        plt.figure(0)    #Et plot med alle atmosfærespektrene skabes
        plt.plot(Wavelength, Spectrum, colours[i], label = planets[i]) # Datasæt "i" plottes
        plt.title("Transmittance spektrum CO2 baseret atmosfærer") # plottets titel defineres
        plt.xlabel("wavelength [um]")                       # x-aksens titel defineres
        plt.ylabel("Transmittance [ppm]")                         # y-aksens titel defineres
        plt.legend()                            # legend med titel 
        plt.show
    
        plt.figure()      #Et plot for hvert spektrum og tilhørende signal skabes
        plt.errorbar(Wavelength, Signal,fmt=' ', yerr=error, label='both limits (default)')
        plt.plot(Wavelength, Signal, "b.", label = planets[i]) # Datasæt "i" plottes
        plt.plot(Wavelength, Spectrum, colours[i])
        plt.title("Transmittance spektrum " + planets[i] + " " + atmospheres[j]) # plottets titel defineres
        plt.xlabel("wavelength [um]")                     # x-aksens titel defineres
        plt.ylabel("Transmittance [ppm]")                 # y-aksens titel defineres 
        plt.ylim(np.mean(Spectrum)-diff,np.mean(Spectrum)+diff)
        plt.show
    
        plt.figure()     #Et plot for hvert spektrum og tilhørende binnede signal skabes
        plt.errorbar(binnedData[1], binnedData[0],fmt=' ', yerr=binnedData[2], label='both limits (default)')
        plt.plot(binnedData[1], binnedData[0], "b.", label = planets[i]) # Datasæt "i" plottes
        plt.plot(Wavelength, Spectrum, colours[i])
        plt.title("Transmittance spektrum " + planets[i] + " " + atmospheres[j]) # plottets titel defineres
        plt.xlabel("wavelength [um]")                     # x-aksens titel defineres
        plt.ylabel("Transmittance [ppm]")                 # y-aksens titel defineres 
        plt.ylim(np.mean(Spectrum)-diff,np.mean(Spectrum)+diff)
        plt.show
    
    
    
