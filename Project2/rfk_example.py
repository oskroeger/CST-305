import numpy as np
from scipy.integrate import odeint

def dydx(y, x):
    return y / (np.exp(x) - 1)  # Modified equation

def runge_kutta_recursive(x0, y0, h, steps, y_values=[], x_values=[]):
    if len(y_values) >= steps:
        return x_values, y_values  # Return both x and y values

    k1 = dydx(y0, x0)
    k2 = dydx(y0 + (h/2 * k1), x0 + h/2)
    k3 = dydx(y0 + (h/2 * k2), x0 + h/2)
    k4 = dydx(y0 + (h * k3), x0 + h)
    
    y_next = y0 + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    x_next = x0 + h

    y_values.append(y_next)
    x_values.append(x_next)  # Store the next x value

    return runge_kutta_recursive(x_next, y_next, h, steps, y_values, x_values)

# Initial conditions and parameters
x0 = 1
y0 = 5
h = 0.02
pts = 5  # Number of points to calculate, now including x0/y0 so we calculate one less

# Solve using RK4
rk4_x_values, rk4_solutions = runge_kutta_recursive(x0, y0, h, pts)
print("RK4 x values:", [x0] + rk4_x_values)  # Include initial x0
print("RK4 Solutions for y values:", [y0] + rk4_solutions)  # Include initial y0


# Solve using odeint
x_values = np.linspace(x0, x0 + h * (pts - 1), pts)  # Array of x values
odeint_solutions = odeint(dydx, y0, x_values, tfirst=True)

print("odeint Solutions for the first", pts, "points are:", odeint_solutions[:, 0])

# Compare the results
differences = np.abs(np.array(rk4_solutions) - odeint_solutions[:, 0])
print("Differences:", differences)
