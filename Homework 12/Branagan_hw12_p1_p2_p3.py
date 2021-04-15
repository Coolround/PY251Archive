#Ryan Branagan
#Collaborators: N/A
#Branagan_hw12_p1_p2_p3.py
#4/11/19

import numpy as np
import pylab as p
#%%
#Parameters
k = 5.
xa = 0
xb = 1
ya = 0
yb = 2
N = 100

#Define things
xs = np.linspace(xa,xb,N)
ys = 2.*xs
h = xs[1]-xs[0]

#%%
#Problem 1
for i in range(10**6):
    ys[1:-1] = 0.5*(ys[:-2]+ys[2:])-(((k*(h**2))/2)*np.sqrt(1+(((ys[:-2]-ys[2:])**2)/((2*h)**2))))
#%%

#Setup of Plotting
fig,ax = p.subplots(1,1)

#Sweeping
ys = 2.*xs
Sweeps = 0
while True:
    i = np.copy(ys)
    ys[1:-1] = 0.5*(ys[:-2]+ys[2:])-(((k*(h**2))/2)*np.sqrt(1+(((ys[:-2]-ys[2:])**2)/((2*h)**2))))
    Sweeps = Sweeps + 1
    if Sweeps == 10**2 or Sweeps == (2.805*(10**3)) or Sweeps == 10**4:
        ax.plot(xs,ys,label=str(Sweeps)+" Sweeps")
    if np.mean(np.abs(ys-i)) < 10**-8:
        break

#Plotting
ax.plot(xs,ys,'r-',label="Final")
ax.set_title('String Model')
ax.set_xlabel('Horizontal Distance')
ax.set_ylabel('Vertical Distance')
ax.legend()
#%%
#Problem 3
def Length(x,y):
    return np.sqrt(1+(((y[1:]-y[:-1])/(x[1:]-x[:-1]))**2))

ks = np.linspace(1,8,8)
ans = np.zeros_like(ks)
for i,k in enumerate(ks):
    for j in range(Sweeps):
        ys[1:-1] = 0.5*(ys[:-2]+ys[2:])-(((k*(h**2))/2)*np.sqrt(1+(((ys[:-2]-ys[2:])**2)/((2*h)**2))))
    L = Length(xs,ys)
    L[0] = L[0]*(3/2)
    L[-1] = L[-1]*(3/2)
    ans[i] = h*np.sum(L)

fig2,ax2 = p.subplots(1,1)
ax2.plot(ks,ans,'-o')
ax2.set_title('Length vs Constant k')
ax2.set_xlabel('k')
ax2.set_ylabel('Length')