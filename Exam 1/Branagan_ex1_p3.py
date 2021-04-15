#Ryan Branagan
#Collaborators: Jack Featherstone, Grant Sherrill, JP Habeeb, Emma Stone, Crosson Nipper, Sally Lord
#Branagan_ex1_p3.py
#2/9/19

import numpy as np
import pylab as p

#%%
#Part a
displacement = np.array([])
y = 0
for i in range(100):
    y = y + np.random.choice([-1,1])
    displacement = np.append(displacement,y)

ts = np.linspace(0,99,100)

fig1, dis = p.subplots(1,1)
dis.plot(ts,displacement)
dis.set_xlabel('Time/Step Number')
dis.set_ylabel('Distance from Origin')
dis.set_title('Distance from Origin vs Time')
p.show()
#%%
#Part b
N = 8000

def FDisp():
    A = np.array([])
    for i in range(100):
        z = np.random.choice([-1,1])
        A = np.append(A,z)
    return np.sum(A)

FDispList = np.array([])
for i in range(N):
    FDispList = np.append(FDispList,(FDisp()))

Avg = np.abs(np.sum(FDispList)/N)
print(Avg)

p.figure(2)
p.hist(FDispList,20)
p.xlabel('Final Displacement')
p.ylabel('Number of Times Occured')
p.title('Frequency of Certain Final Displacements')
p.show()
#%%
#Part c
N = 8000

FDispListS = np.array([])
for i in range(N):
    FDispListS = np.append(FDispListS,(FDisp())**2)

RMS = np.sqrt(np.sum(FDispListS)/N)
print(RMS)

p.figure(3)
p.hist(FDispListS,20)
p.xlabel('Final Displacement Squared')
p.ylabel('Number of Times Occured')
p.title('Frequency of Certain Final Displacements Squared')
p.show()
#%%
#Part d
Trials = 50

def FDisp2(S):
    A = np.array([])
    for i in range(S):
        z = np.random.choice([-1,1])
        A = np.append(A,z)
    return np.sum(A)

steplist = np.linspace(10,5000,50)

Step1 = np.array([])
Step2 = np.array([])
for s in steplist:
    for i in range(Trials):
        Step1 = np.append(Step1,(FDisp2(int(s)))**2)
    Step2 = np.append(Step2,(np.sqrt(np.sum(Step1)/Trials)))
    Step1 = np.array([])

fig4, (p1,p2) = p.subplots(2,1,figsize=(6,8))

p1.plot(steplist,Step2,'o')
p1.set_xlabel('Steps')
p1.set_ylabel('RMS Displacment')
p1.set_title('RMS Displacement vs Steps')

p2.plot(np.log10(steplist),np.log10(Step2),'o')
p2.set_xlabel('Log of Steps')
p2.set_ylabel('Log of RMS Displacement')
p.show()