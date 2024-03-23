import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

def plot_lorenz(r, title):
    dt = 0.01
    num_steps = 10000
    
    xs = np.empty(num_steps + 1)
    ys = np.empty(num_steps + 1)
    zs = np.empty(num_steps + 1)
    
    xs[0], ys[0], zs[0] = (0., 1., 1.05)
    
    for i in range(num_steps):
        x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r=r)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)
    
    # 3D plot
    fig = plt.figure(figsize=(10, 8))
    
    ax = fig.add_subplot(221, projection='3d')
    ax.plot(xs, ys, zs, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")
    
    # X plot
    ax2 = fig.add_subplot(222)
    ax2.plot(xs)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('X')
    ax2.set_title('X Plot')
    
    # Y plot
    ax3 = fig.add_subplot(223)
    ax3.plot(ys)
    ax3.set_xlabel('Time')
    ax3.set_ylabel('Y')
    ax3.set_title('Y Plot')
    
    # Z plot
    ax4 = fig.add_subplot(224)
    ax4.plot(zs)
    ax4.set_xlabel('Time')
    ax4.set_ylabel('Z')
    ax4.set_title('Z Plot')
    
    plt.tight_layout(pad=3.0)
    plt.suptitle(title, fontsize=16)
    plt.subplots_adjust(top=0.9)
    plt.show()

# Plot for each scenario
plot_lorenz(28, "Chaotic")
plot_lorenz(10, "Semi-Chaotic")
plot_lorenz(0, "Non-Chaotic")
