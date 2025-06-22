# Evaluate and plot the analytical projectile motion model in the y dimension (i.e. t vs ry(t))
import numpy as np
import matplotlib.pyplot as plt

# Initial and final time of the simulation
t0 = 0
tf = 2

# Initial dimension-wise conditions
ry0 = 0   # initial vertical position in meters
vy0 = 5   # initial vertical velocity in m/s
g = 9.81  # acceleration due to gravity in m/s^2

# Evaluate our model at 100 timesteps between t0 and tf
t = np.linspace(t0, tf, 100)
ry = ry0 + vy0 * t - 0.5 * g * t**2        # vertical position as a function of time

# Plotting with Matplotlib
plt.plot(t, ry)
plt.title("Projectile Motion in Y-Direction")
plt.xlabel("Time (s)")
plt.ylabel("Vertical Position ry(t) (m)")
plt.grid(True)
plt.show()
