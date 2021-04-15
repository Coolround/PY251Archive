#Ryan Branagan
#Collaborators: N/A
#Branagan_hw8_p2.py
#2/28/19

import numpy as np
import pylab as p
from scipy.optimize import curve_fit as cf
#%%
#Import Data
Dat = np.loadtxt("C:\\Users\\ryan-\\Documents\\251\\Homework 8\\damped_oscillation.txt")
t = Dat[:,0]
theta = Dat[:,1]

#Define our function
def Damped(t,a,w,phi,tau,b):
    return a*np.cos(w*t+phi)*np.exp(-t/tau)+b

#Fitting
par,con = cf(Damped,t,theta)

#Fitted Curve
def Fitted(t):
    a = par[0]
    w = par[1]
    phi = par[2]
    tau = par[3]
    b = par[4]
    return a*np.cos(w*t+phi)*np.exp(-t/tau)+b

#Getting Points
Fit = Fitted(t)

#Residual
R = (Fit - theta)**2
R = np.sum(R)

#Plotting
fig,ax = p.subplots(1,1)
ax.plot(t,theta,'ro-',label="Data")
ax.plot(t,Fit,'k--',label="Fitted Function")
ax.legend()
ax.set_title('Position Over Time for a Pendulum')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Angular Position [radians]')
ax.annotate('a='+str(par[0]),xy=(410, 350),xycoords='figure pixels')
ax.annotate('omega='+str(par[1]),xy=(410, 325),xycoords='figure pixels')
ax.annotate('phi='+str(par[2]),xy=(410, 300),xycoords='figure pixels')
ax.annotate('tau='+str(par[3]),xy=(410, 275),xycoords='figure pixels')
ax.annotate('b='+str(par[4]),xy=(410, 250),xycoords='figure pixels')
ax.annotate('residual='+str(R),xy=(425, 225),xycoords='figure pixels')