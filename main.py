import matplotlib.pyplot as plt 
import numpy as np

v0 = input("Enter the initial velocity (m/s):")
theta = input("Enter the launch angle (degrees):")

g = 9.81

v0 = float(v0)
theta = float(theta)

theta = np.radians(theta)

t = np.linspace(0, 2*v0*np.sin(theta)/g, 1000)
x = v0*np.cos(theta)*t
y = v0*np.sin(theta)*t - 0.5*g*g**2

plt.plot(x,y)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()