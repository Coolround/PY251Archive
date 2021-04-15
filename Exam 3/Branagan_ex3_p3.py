#Ryan Branagan
#Collaborators: Jack Featherstone, John Paul Habeeb, Mason Lovejoy-Johnson, and Grant Sherril
#Branagan_ex3_p3.py
#4/17/19

import numpy as np
import pylab as p
#%%
#Dogs = 1
#Cats = 0
#Yes = 1
#No = 0
#Make neighborhood
Neigh = np.zeros([20,20],dtype=int)
for i in range(20):
    for j in range(20):
        Neigh[i,j] = np.random.randint(0,2)

#Define Process of testing and changing animal
def Change(Arr,k):
    #Pick a house
    x = np.random.randint(0,20)
    y = np.random.randint(0,20)
    house = Arr[y,x]
    
    #Periodic Boundary and neighbors
    if x < 1:
        left = -1
    else:
        left = x - 1
    if x > 18:
        right = 0
    else:
        right = x + 1
    if y < 1:
        up = -1
    else:
        up = y - 1
    if y > 18:
        down = 0
    else:
        down = y + 1
    uph = Arr[up,x]
    righth = Arr[y,right]
    downh = Arr[down,x]
    lefth = Arr[y,left]
    
    #Logic Processes
    #Logic 1
    if int(uph+righth+downh+lefth) == 3 or 4 and house == 0:
        ans = 1
    if int(uph+righth+downh+lefth) == 0 or 1 and house == 1:
        ans = 1
    #Logic 2
    a = np.random.uniform(0,2)
    S = 0
    D = 0
    hlist = np.array([uph,righth,downh,lefth],dtype=int)
    for h in hlist:
        if not h == house:
            S = S + 1
        if h == house:
            D = D + 1
    factor = np.exp(-k*(D-S))
    if a < factor:
        L2 = 1
    else:
        L2 = 0
    if int(uph+righth+downh+lefth) == 3 or 4 and house == 1:
        ans = L2
    if int(uph+righth+downh+lefth) == 0 or 1 and house == 0:
        ans = L2
    if int(uph+righth+downh+lefth) == 2:
        ans = L2
    
    #Change the animal
    if ans == 1:
        if house == 1:
            Arr[y,x] = 0
        if house == 0:
            Arr[y,x] = 1
    return Arr
#%%
#Part 1
ks = np.array([0.1,10.])
Days = 5*(10**4)
for k in ks:
    for i in range(Days):
        Neigh = Change(Neigh,k)
    p.figure(k)
    p.imshow(Neigh)
#%%
#Part 2
ks2 = np.linspace(0.,2.,20)
fig,ax = p.subplots(1,1,figsize=(10,10))
ts = np.array([0])
ms = np.array([(2*np.sum(Neigh)-400)])
for k in ks2:
    NewN = np.copy(Neigh)
    Newt = np.copy(ts)
    Newm = np.copy(ms)
    for i in range(int(Days/5)):
        Newt = np.append(Newt,Newt[i]+1)
        NewN = Change(NewN,k)
        m = 2*np.sum(NewN)-400
        Newm = np.append(Newm,m)
    ax.plot(Newt,Newm,label="k = "+str(k))
#ax.legend()
ax.set_title("Difference between Dogs and Cats Over Time")
ax.set_xlabel("Time [Iterations]")
ax.set_ylabel("Difference m [Number]")
#%%
ks3 = np.linspace(0.,2.,20)
SDs = np.array([])
Goal = np.array([])
ms2 = np.array([])
for k in ks3:
    NewN2 = np.copy(Neigh)
    for sim in range(10):
        SimSDs = np.copy(SDs)
        Simm = np.copy(ms2)
        for i in range(int(10**5)):
            NewN2 = Change(NewN2,k)
            m = 2*np.sum(NewN2)-400
            Simm = np.append(Simm,m)
        SD = np.std(Simm[50000:])
        SimSDs = np.append(SimSDs,SD)
    F = np.mean(SimSDs)
    Goal = np.append(Goal,F)

fig2,ax2 = p.subplots(1,1)
ax2.plot(ks3,Goal)
ax2.set_title("Mean Standard Deviation of m vs k")
ax2.set_xlabel("k")
ax2.set_ylabel("Mean Standard Deviation of m")