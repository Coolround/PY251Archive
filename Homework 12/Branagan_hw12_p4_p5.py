#Ryan Branagan
#Collaborators: Jack Featherstone
#Branagan_hw12_p4_p5.py
#4/17/19

import numpy as np
import pylab as p
#%%
#Defining Important Values
xa = -5.
xb = 5.
c = 50.
J = 100
N = 200
dx = (xb-xa)/N
dt = 0.25*dx/c
xs = np.linspace(xa,xb,J+1)
t0 = 0
tf = N*dt
ts = np.linspace(t0,tf,N+1)
y = np.zeros([J+1,N+1])
v = np.zeros([J+1,N+1])
A = 0.1
sigma = 1.

#Setting Initial Conditions
y[:,0] = A * np.exp(-xs**2/sigma**2)
y[:,1] = A * np.exp(-xs**2/sigma**2)
#%%
#These are for the Initial Conditions for 19.2/12.5
v[:,0] = ((2*A*c*xs)/(sigma**2))*np.exp(-(xs**2)/(sigma**2))
v[:,1] = ((2*A*c*xs)/(sigma**2))*np.exp(-(xs**2)/(sigma**2))
#%%
#Applying Method
for n in range(1,N):
    #Boundaries
    y[0,n+1] = 0
    y[-1,n+1] = 0
    
    #Half Step
    yh = np.zeros(J+1)
    vh = np.zeros(J+1)
    
    for j in range(1,J):
        yh[j] = y[j,n] + (dt/2)*v[j,n]
        vh[j] = v[j,n] + ((dt*(c**2))/2)*((y[j+1,n]-2*y[j,n]+y[j-1,n])/(dx**2))
    
    #Find Values
    for j in range(1,J):
        y[j,n+1] = y[j,n] + dt*vh[j]
        v[j,n+1] = v[j,n] + (dt*(c**2))*((yh[j+1]-2*yh[j]+yh[j-1])/(dx**2))

#Plotting
fig,ax = p.subplots(1,1)
for n in range(N):
    ax.plot(y[:,n]+(float(n)/500))