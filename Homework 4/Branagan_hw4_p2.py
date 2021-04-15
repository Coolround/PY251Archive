#Ryan Branagan
#Collaborators: N/A
#Branagan_hw4_p2.py
#1/31/19

import numpy as np

def costanh(x):
    return np.cos(x)*np.tanh(x)

f = costanh
x = 2
h = 10**-2
ND5X = 0.502625754665

#Define the Central Difference
def Cen5S(f,x,h,ND5X):
    if type(ND5X) == str:
        return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)
    if not type(ND5X) == str:
        x = (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)
        y = -(1/30)*ND5X*(h**4)
        return np.array([x,y])

print(Cen5S(f,x,h,ND5X))
print(h**4)