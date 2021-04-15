#Ryan Branagan
#Collaborators: N/A
#Branagan_hw8_p1.py
#2/28/19

import numpy as np
import pylab as p
#%%
#Import Data
Dat = np.loadtxt("C:\\Users\\ryan-\\Documents\\251\\Homework 8\\freefall.data")
t = Dat[:,0]
v = Dat[:,1]

#Fitting Parameters
Sumt = np.sum(t)
Sumt2 = np.sum(t**2)
Sumv = np.sum(v)
Sumtv = np.sum(t*v)
N = len(t)

#Using LinAlg
A = np.matrix([[Sumt2,Sumt],[Sumt,N]])
r = np.matrix([[Sumtv],[Sumv]])
Soln = np.linalg.solve(A,r)
Fit = Soln[0,0]*t+Soln[1,0]

#Plotting
fig,ax = p.subplots(1,1)
ax.plot(t,v,'ro',label="Data")
ax.plot(t,Fit,'k--',label="Line of Best Fit")
ax.set_title('Velocity Over Time')
ax.legend()
ax.set_xlabel('Time [s]')
ax.set_ylabel('Velocity [m/s]')

#Result
print("The experimental value of g for this experiment is approximately 10.089")