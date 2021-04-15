#Ryan Branagan
#Collaborators: N/A
#Branagan_hw3_p1.py
#1/22/19

import numpy as np
import pylab as p

#Input
n=10
f=np.sin
a=0
b=np.pi/2
truans=1

#Define the left hand, right hand, and mid point sum
def leftpoint(f,a,b,N):
    h = (b-a)/N
    
    xax = np.zeros(N)
    for i in range(N):
        y = a + i*h
        xax[i] = y 

    return np.sum(f(xax) * h)

def midpoint(f,a,b,N):
    h = (b-a)/N
    
    xax = np.zeros(N)
    for i in range(N):
        y = a+(i+1/2)*h
        xax[i] = y 

    return np.sum(f(xax) * h)

def rightpoint(f,a,b,N):
    h = (b-a)/N
    
    xax = np.array([])
    for i in range(N):
        y = a+(i+1)*h
        xax = np.append(xax,y) 

    return np.sum(f(xax) * h)

#Make a list of Ns
Nlist = []
s = 1
for i in range(n):
    s = s * 2
    Nlist.append(s)

#Make a list of the sums for each N in the Nlist
ansMP = np.array([])
for N in Nlist:
    y = midpoint(f,a,b,N)
    ansMP = np.append(ansMP,y)

ansLHS = np.array([])
for N in Nlist:
    y = leftpoint(f,a,b,N)
    ansLHS = np.append(ansLHS,y)

#Calculate errors
errMP = (ansMP-truans)/truans

errLHS = (ansLHS-truans)/truans

#Plot the answer for each N
#p.figure(1)
#p.plot(Nlist,ansMP,'o-',label="Midpoint")
#p.plot(Nlist,ansLHS,'o-',label="Left Hand Side")
#p.legend()

#Plotting log-log plot for error
p.figure(2)
p.plot(np.log10(Nlist),np.log10(np.abs(errMP)),'o-',label="Midpoint Error")
p.plot(np.log10(Nlist),np.log10(np.abs(errLHS)),'o-',label="Left Hand Side Error")
p.legend()
p.xlabel('Log of N subintervals')
p.ylabel('Log of the error')
p.show()