#Ryan Branagan
#Collaborators: N/A
#Branagan_hw3_p2.py
#1/23/19

import numpy as np
import pylab as p

#Define a function for our integral we want to integrate
def sinx2(x):
    return np.sin(x**2)

#Input
n=6
f=sinx2
a=0
b=100

#Define numerical integration techniques
def leftpoint(f,a,b,N):
    h = (b-a)/N
    
    xax = np.array([])
    for i in range(N):
        y = a + i*h
        xax = np.append(xax,y) 

    return np.sum(f(xax) * h)

def midpoint(f,a,b,N):
    h = (b-a)/N
    
    xax = np.array([])
    for i in range(N):
        y = a+(i+1/2)*h
        xax = np.append(xax,y) 

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
s = 2048
for i in range(n):
    s = s * 2
    Nlist.append(s)

#Make a list of the sums for each N in the Nlist
ansMP = np.array([])
for N in Nlist:
    y = midpoint(f,a,b,N)
    ansMP = np.append(ansMP,y)

#Find Error
print('Sorry this will take a little bit (less than a minute)')
truans = midpoint(f,a,b,200000)
errMP = (ansMP-truans)/truans

#Print Nlist and answers
print(Nlist)
print(ansMP)

#Plot error vs N to find what Ns are needed to have a certain error
p.plot(np.log10(Nlist),np.log10(np.abs(errMP)),'o-',label="Midpoint Error")
#p.plot(Nlist,ansMP,'o-')
p.show()