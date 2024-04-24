import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, summation, limit, oo


# ----------------------------------------------
# Part 1 - A
# ----------------------------------------------

# Define the function and interval
f = lambda x: np.sin(x) + 1
a, b = -np.pi, np.pi
x = np.linspace(a, b, 400)
y = f(x)

# Create plot
fig, axs = plt.subplots(3, 1, figsize=(8, 18))

# Subinterval partitions
n = 4
dx = (b - a) / n
x_sub = np.linspace(a, b, n + 1)

# Left-hand endpoint Riemann Sum
x_left = x_sub[:-1]
y_left = f(x_left)
axs[0].bar(x_left, y_left, width=dx, alpha=0.3, align='edge', edgecolor='b')
axs[0].plot(x, y, 'r-')
axs[0].set_title("Left-hand Endpoint Riemann Sum")

# Right-hand endpoint Riemann Sum
x_right = x_sub[1:]
y_right = f(x_right)
axs[1].bar(x_left, y_right, width=dx, alpha=0.3, align='edge', edgecolor='g')
axs[1].plot(x, y, 'r-')
axs[1].set_title("Right-hand Endpoint Riemann Sum")

# Midpoint Riemann Sum
x_mid = (x_left + x_right) / 2
y_mid = f(x_mid)
axs[2].bar(x_mid, y_mid, width=dx, alpha=0.3, color='yellow', align='center', edgecolor='purple')
axs[2].plot(x, y, 'r-')
axs[2].set_title("Midpoint Riemann Sum")

# Show plots
plt.tight_layout()
plt.show()

# ----------------------------------------------
# Part 1 - B (Not Necessary)
# ----------------------------------------------

# Define the symbols and function for the Riemann sum calculation
n, k = symbols('n k', integer=True)
x_k = k / n  # right-hand endpoint
f_xk = 3 * x_k + 2 * x_k**2  # f(x_k) = 3x + 2x^2
delta_x = 1 / n

# Define the Riemann sum
riemann_sum = summation(f_xk * delta_x, (k, 1, n))

# Calculate the limit as n approaches infinity
integral_limit = limit(riemann_sum, n, oo)

# Display the Riemann sum formula and the limit
riemann_sum, integral_limit
