import numpy as np
import matplotlib.pyplot as plt

# Define the range for x (or t)
x = np.linspace(0, 2*np.pi, 1000)

# ODE 1 Solutions
C1_1, C2_1 = 0, 0  # Coefficients for the homogeneous solution of ODE 1
yH_1 = C1_1*np.cos(2*x) + C2_1*np.sin(2*x)  # Homogeneous solution for ODE 1
yG_1 = x/4 - (np.sin(2*x))/8  # Green's function solution for ODE 1

# ODE 2 Solutions
C1_2, C2_2 = 0, 0  # Coefficients for the homogeneous solution of ODE 2
yH_2 = C1_2*np.cos(x) + C2_2*np.sin(x)  # Homogeneous solution for ODE 2
yG_2 = -4*np.cos(x) + 4  # Green's function solution for ODE 2

# Plotting ODE 1 Solutions
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, yH_1, label='Homogeneous Solution $y_H = C_1\cos(2x) + C_2\sin(2x)$')
plt.plot(x, yG_1, label="Green's Function Solution $y = t/4 - (\sin(2t))/8$", linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution for ODE 1: $y''+4y=x$")
plt.legend()
plt.grid(True)

# Plotting ODE 2 Solutions
plt.subplot(1, 2, 2)
plt.plot(x, yH_2, label='Homogeneous Solution $y_H = C_1\cos(x) + C_2\sin(x)$')
plt.plot(x, yG_2, label="Green's Function Solution $y = -4\cos(t) + 4$", linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution for ODE 2: $y''+y=4$")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
