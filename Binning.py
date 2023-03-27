# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 09:33:28 2023

@author: olive
"""

import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

#Definere funktionen som funktion af bølgelængden(x), kontrasten ppm (y), 
#støjen (yerr) og binnings faktoren
def weighted_avg(x, y, yerr, binning_factor):
   
    #Tomt array
    y_avg_arr = []
    y_avg_err_arr = []
    x_avg_arr =[]

# Denne kode beregner den vægtede gennemsnit af arrays med den specifiseret binnings faktor


#'for' loopet itererer over intervallet af værdier i y, således at hver iteration dækker en del
#af y med størrelsen af binning faktoren
    for i in range(0, math.ceil(len(y) / binning_factor)):  
#loppet bruger den reciproke af kvadraterne af yerr-værdierne i chunken til at beregne den
#vægtet gennemsnitlig y_avg af y-værdier i intervallet.
        reciprocal_squares = 1 / (yerr[i * binning_factor:(i + 1) * binning_factor] ** 2)
#Koden beregner derefter fejlen i det vægtede gennemsnit y_avg_err, som er den reciproke
#af kvadratroden af ​​summen af ​​det reciproke af kvadraterne af yerr inden for intervallet.
        y_avg = np.sum(y[i * binning_factor:(i + 1) * binning_factor] * reciprocal_squares) / np.sum(
            reciprocal_squares)
#Værdierne y_avg og y_avg_err er opbevaret i arrays henholdsvis y_avg_arr og y_avg_err_arr.


#Derudover beregner loopen middelværdien af ​​x-værdierne inden for den samme del og tilføjer den til
#x_avg_arr array.
        y_avg_err = 1 / np.sqrt(np.sum(reciprocal_squares))
        y_avg_arr.append(y_avg)
        y_avg_err_arr.append(y_avg_err)

        x_avg_arr.append(np.mean(x[i * binning_factor:(i + 1) * binning_factor]))

#Til sidst returner funktionen tre arrays: x_avg_arr, y_avg_arr og y_avg_err_arr, som indeholder
#de indskrevne gennemsnit og fejl for input-arrays x, y og yerr.
    return x_avg_arr, y_avg_arr, y_avg_err_arr

#Definere dataet
x = np.loadtxt("psg_contrast_1b.txt")[:, 0] # Datapunkternes bølgelængder læses fra filen
y = np.loadtxt("psg_contrast_1b.txt")[:, 1]*10**6 # Værdien af datapunkterne aflæses
yerr = np.loadtxt("psg_contrast_1b.txt")[:, 2]*10**6 #Støjen fra datapunkterne aflæses
binning_factor=8 #Binnings faktoren defineres

alpha= weighted_avg(x, y, yerr, binning_factor) # Definere funktionen

#Plotter binningen (blå) og det oprindelig data (rød)
plt.figure()
plt.plot(x,y,"r")
plt.errorbar(alpha[0],alpha[1],yerr=alpha[2],fmt="o")
plt.title("Binning 1b")
plt.xlabel("Wavelength")
plt.ylabel("Binning")
plt-
plt.show

