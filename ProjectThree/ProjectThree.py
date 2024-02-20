"""
Programmers: Owen Kroeger, Atu Ambala

Description:
The script compares solutions to two second-order ordinary differential equations using both direct integration 
and Green's method. It defines the equations, solves them numerically, and plots the results for comparison, 
demonstrating the different approaches to solving ODEs in Python.

Packages:
The script uses NumPy for numerical operations, SciPy's 'odeint' for solving the differential equation,
and Matplotlib for visualization.

Note:
The assigned ODEs are:

1. y"+4y=x;y(0)=y'(0)=0
2. y"+y=4; y(0)=y'(0)=0

"""

import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt

# Define the system for the first ODE y'' + 4y = x
def system1(u, x):
    u1, u2 = u
    du1dx = u2
    du2dx = x - 4*u1
    return [du1dx, du2dx]

# Define the system for the second ODE y'' + y = 4
def system2(u, x):
    u1, u2 = u
    du1dx = u2
    du2dx = 4 - u1
    return [du1dx, du2dx]

# Initial conditions
u0 = [0, 0]

# x array for which to solve
x = np.linspace(0, 10, 200)

# Solve both systems of ODEs
sol1 = odeint(system1, u0, x)
sol2 = odeint(system2, u0, x)

# Define the differential equation
def odes(t, y):
    return [y[1], -4*y[0] + t]

# Solve the differential equation
sol3 = solve_ivp(odes, [0, 10], [0, 0], t_eval=np.linspace(0, 10, 1000))

# Define the differential equation
def odes2(t, y):
    return [y[1], -y[0] + 4]

# Solve the differential equation
sol4 = solve_ivp(odes2, [0, 10], [0, 0], t_eval=np.linspace(0, 10, 1000))

# Plot both sets of solutions on the same plot
plt.figure(figsize=(10, 6))

plt.plot(x, sol1[:, 0], label='$y\'\' + 4y = x$ (ODE)', color='blue', linestyle='-')
plt.plot(x, sol2[:, 0], label='$y\'\' + y = 4$ (ODE)', color='red', linestyle='-')
plt.plot(sol3.t, sol3.y[0], label='$y\'\' + 4y = x$ (Green\'s Method)', color='green', linestyle='--')
plt.plot(sol4.t, sol4.y[0], label='$y\'\' + y = 4$ (Green\'s Method)', color='pink', linestyle='--')

plt.xlabel('x')
plt.ylabel('y(t)')
plt.title('Comparison of ODE and Green\'s Method Solutions')
plt.legend()

plt.grid(True)
plt.show()
