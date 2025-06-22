# Simulate a 2D projectile using the Euler method
import numpy as np
import matplotlib.pyplot as plt

# The simulation initial time, final time and step size
t_current = 0
tf = 2
dt = 0.01   # Remember you can change this

# Initial position
rx_current = 0
ry_current = 0.1

# Initial velocity
vx_current = 5 * np.sqrt(3)
vy_current = 5

# Gravitational acceleration
g = 9.81

# Running the simulation by stepping forward in time in increments of dt.
# We use an Euler Method solver to approximate the functions in small steps.

# Lists to store trajectory
rx_vals = []
ry_vals = []

# Euler integration loop
while t_current < tf:

    # Stop simulation if projectile hits the ground
    if ry_current < 0:
        break

    # Save current position
    rx_vals.append(rx_current)
    ry_vals.append(ry_current)

    # Euler update: position
    rx_new = rx_current + vx_current * dt
    ry_new = ry_current + vy_current * dt

    # Euler update: velocity
    vx_new = vx_current  # No horizontal acceleration
    vy_new = vy_current - g * dt

    # Time update
    t_current += dt

    # Prepare for next step
    rx_current = rx_new
    ry_current = ry_new
    vx_current = vx_new
    vy_current = vy_new

# Plot trajectory
plt.plot(rx_vals, ry_vals, 'k-')
plt.title("2D Projectile Motion (Euler Method)")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.grid(True)
plt.show()
