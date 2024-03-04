"""
Programmers: Owen Kroeger, Atu Ambala

Description:
The code generates a plot illustrating the degradation of data + I/O in processors A and B over time. 
It begins by importing the necessary libraries for numerical computation and plotting. 
Next, it creates an array of time points from 0 to 30 and calculates the degradation 
of data + I/O using a specified formula. The degradation values are then plotted against 
the time points to visualize the trend over time. The x-axis is labeled as 'Time t', 
representing the time units used in the calculation, while the y-axis is labeled 
as 'Data + I/O in Processors A and B (MBytes)', indicating the amount of data + I/O in processors A and B. 
The plot provides a clear depiction of how the data + I/O degrades in processors A and B, 
starting from an initial value of 100 MBytes in each processor.

Packages:
The code uses two main packages:
1. NumPy: NumPy is used for numerical computations in Python. It provides support for arrays,
matrices, and mathematical functions that are essential for the calculations in the code.

2. Matplotlib.pyplot: Matplotlib is a plotting library for Python. The code specifically 
uses the pyplot module from Matplotlib to create the plot showing the degradation of data + I/O over time.


"""

import numpy as np
import matplotlib.pyplot as plt

# Original data + I/O in processors A and B
original_data_io = 100  # 100 MBytes

t = np.linspace(0, 30, 100)  # Time points from 0 to 30
x = original_data_io * (-np.exp(3*(t-1)/100) + 8*np.exp(-(t-1)/25))/7 # this the equaiton for x(t)

plt.plot(t, x)
plt.xlabel('Time t')
plt.ylabel('Data + I/O in Processors A and B (MBytes)')
plt.title('Data + I/O Degradation of Processors A and B over Time')
plt.show()
