#Ryan Branagan
#Collaborators: Jack Featherstone, John Paul Habeeb, Mason Lovejoy-Johnson, and Grant Sherril
#Branagan_ex3_p2.py
#4/17/19

import numpy as np
import pylab as p
#%%
#Make an R
Coords = np.array([[7,4],[8,4],[9,4],[10,4],[11,4],[12,4],[13,4],[7,5],[8,5],[12,5],[13,5],[14,5],[7,6],[8,6],[13,6],[14,6],[7,7],[8,7],[13,7],[14,7],[7,8],[8,8],[13,8],[14,8],[7,9],[8,9],[12,9],[13,9],[14,9],[7,10],[8,10],[9,10],[10,10],[11,10],[12,10],[13,10],[7,11],[8,11],[9,11],[10,11],[11,11],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[7,13],[8,13],[11,13],[12,13],[13,13],[7,14],[8,14],[12,14],[13,14],[14,14],[7,15],[8,15],[13,15],[14,15],[7,16],[8,16],[13,16],[14,16],[7,17],[8,17],[13,17],[14,17]])
Coords = Coords + 9

Alf = 1.
dx = 1.
dy = 1.
dt = 0.25
X = 40
Y = 40
t0 = 0
tf = 300
T = int(tf/dt)+2
Tol = 10**-6
Temp = np.zeros([T+1,X,Y])

def Bound(Arr,t):
    for C in Coords:
        x = C[0]
        y = C[1]
        Arr[t,y,x] = 1.
    Arr[t,0] = 0
    Arr[t,-1] = 0
    Arr[t,:,0] = 0
    Arr[t,:,-1] = 0
    return Arr

Temp = Bound(Temp,0)
Temp = Bound(Temp,1)
for t in range(1,T):
    for x in range(1,X-1):
        for y in range(1,Y-1):
            Temp[t+1,y,x] = ((2.*Alf*dt)*((((Temp[t,y,x+1])-(2.*Temp[t,y,x])+(Temp[t,y,x-1]))/(dx**2))+(((Temp[t,y+1,x])-(2.*Temp[t,y,x])+(Temp[t,y-1,x]))/(dy**2))))+(Temp[t-1,y,x])
    Temp = Bound(Temp,t+1)


p.pcolor(Temp[t,::-1,:])