# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:54:13 2023

@author: William
"""
import numpy as np
import math
import matplotlib.pyplot as plt
###################################################################################################################################
# Formålet med denne funktion er at binne et datasæt og derved reducere støj
# I funktionen insættes listen med målepunkternes bølgelængder (x-koordinaterne), samt målepunkternes y-koordinat og 

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
    
    
    y_avg = np.array([])
    x_avg = np.array([])
    y_avg_error = np.array([])
    
    # Det næste loop bruges til at indele datasættet i de binintervaller som blev defineret i første loop
    # Gennemsnittet af de datapunkter som falder inden for hvert bin udregnes, og disse værdier gemmes som vores nye datasæt
    Wavelength = np.array(Wavelength)
    Signal = np.array(Signal)
    
    # Det næste loop bruges til at indele datasættet i de binintervaller som blev defineret i første loop
    # Gennemsnittet af de datapunkter som falder inden for hvert bin udregnes, og disse værdier gemmes som vores nye datasæ
    
    for i in range(max(Xbinned)): # Dette loop binner datasættet et bin af gangen
        currentBin = np.zeros(len(Wavelength))
        currentBin[Xbinned == i+1] = Wavelength[Xbinned == i+1] # Bølgelængder der ligger inden for pågældende bin gemmes i liste
       
        RS = 1/(Noise[Wavelength == currentBin]**2)
       
        binnedDatapoints = np.sum(Signal[Wavelength == currentBin]*RS)/np.sum(RS) # Signalet tilhørende binnets  bølgelængde interval gemmes i liste
        
        
        y_avg = np.append(y_avg,binnedDatapoints) # gennemsnittet af signaler i pågældende bin udregnes og gemmes som nyt datapunkt
        x_avg = np.append(x_avg,np.mean(currentBin[currentBin > 0])) # midten af binnet gemmes som bølgelængden tilhørende nyt datapunkt 
        y_avg_error = np.append(y_avg_error,1/np.sqrt(np.sum(RS)))
        
    return y_avg, x_avg, y_avg_error



