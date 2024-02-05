import numpy as np
from scipy.integrate import odeint

def dydx(y, x):
    return x + y

def runge_kutta_recursive(x0, y0, h, steps, y_values=[]):
    if len(y_values) >= steps:
        return y_values

    k1 = dydx(y0, x0)
    k2 = dydx(y0 + (h/2 * k1), x0 + h/2)
    k3 = dydx(y0 + (h/2 * k2), x0 + h/2)
    k4 = dydx(y0 + (h * k3), x0 + h)
    
    print("K1: ", k1)
    print("K2: ", k2)
    print("K3: ", k3)
    print("K4: ", k4)

    y_next = y0 + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)
    y_values.append(y_next)

    return runge_kutta_recursive(x0 + h, y_next, h, steps, y_values)

# Example usage
x0 = 0
y0 = 1
h = 0.1
pts = 5  # Number of points to calculate

# Solve using RK4
rk4_solutions = runge_kutta_recursive(x0, y0, h, pts)
print("RK4 Solutions for the first", pts, "points are:", rk4_solutions)

# Solve using odeint
x_values = np.linspace(x0, x0 + h * (pts - 1), pts)  # Array of x values
odeint_solutions = odeint(dydx, y0, x_values, tfirst=True)

print("odeint Solutions for the first", pts, "points are:", odeint_solutions[:, 0])

# Compare the results
differences = np.abs(np.array(rk4_solutions) - odeint_solutions[:, 0])
print("Differences:", differences)
