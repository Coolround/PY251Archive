#Ryan Branagan
#Collaborators: N/A
#Branagan_hw3_p3.py
#1/24/19

import numpy as np

#Define a function for our integral we want to integrate
def cosq(x):
    return np.cos(x**2-x)

#Input
n=15
f=cosq
a=-1
b=1
j=30000

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

print(leftpoint(f,a,b,j))
print(midpoint(f,a,b,j))
print(trap(f,a,b,j))

#Results
print('The number of subintervals needed to have an error of 10^-4 for Left Hand Rule is approximately 20000')
print('The number of subintervals needed to have an error of 10^-4 for Mid-Point Rule is approximately 124')
print('The number of subintervals needed to have an error of 10^-4 for Trapezoid Rule is approximately 114')