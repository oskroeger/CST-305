import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from scipy.integrate import quad

# ----------------------------------------------
# Part 1 - A
# ----------------------------------------------

# Define the function and interval
f = lambda x: np.sin(x) + 1
a, b = -np.pi, np.pi
x = np.linspace(a, b, 400)
y = f(x)

# Create plot side by side
fig, axs = plt.subplots(1, 3, figsize=(18, 6))  # Adjust subplot to horizontal layout

# Subinterval partitions
n = 4
dx = (b - a) / n
x_sub = np.linspace(a, b, n + 1)

# Left-hand endpoint Riemann Sum
x_left = x_sub[:-1]
y_left = f(x_left)
axs[0].bar(x_left, y_left, width=dx, alpha=0.3, align='edge', edgecolor='blue', color='cyan')
axs[0].plot(x, y, 'r-')
axs[0].set_title("Left-hand Endpoint Riemann Sum")

# Right-hand endpoint Riemann Sum
x_right = x_sub[1:]
y_right = f(x_right)
axs[1].bar(x_left, y_right, width=dx, alpha=0.3, align='edge', edgecolor='green', color='lightgreen')
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
# Part 2
# ----------------------------------------------

# Time in minutes
times = np.arange(0, 31)  # 0 to 30 minutes

# Rates in MB/s
rates = np.array([24.5, 23.0, 25.5, 22.8, 22.7, 25.2, 24.7, 23.9, 25.1, 25.2, 25.4, 25.3, 24.8, 24.6, 25.7, 25.8, 25.9, 24.9, 25.3, 25.5, 24.8, 23.6, 24.9, 25.1, 25.0, 25.2, 24.8, 24.2, 24.3, 25.4, 25.6])

# Define the function R(t) using cubic spline interpolation
R = CubicSpline(times, rates)

# Plotting R(t)
t_fine = np.linspace(0, 30, 300)
plt.figure(figsize=(10, 5))
plt.plot(t_fine, R(t_fine), label='Interpolated Download Rate')
plt.scatter(times, rates, color='red', label='Recorded Rates')
plt.title('Download Rate Over Time')
plt.xlabel('Time (minutes)')
plt.ylabel('Rate (MB/s)')
plt.legend()
plt.grid(True)
plt.show()

# Numerical integration with increased subdivisions
total_data_MB, error = quad(lambda t: R(t), 0, 30, limit=100)
total_data_MB *= 60  # Convert minutes to seconds

# Print the corrected total data downloaded
print(f"Total data downloaded over 30 minutes: {total_data_MB:.2f} MB")
print(f"Estimation error of the integration: {error:.2e}")
