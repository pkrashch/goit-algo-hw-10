import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Define the function
def f(x):
    return x ** 2

# Limits of integration
a = 0  # lower limit
b = 2  # upper limit
y_max = f(b)  # height of the rectangle (max value of f(x) on [a, b])

# Monte Carlo Method
def monte_carlo_integrate(f, a, b, y_max, num_points=10000):
    # Generate random x and y coordinates
    x_rand = np.random.uniform(a, b, num_points)
    y_rand = np.random.uniform(0, y_max, num_points)
    
    # Check which points are under the curve
    under_curve = y_rand < f(x_rand)
    
    # Calculate the ratio and multiply by the rectangle area
    rect_area = (b - a) * y_max
    integral_mc = (np.sum(under_curve) / num_points) * rect_area
    
    return integral_mc, x_rand, y_rand, under_curve

# Number of points for simulation
num_points = 15000
mc_result, x_pts, y_pts, under = monte_carlo_integrate(f, a, b, y_max, num_points)

# Analytical calculation with quad for comparison
quad_result, error = spi.quad(f, a, b)

# Printing results
print(f"Monte Carlo Result ({num_points} points): {mc_result}")
print(f"Quad Function Result: {quad_result}")
print(f"Absolute Difference: {abs(mc_result - quad_result)}")

# Visualization
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, 'r', linewidth=2, label='$f(x) = x^2$')
ax.fill_between(np.linspace(a, b), f(np.linspace(a, b)), color='gray', alpha=0.2, label='True Area')

# Plotting Monte Carlo points
ax.scatter(x_pts[under], y_pts[under], color='green', s=1, alpha=0.5, label='Points under curve')
ax.scatter(x_pts[~under], y_pts[~under], color='blue', s=1, alpha=0.3, label='Points above curve')

ax.set_xlim([a - 0.2, b + 0.2])
ax.set_ylim([0, y_max + 0.5])
ax.legend(loc='upper left')
plt.title(f'Monte Carlo Integration (Area ≈ {mc_result:.4f})')
plt.grid(True)
plt.show()