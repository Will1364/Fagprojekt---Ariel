# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:54:13 2023

@author: willi
"""
import numpy as np
import math
import matplotlib.pyplot as plt

Wavelength = np.loadtxt("psg_rad_1b.txt")[:, 0]


def binData(Wavelength, Signal, Resolution):
    
    bins = [Wavelength[0]] # definerer en liste med grænser mellem bins
    
    
    # Det første loop i koden bruges til at definerede kasser/bins som dataen skal sorteres efter
    # binbredden er defineret efter R=Lambda/dLambda, hvor lambda er bølgelængden og R er den valgte opløsning
    
    
    for i in range(len(Wavelength)-2): 
        Lambda = Wavelength[i+1] # Bølgelængder defineres én for én
        binSize = Lambda/Resolution # binstørrelse for bølgelængde defineres ud fra R=Lambda/dLambda
        
        if (Lambda-binSize/2) > bins[-1]: # Hvis et bin ikke overlapper med andre definerede bins,
            bins.append(Lambda+binSize/2) # lægges pågældende bins øvre grænse til listen med bin grænser
            
    Xbinned = np.digitize(Wavelength, bins, right=False) #listen med bølgelængder opdeles inden for bingrænser
    
    binnedDatapoint = []
    binnedWavelengths = []
    
    
    # Det næste loop bruges til at indele datasættet i de binintervaller som blev defineret i første loop
    # Gennemsnittet af de datapunkter som falder inden for hvert bin udregnes, og disse værdier gemmes som vores nye datasæt
    
    for i in range(max(Xbinned)) # Dette loop binner datasættet et bin af gangen
        currentBin = Wavelength[Xbinned == i+1] # Bølgelængder der ligger inden for pågældende bin gemmes i liste
        binnedDatapoints = Signal[Wavelength == currentBin] # Signalet tilhørende binnets  bølgelængde interval gemmes i liste
        
        dataPoint = np.mean(binnedDatapoints) # gennemsnittet af signaler i pågældende bin udregnes og gemmes som nyt datapunkt
        binnedWavelength = np.mean(currentBin) # midten af binnet gemmes som bølgelængden tilhørende nyt datapunkt 
        
        binnedDatapoint.append(dataPoint)
        binnedWavelengths.append(binnedWavelength)
    return binnedDatapoint, binnedWavelengths



