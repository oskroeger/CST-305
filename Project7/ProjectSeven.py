#!/usr/bin/env python3

"""
File: ProjectSix.py

Programmers: Owen Kroeger, Atu Ambala
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D     # noqa: F401 unused import

# ==================================================================================
# Part 1: Lorenz System
# ==================================================================================

# Function to compute derivatives of the Lorenz system
def lorenz(x, y, z, s=10, r=28, b=2.667):
    # Compute the derivatives
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# Function to simulate and plot the Lorenz system
def plot_lorenz(r, title):
    dt = 0.01
    num_steps = 10000
    
    # Arrays to store the values of x, y, and z
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)
    
    # Initial conditions
    xs[0], ys[0], zs[0] = (0., 1., 1.05)
    
    # Iterate to compute the trajectory
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r=r)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)
    
    # Create a figure for plotting
    fig = plt.figure(figsize=(10, 8))
    
    # Plot the 3D trajectory
    ax = fig.add_subplot(221, projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    
    # Plot the X variable over time
    ax2 = fig.add_subplot(222)
    ax2.plot(xs)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('X')
    ax2.set_title('X Plot')
    
    # Plot the Y variable over time
    ax3 = fig.add_subplot(223)
    ax3.plot(ys)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Y')
    ax3.set_title('Y Plot')
    
    # Plot the Z variable over time
    ax4 = fig.add_subplot(224)
    ax4.plot(zs)
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Z')
    ax4.set_title('Z Plot')
    
    # Adjust layout and display the plot
    plt.tight_layout(pad=3.0)
    plt.suptitle(title, fontsize=16)
    plt.subplots_adjust(top=0.9)
    plt.show()

# Plot for each scenario
plot_lorenz(28, "Chaotic")       # Plot for chaotic scenario
plot_lorenz(10, "Semi-Chaotic")  # Plot for semi-chaotic scenario
plot_lorenz(0, "Non-Chaotic")    # Plot for non-chaotic scenario

# ==================================================================================
# Part 2: Lorenz System Models
# ==================================================================================
k
# ------------------
# Part 2 - 1
# ------------------

# Arrival times and service durations
arrival_times = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
service_durations = np.array([2.22, 1.76, 2.13, 0.14, 0.76, 0.70, 0.47, 0.22, 0.18, 2.41, 0.41, 0.46, 1.37, 0.27, 0.27])
time_in_queue = np.array([0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0])
num_in_queue = np.array([0, 0, 1, 1, 1, 2, 3, 2, 1, 0, 0, 1, 0, 0, 0])

# Data arrays for plotting
service_start_times = np.array([1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10.0, 12.41, 12.82, 13.28, 14.65, 15.0])
exit_times = np.array([3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27])
time_in_queue = np.array([0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.4, 0, 1.41, 0.82, 0.28, 0.65, 0])
num_in_system = np.array([0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0])

L_q_A = np.mean(num_in_queue)
print(f'L_q_A = ', L_q_A)

L_q = round(np.sum(time_in_queue) / 15.27, 4)
print(f'L_q = ', L_q)

# Plotting
# Arrival Time vs Start Time
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, service_start_times, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Service Start Time')
plt.title('Arrival Time vs Service Start Time')
plt.grid(True)
plt.show()

# Arrival Time vs Exit Time
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, exit_times, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Exit Time')
plt.title('Arrival Time vs. Exit Time')
plt.grid(True)
plt.show()

# Arrival Time vs Time in Queue
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, time_in_queue, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Time in Queue')
plt.title('Arrival Time vs. Time in Queue')
plt.grid(True)
plt.show()

# Arrival Time vs Number in System
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, num_in_system, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Number in System')
plt.title('Arrival Time vs. Number in System')
plt.grid(True)
plt.show()

# Arrival Time vs Number in Queue
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, num_in_queue, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Number in Queue')
plt.title('Arrival Time vs. Number in Queue')
plt.grid(True)
plt.show()

# ------------------
# Part 2 - 3
# ------------------

# Initial parameters
lambda_initial = 10  # initial arrival rate, e.g., 10 packets per second
mu_initial = 20      # initial service rate, e.g., 20 packets per second

# Range for k
k_values = np.arange(1, 11, 1)  # k from 1 to 10

# Metrics calculations
utilization = [lambda_initial / mu_initial] * len(k_values)  # Utilization does not change
throughput = [k * lambda_initial for k in k_values]  # Throughput increases linearly with k
mean_number_in_system = [lambda_initial / mu_initial / (1 - lambda_initial / mu_initial)] * len(k_values)  # E[N] does not change
mean_time_in_system = [1 / (k * (mu_initial - lambda_initial)) for k in k_values]  # E[T] decreases with k

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs[0, 0].plot(k_values, utilization, marker='o')
axs[0, 0].set_title('Utilization ($\\rho$)')
axs[0, 0].set_xlabel('k')
axs[0, 0].set_ylabel('Utilization')

axs[0, 1].plot(k_values, throughput, marker='o', color='g')
axs[0, 1].set_title('Throughput ($X$)')
axs[0, 1].set_xlabel('k')
axs[0, 1].set_ylabel('Throughput')

axs[1, 0].plot(k_values, mean_number_in_system, marker='o', color='r')
axs[1, 0].set_title('Mean Number in System ($E[N]$)')
axs[1, 0].set_xlabel('k')
axs[1, 0].set_ylabel('Mean Number in System')

axs[1, 1].plot(k_values, mean_time_in_system, marker='o', color='m')
axs[1, 1].set_title('Mean Time in System ($E[T]$)')
axs[1, 1].set_xlabel('k')
axs[1, 1].set_ylabel('Mean Time in System')

fig.tight_layout()
plt.show()
