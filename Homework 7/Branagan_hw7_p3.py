#Ryan Branagan
#Collaborators: N/A
#Branagan_hw7_p3.py
#2/27/19

import numpy as np
#%%
#Equations
#[1-cos(theta)+0]*[Fx]=[0]
#[0+sin(theta)+1]*[T]=[mg]
#[0+sin(theta)-1]*[Fy]=[0]
#%%
#Parameters
m = 14
L = 1.2
g = 9.81
theta = np.deg2rad(35)

#Matricies
A = np.matrix([[1,-np.cos(theta),0],[0,np.sin(theta),1],[0,np.sin(theta),-1]])
r = np.matrix([[0],[m*g],[0]])
v = np.linalg.solve(A,r)

#Answer
print('Fx is',v[0,0],'N')
print('T is',v[1,0],'N')
print('Fy is',v[2,0],'N')