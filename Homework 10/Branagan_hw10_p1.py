#Ryan Branagan
#Collaborators: N/A
#Branagan_hw10_p1.py
#4/2/19

import numpy as np
import pylab as p
#%%
#Define Monte Carlo and Function
def MC(f,a,b,N):
    h = ((b-a)/N)
    x = np.array([np.random.uniform(a,b) for i in range(N)])
    return np.sum(f(x)*h)

def Fres(x):
    return np.cos((np.pi*(x**2))/2)

def Gaussian(x,Sigma,Mu):
    return (1/(np.sqrt(2*np.pi)*Sigma))*np.exp(-1*(((x-Mu)**2)/(2*(Sigma**2))))
#%%
#Parameters
f = Fres
a = 0
b = 2
Ns = np.array([10**2,10**3,10**4])
Trials = 1000

#Get results
Results = np.array([np.zeros(Trials),np.zeros(Trials),np.zeros(Trials)])
for i,N in enumerate(Ns):
    for j in range(Trials):
        Results[i,j] = MC(f,a,b,N)

#Gaussian stuff
STD1 = np.std(Results[0])
STD2 = np.std(Results[1])
STD3 = np.std(Results[2])
Mu1 = np.mean(Results[0])
Mu2 = np.mean(Results[1])
Mu3 = np.mean(Results[2])

#Plotting
fig,(ax1,ax2,ax3) = p.subplots(1,3)
ax1.hist(Results[0],bins=50,color="red",normed=True)
ax2.hist(Results[1],bins=50,color="blue",normed=True)
ax3.hist(Results[2],bins=50,color="green",normed=True)
x = np.linspace(a,b,Ns[2])
ax1.plot(x,Gaussian(x,STD1,Mu1),'k--')
ax2.plot(x,Gaussian(x,STD2,Mu2),'k--')
ax3.plot(x,Gaussian(x,STD3,Mu3),'k--')
ax1.set_xlim(0,1)
ax2.set_xlim(0,1)
ax3.set_xlim(0,1)