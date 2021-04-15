#Ryan Branagan
#Collaborators: N/A
#Branagan_hw3_p4.py
#1/24/19

import numpy as np
import pylab as p

#Define a function for our integral we want to integrate
def erf(x):
    return (2/np.sqrt(np.pi))*np.exp(-(x**2))

#Input
n=15
f=np.sin
a=0
b=np.pi/2
j=1000

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

def trap(f,a,b,N):
    return 0.5*(leftpoint(f,a,b,N)+rightpoint(f,a,b,N))

def simp(f,a,b,N):
    return (trap(f,a,b,N)/3)+((2*midpoint(f,a,b,N))/3)

def simp2(f,a,b,N):
    h = (b-a)/N
    
    term1 = np.array([])
    for Z in range(N):
        term1 = np.append(term1,(f(a+Z*h)))
    
    term2 = np.array([])
    for Y in range(N+1):
        term2 = np.append(term2,(f(a+Y*h-h/2)))
    
    return (h/6)*(f(a)+f(b)+2*np.sum(term1)+4*np.sum(term2))

def simp3(f,a,b,N):
    h = (b-a)/N
    
    #Left
    xl = np.array([])
    for A in range(N):
        xl = np.append(xl,(a+A*h))
    Left = np.sum(f(xl)*h)
    
    #Right
    xr = np.array([])
    for B in range(N):
        xr = np.append(xr,(a+(B+1)*h))
    Right = np.sum(f(xr)*h)
    
    #Trap
    Trap = (Left+Right)/2
    
    #Mid
    xm = np.array([])
    for C in range(N):
        xm = np.append(xm,(a+(C+1/2)*h))
    Mid = np.sum(f(xm)*h)
    
    return (Trap/3)+(2*Mid/3)

#An array of "x"s
x = np.linspace(a,b,j)

#Make an array of answers
ans = np.array([])
for b in x:
    y = simp(f,a,b,j)
    ans = np.append(ans,y)

#Plotting
p.plot(x,ans,'o-')
p.show()