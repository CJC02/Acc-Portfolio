import numpy as np
import matplotlib.pyplot as plt

#Quesion 3
# inputs/constants

#acceleration due to gravity
g = 9.81   

#density of fluid (air) (kg m^-3)                   
rho = 1.225     
#radius of steel ball (m)                      
radius = 2.5e-3  
#formula for cross sectional area (m^2)                        
area = np.pi * radius ** 2  
#formula for volume of sphere (m^3)        
volume = np.pi * 4 / 3 * radius ** 3   
#mass from density (kg) 
mass = rho * volume   
#restitution coefficient of steel, non-dimensional
cor = 0.75                              

# Initial conditions

#initial horizontal position (m)
rx0 = 0
#initial vertical position (m)
ry0 = 5
#initial velocity (m s^-1)
v = 0
#initial angle of projection (radians)
theta = np.radians(0)

#components of initial velocity (m s^-1)
vx0 = v * np.cos(theta)
vy0 = v * np.sin(theta)

#initial and final time (s)
t0 = 0
tf = 15
#time step (s)
dt = 0.0001

# This saves the simulated times, velocities and positions in growable lists
t_current = t0

vx_current = vx0
vy_current = vy0

rx_current = rx0
ry_current = ry0

t = [t_current]

vx = [vx_current]
vy = [vy_current]

rx = [rx_current]
ry = [ry_current]


#sets parameters of function between the initial and final times
while t_current < tf:
    # Calculates accelerations from the forces acting on the projectile using Newton's 2nd Law
    ax_current = 0 
    ay_current = -g 

    # Euler's Method 
    # Calculating the new velocity based on the current velocity and the known acceleration
    vx_next = vx_current + dt * ax_current
    vy_next = vy_current + dt * ay_current

    # Calculating the new position based on the initial position and the initial velocity components. 
    rx_next = rx_current + dt * vx_current
    ry_next = ry_current + dt * vy_current

    # Implementing the code to the next timestep
    t_next = t_current + dt

    #parameter that switches the restituion value to negative when height goes below 0m, this is the bounce.
    if ry_next < 0:
         vy_next = -cor * vy_next

    # This is the loop, where the next velocities and positions become the current ones
    t_current = t_next

    vx_current = vx_next
    vy_current = vy_next

    rx_current = rx_next
    ry_current = ry_next

    # Save velocities and positions from our lists
    t.append(t_current)

    vx.append(vx_current)
    vy.append(vy_current)

    rx.append(rx_current)
    ry.append(ry_current)

t = np.array(t)

vx = np.array(vx)
vy = np.array(vy)

rx = np.array(rx)
ry = np.array(ry)


plt.plot(t, ry)
      
plt.title('Steel ball')
plt.xlabel('Time (s)')
plt.ylabel('Vertical distance (m)')
plt.grid(True)
plt.show
