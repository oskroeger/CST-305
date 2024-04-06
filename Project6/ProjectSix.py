import numpy as np
import matplotlib.pyplot as plt

def taylor_series_part1(x):
    """Taylor series up to n<=4 for the first part of the assignment."""
    return 1 - x - (1/3)*x**3 - (1/12)*x**4

def taylor_series_part2(x):
    """Second-order Taylor polynomial near x=3 for the second part of the assignment."""
    # Given the derivatives and their values at x=3: y(3)=6, y'(3)=1, y''(3)=-11
    # Taylor polynomial: f(x) = 6 + (x - 3) - 11/2*(x - 3)^2
    return 6 + (x - 3) - 11/2 * (x - 3)**2

# Evaluate and print the results for specific points
x_part1 = 3.5
y_part1 = taylor_series_part1(x_part1)
print(f"Part 1: Value of the Taylor series at x = {x_part1} is approximately {y_part1:.3f}")

# Visualization
plt.figure(figsize=(14, 7))

# Part 1
plt.subplot(1, 2, 1)
x_vals_part1 = np.linspace(-2, 5, 400)
y_vals_part1 = taylor_series_part1(x_vals_part1)
plt.plot(x_vals_part1, y_vals_part1, label='Taylor Series - n<=4')
plt.scatter([x_part1], [y_part1], color='red', zorder=5)
plt.text(x_part1, y_part1, f'({x_part1}, {y_part1:.3f})', color='black', verticalalignment='bottom')
plt.title('Part 1: Taylor Series Expansion at x=3.5')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
# Display the Taylor polynomial equation for Part 1
plt.text(-2, -30, "f(x) = 1 - x - 1/3x^3 - 1/12x^4", fontsize=12, color='blue')

# Part 2
plt.subplot(1, 2, 2)
x_vals_part2 = np.linspace(2, 4, 400)
y_vals_part2 = taylor_series_part2(x_vals_part2)
plt.plot(x_vals_part2, y_vals_part2, label='2nd Order Taylor Polynomial near x=3')
plt.title('Part 2: 2nd Order Taylor Polynomial')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid(True)
# Display the Taylor polynomial equation for Part 2
plt.text(2, 4, "f(x) = 6 + 1(x - 3) - 11/2(x - 3)^2", fontsize=12, color='blue')

plt.tight_layout()
plt.show()
