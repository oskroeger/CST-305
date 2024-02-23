import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 10, 1000)

# Define the homogeneous solution for y"+4y=x
def y_h1(x, c1, c2):
    return c1 * np.cos(2*x) + c2 * np.sin(2*x)

# The arbitrary constants for y"+4y=x
c1 = 0
c2 = 0

# Define the homogeneous solution y"+y=4
def y_h2(x, c3, c4):
    return c3 * np.cos(x) + c4 * np.sin(x)

# The arbitrary constants for y"+y=4
c3 = 0
c4 = 0

# Calculate y values for y"+4y=x
y1 = y_h1(x, c1, c2)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label=f'y_h1(x) = {c1} * cos(2x) + {c2} * sin(2x)')
plt.xlabel('x')
plt.ylabel('y_h1(x)')
plt.title('Homogeneous Solution of y\'\' + 4y = x')
plt.legend()
plt.grid(True)
plt.show()

# Calculate y values for 
y2 = y_h2(x, c3, c4)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, y2,color='red', label=f'y_h2(x) = {c1} * cos(x) + {c2} * sin(x)')
plt.xlabel('x')
plt.ylabel('y_h2(x)')
plt.title('Homogeneous Solution of y\'\' + y = 4')
plt.legend()
plt.grid(True)
plt.show()