#Ryan Branagan
#Collaborators: I got help from Jack Featherstone
#Branagan_hw2_p3.py
#1/15/19

#import what I need
import numpy as np
import pylab as p

#Initial conditions
v0 = 300. #Initial speed (m/s)
theta = 89.99 #Angle with respect to the x axis
tf = 61 #How long in seconds it should plot (s)

#Finding the x and y components of the initial velocity (m/s)
vx = v0 * np.cos(theta * (np.pi/180))
vy = v0 * np.sin(theta * (np.pi/180))

#Equations for our x and y positions as a funciton of time (m)
#This is what Jack helped me with
g = 9.81
def xp(t): 
    return vx * t
def yp(t):
    return vy * t - 0.5 * g * t**2

#Making an array of times to plug into our equation (s)
times = np.linspace(0,tf,2*tf+1) #I want to check every half second so 2*tf+1 is necessary

#Make an array of x positions over time (m)
x = np.zeros(2*tf+1)
for a in np.arange(len(x)):
    x[a] = xp(times[a])
#print(x)

#Make an array of y positions over time (m)
y = np.zeros(2*tf+1)
for a in np.arange(len(y)):
    y[a] = yp(times[a])
#print(y)

#Make a plot of the position of the projectile over time
p.plot(x,y,'o')
p.xlabel('X Position (meters)')
p.ylabel('Y Position (meters)')
p.title('Projectile Trajectory')
p.show()