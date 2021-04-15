#Ryan Branagan
#Collaborators: N/A
#Branagan_hw10_p3.py
#4/8/19

import numpy as np
import pylab as p
#%%
#Define things
def MC2D(f,a,b,c,d,N):
    #Regular Monte Carlo Stuff
    dx = (b-a)/N
    dy = (d-c)
    Points = np.array([[np.random.uniform(a,b),np.random.uniform(c,d)] for i in range(N)])
    #Nonrectangular Region
    for P in Points:
        x = P[0]
        y = P[1]
        while np.sqrt(((x-(1/2))**2)+((y-(1/2))**2)) <= (1/3):
            x = np.random.uniform(a,b)
            y = np.random.uniform(c,d)
        P[0] = x
        P[1] = y
    #Unpack x and y
    xlist = Points[:,0]
    ylist = Points[:,1]
    #Monte Carlo Integration
    MC = np.sum(f(xlist,ylist)*dx*dy)
    return xlist,ylist,MC

def func(x,y):
    return np.log10(1+x*y)
#%%
#Parameters
f = func
a = 0
b = 1
c = 0
d = 1
N = 10**4

xs,ys,Ans = MC2D(f,a,b,c,d,N)

fig,ax = p.subplots(1,1,figsize=(8,8))
ax.plot(xs,ys,'ro')
ax.set_title("The region R we are integrating over")
ax.set_xlabel("x")
ax.set_ylabel("y")

print("The answer accurate to "+str(int(np.log10(N)/2)-1)+" digits: "+str(round(Ans,int(np.log10(N)/2)+1)))