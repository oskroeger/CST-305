#!/usr/bin/env python3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# EQUATION:
# ---------------------------------------
# dT/dt = H(W)−C(T,A,F)
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

# Time points
t = np.linspace(0, 10, 100)  # 10 seconds

# Parameters
W = 0.7  # Workload (0 to 1)
k = 0.5  # Heat generation constant
c = 0.1  # Cooling efficiency
A = 25   # Ambient temperature (Celsius)
F = 1.0  # Cooling system efficiency (0 to 1)

# Initial condition
T0 = 30  # Initial CPU temperature (Celsius)

# Solve ODE
temperature = odeint(cpu_temperature, T0, t, args=(W, k, c, A, F))

# Visualization
plt.plot(t, temperature)
plt.xlabel('Time (seconds)')
plt.ylabel('CPU Temperature (Celsius)')
plt.title('CPU Temperature Over Time')
plt.show()

print(f"Change in Temperature / Change in Time (dT/dt):")

print(f"Workload = {W}")
print(f"Heat Generation Constant = {k}")
print(f"Cooling Efficiency = {c}")
print(f"Ambient Temperature = {A}")
print(f"Cooling System Efficiency = {F}")
