#!/usr/bin/env python3

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation as a function
def dydx(y, x):
    
    # This function returns dy/dx given y and x, according to the specified equation
    return y / (np.exp(x) - 1)

# Define a recursive function for the Runge-Kutta 4th order method
def runge_kutta_recursive(x0, y0, h, steps, y_values=None, x_values=None):
    
    # Initialize lists for storing x and y values if not provided
    if y_values is None and x_values is None:
        y_values = [y0]
        x_values = [x0]
    
    # Check if the required number of steps has been reached
    if len(y_values) >= steps:
        return x_values, y_values
    
    # Calculate the next y value using the RK4 formula
    k1 = dydx(y0, x0)
    k2 = dydx(y0 + (h/2 * k1), x0 + h/2)
    k3 = dydx(y0 + (h/2 * k2), x0 + h/2)
    k4 = dydx(y0 + (h * k3), x0 + h)
    y_next = y0 + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    x_next = x0 + h
    
    # Append the next values to their respective lists
    y_values.append(y_next)
    x_values.append(x_next)
    
    # Recursively call the function for the next step
    return runge_kutta_recursive(x_next, y_next, h, steps, y_values, x_values)

# Set initial conditions and parameters
x0 = 1
y0 = 5
h = 0.02  # Step size
steps = 500  # Number of steps

# Solve the differential equation using RK4
rk4_x_values, rk4_y_values = runge_kutta_recursive(x0, y0, h, steps)

n = 0

# Print the first 5 solutions obtained with RK4
print("First 5 solutions using RK4:")
for i in range(6):
    print(f"n = {n}: x0 = {rk4_x_values[i]:.2f}, y0 ≈ {rk4_y_values[i]:.5f}")
    n += 1

# Solve the differential equation using the odeint method
x_values_odeint = np.linspace(x0, x0 + h * (steps - 1), steps)
odeint_solutions = odeint(dydx, y0, x_values_odeint)

n = 0

# Print the first 5 solutions obtained with odeint
print("\nFirst 5 solutions using odeint:")
for i in range(6):
    print(f"n = {n}: x0 = {x_values_odeint[i]:.2f}, y0 ≈ {odeint_solutions.flatten()[i]:.5f}")
    n += 1

# Plotting
plt.figure(figsize=(18, 5.4))

# Plot for RK4 solution
plt.subplot(1, 3, 1)
plt.plot(rk4_x_values, rk4_y_values, 'o-', label='RK4 Solution', markersize=3)
plt.title('RK4 Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Plot for odeint solution
plt.subplot(1, 3, 2)
plt.plot(x_values_odeint, odeint_solutions.flatten(), 'o', label='odeint Solution', markersize=3, linestyle='--', color='orange')
plt.title('odeint Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Plot comparing RK4 and odeint solutions
plt.subplot(1, 3, 3)
plt.plot(rk4_x_values, rk4_y_values, 'o-', label='RK4 Solution', markersize=2, linewidth=2, alpha=0.7)
plt.plot(x_values_odeint, odeint_solutions.flatten(), '^-', label='odeint Solution', markersize=2, color='orange', linewidth=2, alpha=0.7, markevery=10)
plt.title('RK4 vs odeint Solutions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()
