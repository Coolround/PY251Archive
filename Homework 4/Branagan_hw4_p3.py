#Ryan Branagan
#Collaborators: N/A
#Branagan_hw4_p3.py
#1/30/19

import numpy as np
import pylab as p

def lncosh(x):
    return np.log(x)/np.cosh(x)

f = lncosh
h = 10**-2
a = 2
b = 5
points = 1000

#Second Derivative
def d2(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

#Array of xs
xs = np.linspace(a,b,points)

#Array of answers
ans = np.array([])
for x in xs:
    ans = np.append(ans,d2(lncosh,x,h))

#Plotting
p.plot(xs,ans,'o')
p.xlabel('x')
p.ylabel('Second Derivative of Log(x)cosh(x)')
p.show()