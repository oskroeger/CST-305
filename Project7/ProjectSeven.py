import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
plt.figure(figsize=(10, 6))
plt.plot(arrival_times, service_start_times, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Service Start Time')
plt.title('Arrival Time vs Service Start Time')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(arrival_times, exit_times, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Exit Time')
plt.title('Arrival Time vs. Exit Time')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(arrival_times, time_in_queue, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Time in Queue')
plt.title('Arrival Time vs. Time in Queue')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(arrival_times, num_in_system, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Number in System')
plt.title('Arrival Time vs. Number in System')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(arrival_times, num_in_queue, marker='o')
plt.xlabel('Arrival Time')
plt.ylabel('Number in Queue')
plt.title('Arrival Time vs. Number in Queue')
plt.grid(True)
plt.show()
