#!/usr/bin/env python3

"""
File: ProjectSix.py

Programmers: Owen Kroeger, Atu Ambala

Description:
This comprehensive script integrates three distinct yet interrelated computational models:
1. The approximation of functions using Taylor series expansions.
2. The solution of a system of first-order differential equations that collectively model a second-order differential equation.
3. The modeling and visualization of CPU temperature changes over time under varying workloads.

The first part employs Taylor series expansions to approximate functions up to a specified degree, demonstrating the approximations for different inputs. The second part solves a system of first-order differential equations using SciPy's odeint, which effectively models a second-order differential equation related to a theoretical or practical problem. The third part utilizes a differential equation to model the dynamic balance between heat generation and cooling in a CPU, providing insights into thermal management strategies.

Key Equations:
- Taylor series for function approximation.
- A system of first-order differential equations to model a second-order differential equation.
- dT/dt = k * W^2 - c * F * (T - A) for CPU temperature, where T is the temperature, W is the workload, k is the heat generation constant, c is the cooling efficiency, A is the ambient temperature, and F is the cooling system efficiency.

Packages:
The script uses NumPy for numerical operations, SciPy's 'odeint' for solving differential equations, and Matplotlib for visualization. It visualizes the Taylor series approximations, the solution of the differential equation system, and the CPU temperature dynamics, highlighting the utility of mathematical models in understanding complex systems.

Components:
- Taylor series functions: Approximate given functions using Taylor series expansions.
- A system of first-order differential equations solver: Models a second-order differential equation numerically.
- cpu_temperature function: Calculates the rate of change in temperature due to workload and cooling efficiency.
- Parameters setup: Defines constants and initial conditions for all parts.
- Solving ODE: Computes CPU temperature on coarse and fine grids, as well as solves a system of differential equations.
- Interpolation: Maps the coarser solution to a finer grid for the CPU temperature model.
- Visualization: Includes plots for Taylor series approximations, solutions to differential equations, and CPU temperature changes over time, alongside estimation error analysis.

Usage:
Run this script within a Python 3 environment with NumPy, SciPy, and Matplotlib installed. Execute the script using 'python ProjectSix.py'. The output includes graphical representations of function approximations using Taylor series, solutions to a system of differential equations, and CPU temperature changes under varying workloads, illustrating the practical application of these mathematical models.

Note:
The explicit and functional forms of the CPU temperature equation (dT/dt = k * W^2 - c * F * (T - A) and dT/dt = H(W)−C(T,A,F)) represent the same physical phenomenon in different mathematical expressions.
"""


import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Part 1: Taylor Series Expansion
# ==================================================================================

def taylor_series_part1(x):
    """Taylor series up to n<=4 for the first part of the assignment."""
    return 1 - x - (1/3)*x**3 - (1/12)*x**4

def taylor_series_part2(x):
    """Second-order Taylor polynomial near x=3 for the second part of the assignment."""
    # Given the derivatives and their values at x=3: y(3)=6, y'(3)=1, y''(3)=-11
    # Taylor polynomial: f(x) = 6 + (x - 3) - 11/2*(x - 3)^2
    return 6 + (x - 3) - 11/2 * (x - 3)**2

# Evaluate and print the results for specific points
x_part1 = 3.5
y_part1 = taylor_series_part1(x_part1)
print(f"Part 1: Value of the Taylor series at x = {x_part1} is approximately {y_part1:.3f}")

# Visualization
plt.figure(figsize=(14, 7))

# Part 1
plt.subplot(1, 2, 1)
x_vals_part1 = np.linspace(-2, 5, 400)
y_vals_part1 = taylor_series_part1(x_vals_part1)
plt.plot(x_vals_part1, y_vals_part1, label='Taylor Series - n<=4')
plt.scatter([x_part1], [y_part1], color='red', zorder=5)
plt.text(x_part1, y_part1, f'({x_part1}, {y_part1:.3f})', color='black', verticalalignment='bottom')
plt.title('Part 1: Taylor Series Expansion at x=3.5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
# Display the Taylor polynomial equation for Part 1
plt.text(-2, -30, "f(x) = 1 - x - 1/3x^3 - 1/12x^4", fontsize=12, color='blue')

# Part 2
plt.subplot(1, 2, 2)
x_vals_part2 = np.linspace(2, 4, 400)
y_vals_part2 = taylor_series_part2(x_vals_part2)
plt.plot(x_vals_part2, y_vals_part2, label='2nd Order Taylor Polynomial near x=3')
plt.title('Part 2: 2nd Order Taylor Polynomial')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
# Display the Taylor polynomial equation for Part 2
plt.text(2, 4, "f(x) = 6 + 1(x - 3) - 11/2(x - 3)^2", fontsize=12, color='blue')

plt.tight_layout()
plt.show()


# Part 2: Power Series
# ==================================================================================
def solve_differential_equation(x):
    n = 8  # Solve for n <= 8
    a = np.zeros(n+1)  # Coefficients
    a[0] = 1  # Initial condition, y(0) = 1

    for i in range(1, n+1):
        a[i] = -a[i-2] / 4*((i-1) * (i))

    y = sum(a[i] * x**i for i in range(n+1))
    return y

# Example usage
x_value = 0
result = solve_differential_equation(x_value)
print ("--------------------------------------------")
print("Part 2: value of", f"y({x_value}) = {result}")

# Define the system of first-order differential equations
def model(y, x):
    y0, y1 = y
    dydx = [y1, (x - (x**2 + 4)*y0)/(x**2 + 4)]
    return dydx

# Initial conditions
y0 = [0, 1]  # y(0) = 0, y'(0) = 1

# Array of x values
x = np.linspace(0, 10, 100)

# Solve the differential equation using odeint
y = odeint(model, y0, x)

# Plot the solution
plt.figure(figsize=(12, 6))
plt.plot(x, y[:, 0], label='y(x)')
plt.plot(x, y[:, 1], label="y'(x)")
plt.title("Solving a Second-Order Differential Equation Numerically Using the odeint Solver")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


# Part 3: CPU Temperature Simulation
# ==================================================================================

# DIFFERENTIAL EQUATION (Explicit Form):
# ---------------------------------------
# dT/dt = k * W^2 - c * F * (T - A)
# ---------------------------------------

def cpu_temperature(T, t, W, k, c, A, F):

    """Function that will calculate the change in CPU temperature
	Equation (Functional Form): dT/dt = H(W)−C(T,A,F)
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

# Print statements for parameters
print("\n------------------------------------------------\n")
print("Part 3: Parameters - ")
print(f"Workload (W): {W}")
print(f"Heat generation constant (k): {k}")
print(f"Cooling efficiency (c): {c}")
print(f"Ambient temperature (A): {A} Celsius")
print(f"Cooling system efficiency (F): {F}")

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
