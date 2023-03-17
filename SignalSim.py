# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 10:09:38 2023

@author: Mathilde Saltoft 
"""

##############################################################################
## Author : MAthilde Saltoft Schou

# packeges for calc and script

import numpy as np
import matplotlib.pyplot as plt

# The function for adding randomrumbers to the data points

# define array of data points
#Wavelength = np.loadtxt(filename)[:, 0]
#Spectrum = np.loadtxt(filename)[:, 1]*10**6
#Noise = np.loadtxt(filename)[:, 2]*10**6


def SignalSimulater(Spectrum, Noise):
    n = len(Spectrum)
    #np.random.seed(69314)     # Seed to check code
    
    RNDvector = np.array([])
    
    for i in range(0, n):
        RND = np.random.normal(0, Noise[i],1)   # Generate Random nomber (RND) from norm dist with s = noise
        print(RND)
        RNDvector = np.append(RNDvector,RND)    # Create vector from RND
    
    
    Signal = Spectrum + RNDvector       #Calculate Signal by adding random numbers to spectrum
    return Signal

#Signal = SignalSimulater(Spectrum, Noise)

#plt.figure()
#plt.plot(Wavelength, Signal, "bo")
#plt.plot(Wavelength, Spectrum, "r")
#plt.show()
