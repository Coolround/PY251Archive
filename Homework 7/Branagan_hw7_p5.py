#Ryan Branagan
#Collaborators: N/A
#Branagan_hw7_p4.py
#2/27/19

import numpy as np
import pylab as p
#%%
#1
#Parameters
k = 15
m = 0.3
t0 = 0
tf = 5
points = 5001

#Input Matrix
M = np.matrix([[2*k,-k],[-k,2*k]])

#Solving
evals,evecs = np.linalg.eig(M)

ws = np.sqrt(evals/m)

w1 = ws[0]
C11 = evecs[0,0]
C12 = evecs[0,1]
w2 = ws[1]
C21 = evecs[1,0]
C22 = evecs[1,1]

print(w1)
print(C11)
print(C12)
print(w2)
print(C21)
print(C22)

#Equations
ts = np.linspace(t0,tf,points)
x11 = C11*np.cos(w1*ts)
x12 = C12*np.cos(w1*ts)
x21 = C21*np.cos(w2*ts)
x22 = C22*np.cos(w2*ts)

#Plottting
fig1,ax1 = p.subplots(1,1)
ax1.plot(ts,x11,label="Mass 1")
ax1.plot(ts,x12,label="Mass 2")
ax1.set_title('Position Over Time for Both Masses for Omega='+str(w1))
ax1.legend()
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Position [m]')

fig2,ax2 = p.subplots(1,1)
ax2.plot(ts,x21,label="Mass 1")
ax2.plot(ts,x22,label="Mass 2")
ax2.set_title('Position Over Time for Both Masses for Omega='+str(w2))
ax2.legend()
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Position [m]')
#%%
#2
#Answer in report
#%%
#3
#Parameters
k = 15
m = 0.3
t0 = 0
tf = 5
points = 5001

#Input Matrix
M = np.matrix([[2*k,-k],[-k,k]])

#Solving
evals,evecs = np.linalg.eig(M)

ws = np.sqrt(evals/m)

w1 = ws[0]
C11 = evecs[0,0]
C12 = evecs[0,1]
w2 = ws[1]
C21 = evecs[1,0]
C22 = evecs[1,1]

#Equations
ts = np.linspace(t0,tf,points)
x11 = C11*np.cos(w1*ts)
x12 = C12*np.cos(w1*ts)
x21 = C21*np.cos(w2*ts)
x22 = C22*np.cos(w2*ts)

#Plottting
fig3,ax3 = p.subplots(1,1)
ax3.plot(ts,x11,label="Mass 1")
ax3.plot(ts,x12,label="Mass 2")
ax3.set_title('Position Over Time for Both Masses for Omega='+str(w1))
ax3.legend()
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Position [m]')

fig4,ax4 = p.subplots(1,1)
ax4.plot(ts,x21,label="Mass 1")
ax4.plot(ts,x22,label="Mass 2")
ax4.set_title('Position Over Time for Both Masses for Omega='+str(w2))
ax4.legend()
ax4.set_xlabel('Time [s]')
ax4.set_ylabel('Position [m]')