#Ryan Branagan
#Collaborators: N/A
#Branagan_hw7_p2.py
#2/27/19

import numpy as np
import pylab as p
from scipy.integrate import odeint
#%%
def deriv(s,t,ma,mb,kl,km,kr):
    xa = s[0]
    va = s[1]
    xb = s[2]
    vb = s[3]
    deriv = [va,(-1*(kl*xa+km*(xa-xb))/(ma)),vb,(-1*(kr*xb+km*(xb-xa))/(mb))]
    return deriv

def DiffEq(si,t0,tf,points,deriv,params):
    ma = params[0]
    mb = params[1]
    kl = params[2]
    km = params[3]
    kr = params[4]
    t = np.linspace(t0,tf,points)
    s = odeint(deriv,si,t,args=(ma,mb,kl,km,kr))
    return t,s
#%%
#1
#Initial conditions
si = [0.,0.1,0.,0.1]
t0 = 0
tf = 30
points = 3001
params = [1,1,1,1,1]

#Getting Points
t,solns = DiffEq(si,t0,tf,points,deriv,params)
xa = solns[:,0]
va = solns[:,1]
xb = solns[:,2]
vb = solns[:,3]

#Plotting
fig1,(pos,vel) = p.subplots(2,1,figsize=(6,8))
pos.plot(t,xa,label="Mass A")
pos.plot(t,xb,label="Mass B")
pos.set_title('Position of Both Masses Over Time')
pos.legend()
pos.set_ylabel('Position [m]')

vel.plot(t,va,label="Mass A")
vel.plot(t,vb,label="Mass B")
vel.set_title('Velocity of Both Masses Over Time')
vel.legend()
vel.set_xlabel('Time [s]')
vel.set_ylabel('Velocity [m/s]')
#%%
#2
#Initial conditions
si = [0.,0.1,0.,-0.1]
t0 = 0
tf = 30
points = 3001
params = [1,1,1,1,1]

#Getting Points
t,solns = DiffEq(si,t0,tf,points,deriv,params)
xa = solns[:,0]
va = solns[:,1]
xb = solns[:,2]
vb = solns[:,3]

#Plotting
fig3,(pos,vel) = p.subplots(2,1,figsize=(6,8))
pos.plot(t,xa,label="Mass A")
pos.plot(t,xb,label="Mass B")
pos.set_title('Position of Both Masses Over Time')
pos.legend()
pos.set_ylabel('Position [m]')

vel.plot(t,va,label="Mass A")
vel.plot(t,vb,label="Mass B")
vel.set_title('Velocity of Both Masses Over Time')
vel.legend()
vel.set_xlabel('Time [s]')
vel.set_ylabel('Velocity [m/s]')
#%%
#3
#Initial conditions
si = [0.,-5,0.,5]
t0 = 0
tf = 30
points = 3001
params = [1,1,1,1,1]

#Getting Points
t,solns = DiffEq(si,t0,tf,points,deriv,params)
xa = solns[:,0]
va = solns[:,1]
xb = solns[:,2]
vb = solns[:,3]

#Plotting
fig3,(pos,vel) = p.subplots(2,1,figsize=(6,8))
pos.plot(t,xa,label="Mass A")
pos.plot(t,xb,label="Mass B")
pos.set_title('Position of Both Masses Over Time')
pos.legend()
pos.set_ylabel('Position [m]')

vel.plot(t,va,label="Mass A")
vel.plot(t,vb,label="Mass B")
vel.set_title('Velocity of Both Masses Over Time')
vel.legend()
vel.set_xlabel('Time [s]')
vel.set_ylabel('Velocity [m/s]')
#%%
#4
#Initial conditions
si = [0.,-20.,0.,0.01]
t0 = 0
tf = 30
points = 3001
params = [1,1,1,1,1]

#Getting Points
t,solns = DiffEq(si,t0,tf,points,deriv,params)
xa = solns[:,0]
va = solns[:,1]
xb = solns[:,2]
vb = solns[:,3]

#Plotting
fig3,(pos,vel) = p.subplots(2,1,figsize=(6,8))
pos.plot(t,xa,label="Mass A")
pos.plot(t,xb,label="Mass B")
pos.set_title('Position of Both Masses Over Time')
pos.legend()
pos.set_ylabel('Position [m]')

vel.plot(t,va,label="Mass A")
vel.plot(t,vb,label="Mass B")
vel.set_title('Velocity of Both Masses Over Time')
vel.legend()
vel.set_xlabel('Time [s]')
vel.set_ylabel('Velocity [m/s]')