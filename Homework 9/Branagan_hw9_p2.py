#Ryan Branagan
#Collaborators: N/A
#Branagan_hw9_p2.py
#3/20/19

import numpy as np
import pylab as p
#%%
#Parameters
t0 = 0
tf = 24.999
points = 1000

ts = np.linspace(t0,tf,points)

#Functions
def X(t):
    x0 = 0
    v0 = 0
    m0 = 5000
    rho = 200
    u = 2000
    return x0+(u+v0)*t+u*((m0/rho)-t)*np.log(1-((rho*t)/m0))

def V(t):
    v0 = 0
    m0 = 5000
    rho = 200
    u = 2000
    return v0-u*np.log((m0-rho*t)/m0)

#Root finding
T = G = 2
i = 0
while True:
    if np.abs(X(T)-4000) < 0.001:
        break
    T = T - ((X(T)-4000)/V(T))
    i = i + 1

#Results
print("The time it takes for the rocket to reach 4km is: "+str(T)+"[s]")
print("Iterations: "+str(i)+"   Initial Guess: "+str(G))

#Plotting
fig, ax = p.subplots(1,1)
ax.plot(ts,X(ts))
ax.plot(T,X(T),"rx",label="4km Point at t="+str(round(T,3)))
ax.axhline(4000,color="k",linestyle="--",label="4km Line")
ax.legend()
ax.set_title("Position Over Time for a Rocket")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Position [m]")