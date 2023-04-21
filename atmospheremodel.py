# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:24:50 2023

@author: mathi
"""

import numpy as np
import math
#import pandas as pd
import matplotlib.pyplot as plt

# fixed Molarmasses [kg/mol]
M_CO2 = 0.044009773
M_air = 0.029
M_O2 = 0.032


# Fixed surface pressure [Pa]
P_10bar = 10**6
P_1bar = 10**5
P_venus = 92*10**6

# fixed gravity g [m/s^2]
g_Tb = 7.94
g_Tc = 9.46
g_Td = 4.74
g_Te = 9.15
g_Tf = 8.37
g_Tg = 8.55

# Parameters for the atmosphere
M = M_CO2
T = 500
R = 8.314
g = g_Tb

N_A = 6.022*10**23
kb = 1.380649*10**(-23)

# specific gas constant
R_s = R / M

# surface pressure
P0 = P_10bar

# surface density
rho_0 = (P0) / (R_s * T)
#rho_0 = P0 / (R * T) * (M * 0.010794) / 1

# scale height H in meter [m]
H = (R_s*T) / (g)

# Pressure as a function of height z
P = []
rho = []


# Set the initial conditions
z0 = 0  # m

# Define the height range and step size
#z_start = z0
#z_end = 145090  # m
n_steps = 51
#dz = (z_end - z_start) / (n_steps - 1)

# Initialize arrays to store pressure and density
P = []
rho = []


# Loop over the height range and calculate pressure and density at each step
for z in range(0, 145091):
    P.append( P0 * np.exp((-g * z) / (R_s * T)) )
    rho.append( rho_0 * np.exp((-g * M * z) / (R * T)) ) 
    rho[z] = (N_A/M)*rho[z]
    
    print(P[z])
    print(rho[z])

# mangler at sætte den til 50 steps, så den kun har 50 forskellige værdier

plt.plot(P, range(0, 145091))
plt.xlabel("Pressure [Pa]")
plt.ylabel("Height")
plt.title("Atmospheric Pressure vs Height")
plt.show()


plt.plot(rho, range(0, 145091))
plt.xlabel('Density (kg/m^3)')
plt.ylabel('Height (m)')
plt.title('Density of an Isothermal CO2 Atmosphere')
plt.show()

N_A = 6.022*10**23

#rho = (N_A/M)*rho[z]

# Define the atmospheric profile
pressure = np.logspace(3, -3, num=50)  # Pressure in Pa
temperature = np.ones_like(pressure) * 273  # Temperature in K
density = pressure / (1.38e-23 * temperature)  # Density in m^-3

