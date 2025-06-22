# Simulate a projectile's 2D motion in time according to an analytical model
import numpy as np
import matplotlib.pyplot as plt

# The simulation initial time, final time and step size
t0 = 0
tf = 1.5
dt = 0.1

# Evaluate our model between t0 and tf in increments of dt
t = np.arange(t0, tf + dt, dt)

# Initial conditions
rx0 = 0      # initial x-position
ry0 = 0      # initial y-position
vx0 = 5      # initial x-velocity
vy0 = 6      # initial y-velocity
g = 9.81      # gravity


# rx0, ry0, vx0, vy0, ...
rx = rx0 + vx0 * t                    # implement your model!
ry = ry0 + vy0 * t - 0.5 * g * t**2   # transcribe your maths from paper to code

# Find peak
peak_idx = np.argmax(ry)
peak_x = rx[peak_idx]
peak_y = ry[peak_idx]

# Plot with enhancements
plt.figure(figsize=(10, 6))
plt.plot(rx, ry, 'b--o', label='Trajectory')  # Blue dashed line with circular markers
plt.fill_between(rx, ry, color='lightblue', alpha=0.3)  # Shade under trajectory
plt.scatter(peak_x, peak_y, color='red', zorder=5, label='Peak')
plt.annotate(f'Peak\n({peak_x:.2f}, {peak_y:.2f})',
             xy=(peak_x, peak_y),
             xytext=(peak_x + 0.2, peak_y + 1),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Axis labels and styling
plt.title("2D Projectile Motion Plot")
plt.xlabel("Horizontal Position (m)")
plt.ylabel("Vertical Position (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
