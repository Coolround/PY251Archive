#Ryan Branagan
#Collaborators: N/A
#Branagan_hw7_p4.py
#2/27/19

import numpy as np
#%%
#Equations
#[R1+0+R3]*[I1]=[E1]
#[0+R2+R3]*[I2]=[E2]
#[1+1-1]*[I3]=[0]
#%%
#Parameters
R1 = 100
R2 = 120
R3 = 65
E1 = 12
E2 = 9

#Matricies
A = np.matrix([[R1,0,R3],[0,R2,R3],[1,1,-1]])
r = np.matrix([[E1],[E2],[0]])
v = np.linalg.solve(A,r)

#Answer
print('I1 is',v[0,0]*1000,'mA')
print('I2 is',v[1,0]*1000,'mA')
print('I3 is',v[2,0]*1000,'mA')