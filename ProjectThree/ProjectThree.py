import numpy as np
from scipy.integrate import odeint
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

# Plotting
plt.figure(figsize=(10, 6))  # Set figure size for better readability

plt.plot(x, sol1[:, 0], label='$y\'\' + 4y = x$', color='blue')
plt.plot(x, sol2[:, 0], label='$y\'\' + y = 4$', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Solutions of Differential Equations')
plt.legend()

plt.grid(True)  # Add a grid for easier visualization
plt.show()
