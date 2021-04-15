#Ryan Branagan
#Collaborators: N/A
#Branagan_hw11_p1.py
#4/10/19

import numpy as np
import pylab as p
#%%
#Define things
def FT(a,tax,fax):
    Aof = np.zeros_like(fax,dtype=complex)
    for i,f in enumerate(fax):
        #Setup Integrand/Product
        P = a*np.exp(-2*np.pi*1.j*f*tax)
        #Trap Rule
        dt = tax[1]-tax[0]
        Trap = (dt/2)*(P[0]+P[-1])+np.sum(P*dt)
        #Put it in an array
        Aof[i] = Trap
    return Aof

def func(t,f0,sigma):
    return np.cos(2*np.pi*f0*t)*np.exp(-1*(t**2)/(2*(sigma**2)))
#%%
#Parameters
t0 = 0
tf = 1
N = 10**3
f0 = 10
sigma = np.array([1,0.5,0.25])
fax0 = -20
ff = 20

ts = np.linspace(t0,tf,N)
fax = np.linspace(fax0,ff,N)

Ans = np.array([np.zeros(N) for i in range(len(sigma))],dtype=complex)
for i,s in enumerate(sigma):
    aot = func(ts,f0,s)
    z = FT(aot,ts,fax)
    Ans[i] = z

fig,ax = p.subplots(1,1)
ax.plot(fax,Ans[0],'r-',label="Sigma="+str(sigma[0]))
ax.plot(fax,Ans[1],'b-',label="Sigma="+str(sigma[1]))
ax.plot(fax,Ans[2],'g-',label="Sigma="+str(sigma[2]))
ax.set_title("Fourier Transform for different values of sigma")
ax.set_xlabel("Frequency [1/s]")
ax.set_ylabel("Fourier Transform")
ax.legend()