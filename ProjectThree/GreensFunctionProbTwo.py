import numpy as np
import matplotlib.pyplot as plt

# Define the range for x (or t)
x = np.linspace(0, 2*np.pi, 1000)

# Homogeneous solution with C1 = 1 and C2 = 1
C1, C2 = 1, 1
yH = C1*np.cos(x) + C2*np.sin(x)

# Specific solution derived from Green's function
yG = 4*(np.sin(x)**2 + np.cos(x)**2 - np.cos(x))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, yH, label='Homogeneous Solution $y_H = C_1\cos(x) + C_2\sin(x)$')
plt.plot(x, yG, label="Green's Function Solution $y = 4(\sin^2(x) + \cos^2(x) - \cos(x))$", linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of Homogeneous and Green\'s Function Solutions')
plt.legend()
plt.grid(True)
plt.show()
