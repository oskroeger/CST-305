#!/usr/bin/env python3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# DIFFERENTIAL EQUATION:
# ---------------------------------------
# dT/dt = k * W^2 - c * F * (T - A)
# ---------------------------------------

def cpu_temperature(T, t, W, k, c, A, F):

    """Function that will calculate the change in CPU temperature
	Equation: dT/dt = H(W)−C(T,A,F)
	dT = change in temperature
	dt = change in time
	H(W) = function represented heat generation as a function of workload W
	C(T,A,F) = function representing cooling as a function of temperature T, 
	ambient temperature A, and fan speed/cooling system efficiency F."""
    # Heat generation
    heat_generated = k * W**2

    # Cooling effect
    cooling_effect = c * F * (T - A)

    # Change in temperature
    dTdt = heat_generated - cooling_effect
    return dTdt

# Parameters
W = 0.7  # Workload (0 to 1)
k = 0.5  # Heat generation constant
c = 0.1  # Cooling efficiency
A = 25   # Ambient temperature (Celsius)
F = 1.0  # Cooling system efficiency (0 to 1)

# Initial condition
T0 = 30  # Initial CPU temperature (Celsius)

# Solve ODE on Coarser Grid
t_coarse = np.linspace(0, 10, 100)  # Coarser grid
temp_coarse = odeint(cpu_temperature, T0, t_coarse, args=(W, k, c, A, F))

# Solve ODE on Finer Grid
t_fine = np.linspace(0, 10, 1000)  # Finer grid
temp_fine = odeint(cpu_temperature, T0, t_fine, args=(W, k, c, A, F))

# Interpolate Coarser Solution to Finer Grid
interpolate_coarse = interp1d(t_coarse, temp_coarse[:, 0], kind='cubic')
temp_coarse_interpolated = interpolate_coarse(t_fine)

# Calculate Error
error = np.abs(temp_fine[:, 0] - temp_coarse_interpolated)

# Visualization
plt.figure(figsize=(12, 6))

# Subplot 1: Temperature
plt.subplot(1, 2, 1)
plt.plot(t_coarse, temp_coarse, label='Coarser Grid')
plt.plot(t_fine, temp_fine, label='Finer Grid', linestyle='--')
plt.xlabel('Time (seconds)')
plt.ylabel('CPU Temperature (Celsius)')
plt.title('CPU Temperature Over Time')
plt.legend()

# Subplot 2: Error
plt.subplot(1, 2, 2)
plt.plot(t_fine, error)
plt.xlabel('Time (seconds)')
plt.ylabel('Error')
plt.title('Estimation Error')

plt.tight_layout()
plt.show()
