#Ryan Branagan
#Collaborators: N/A
#Branagan_hw4_p1.py
#1/29/19

import numpy as np

#Define the function we are trying to find the numerical derivative of
def costanh(x):
    return np.cos(x)*np.tanh(x)

#Parameters
f=costanh
x=2.
h=10**-4
ND3X = 1.231239865696003
#ND3X = 'No'

#Define the Central Difference
def CenDiffD(f,x,h,ND3X):
    if type(ND3X) == str:
        return (f(x+h)-f(x-h))/(2*h)
    if not type(ND3X) == str:
        x = (f(x+h)-f(x-h))/(2*h)
        y = (1/6)*ND3X*(h**2)
        return np.array([x,y])

print(CenDiffD(f,x,h,ND3X))
print(h**2)