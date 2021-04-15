#Ryan Branagan
#Collaborators: N/A
#Branagan_hw6_p1.py
#2/19/19

import numpy as np
import pylab as p
#%%
#Initial Conditions
y0 = 0.
v0 = 35.
t0 = 0
tf = 10
points = 10000

#Define Functions
def AnV(v0,B,t0,tf,points):
    g = 9.81
    #Times
    t = np.linspace(t0,tf,points)
    #Velocities
    v = (v0+(g/B))*np.exp(-B*t)-(g/B)
    return t,v

def AnY(y0,v0,B,t0,tf,points):
    g = 9.81
    #Times
    t = np.linspace(t0,tf,points)
    #Y Positions
    y = (-(v0/B)-(g/B**2))*np.exp(-B*t)-(g*t/B)+(v0/B)+(g/B**2)+y0
    return t,y

def Accel(v,B):
    g = 9.81
    return (-g-B*v)

#Get Points
Bs = [10.**-6,0.1,0.2,0.5]
ys = [np.zeros(points),np.zeros(points),np.zeros(points),np.zeros(points)]
vs = [np.zeros(points),np.zeros(points),np.zeros(points),np.zeros(points)]
As = [np.zeros(points),np.zeros(points),np.zeros(points),np.zeros(points)]
for i,b in enumerate(Bs):
    ts,ys[i] = AnY(y0,v0,b,t0,tf,points)
    vs[i] = AnV(v0,b,t0,tf,points)[1]
    As[i] = Accel(vs[i],b)

#Plotting
fig1,(pos,vel,acc) = p.subplots(3,1, figsize=(6,10))
for i,b in enumerate(Bs):
    pos.plot(ts,ys[i],label=r"$\beta=$"+str(b))
pos.axhline(0,color='k',linestyle='--')
pos.legend()
pos.set_title('Position Over Time for Various Beta Values')
pos.set_ylabel('Height [m]')

for i,b in enumerate(Bs):
    vel.plot(ts,vs[i],label=r"$\beta=$"+str(b))
vel.axhline(0,color='k',linestyle='--')
vel.legend()
vel.set_title('Velocity Over Time for Various Beta Values')
vel.set_ylabel('Velocity [m/s]')

for i,b in enumerate(Bs):
    acc.plot(ts,As[i],label=r"$\beta=$"+str(b))
acc.axhline(0,color='k',linestyle='--')
acc.legend()
acc.set_title('Acceleration Over Time for Various Beta Values')
acc.set_ylabel('Acceleration [m/s^2]')
acc.set_xlabel('Time [s]')