#Ryan Branagan
#Collaborators: Jack Featherstone, Grant Sherrill, JP Habeeb, Emma Stone, Crosson Nipper, Sally Lord
#Branagan_ex1_p1.py
#2/9/19

import numpy as np
import pylab as p

#Parameters
n = 200
e = 3

#Define the potential as a funciton of N
def P(N):
    P = np.array([])
    for i in range(1,N+1):
        if i % 2 == 0:
            T = 1
        elif not i % 2 == 0:
            T = -1
        
        P = np.append(P,((2*T)/i))
    return np.sum(P)

#Input list
Nlist = np.linspace(1,n,n)

#Output list
ans = np.array([])
for A in Nlist:
    ans = np.append(ans,P(int(A)))

x = 2*Nlist+1

#Plotting
fig, ax = p.subplots(1,1)
ax.plot(x,ans,'o')
ax.set_xlabel('N')
ax.set_ylabel('Total Potential Energy on Central Ion [ke^2/r]')
ax.set_title('Total Potential Energy vs N')
p.show()