# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:54:18 2023

@author: William Hedegaard Langvad
"""
import numpy as np
import math
import matplotlib.pyplot as plt


Rs = 0.12*696340
Rp = 14012.4/2



Wavelength = np.loadtxt("Trappist1C_O2.txt")[:, 0]
signal = np.loadtxt("Trappist1C_O2.txt")[:, 1]


Transmittance = signal/((Rp/Rs)**2)

plt.plot(Wavelength, Transmittance)
plt.title("Transmittance spectrum Trappist system") 
plt.xlabel("wavelength [um]") 
plt.ylabel("Transmittance")
plt.show()
