#Ryan Branagan
#Collaborators: N/A
#Branagan_hw10_p2.py
#4/8/19

import numpy as np
import pylab as p
#%%
#Define important things
def Fres(x):
    return np.cos((np.pi*(x**2))/2)

def HitorMiss(f,a,b,c,d,axis):
    x = np.random.uniform(a,b)
    y = np.random.uniform(c,d)
    T = f(x)
    if y > 0:
        if y > T:
            g = 0
            axis.plot(x,y,color='gray',marker='o')
        if y <= T:
            g = 1
            axis.plot(x,y,'ro')
    if y < 0:
        if y < T:
            g = 0
            axis.plot(x,y,color='gray',marker='o')
        if y >= T:
            g = -1
            axis.plot(x,y,'bo')
    if y == 0:
        g = 0
        axis.plot(x,y,'ko')
    return g
#%%
#Parameters
f = Fres
a = 0
b = 2
c = -1
d = 1
N = 10**4

#Setup
fig,ax = p.subplots(1,1)
ax.set_title("Using the Hit or Miss Monte Carlo to calculate the Fresnel Integral")
ax.set_xlabel("x")
ax.set_ylabel("Fresnel Integrand of x")
x = np.linspace(a,b,N)
ax.plot(x,Fres(x),'k--')
ax.axhline(0, color='k', linestyle='--')
Np = 0
Neg = 0

#Results
for i in range(N):
    z = HitorMiss(f,a,b,c,d,ax)
    if z > 0:
        Np = Np + z
    if z < 0:
        Neg = Neg - z

Result = (4*(Np-Neg))/N
print(Result)