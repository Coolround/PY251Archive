#Ryan Branagan
#Collaborators: N/A
#Branagan_hw9_p1.py
#3/19/19

import numpy as np
import pylab as p
#%%
#This is when I did it by hand before
#print(Drag(6.97352815))

#Parameters
t0 = 0 # [s]
tf = 8 # [s]
points = 1000

#Function for motion in air
def Drag(t):
    B = 0.02 # [s^-1]
    g = 9.81 # [m/s^2]
    vy0 = 35. # [m/s]
    return -((g*t)/B)+((vy0+(g/B))/B)*(1-np.exp(-B*t))

#Bisection method
Guesses = np.array([[5,8],[6,7],[6.9,7]])
Cs = np.zeros(len(Guesses))
for i,G in enumerate(Guesses):
    a = G[0]
    b = G[1]
    while True:
        c = (a+b)/2
        if np.abs(Drag(b)-Drag(a)) < 0.001:
            Cs[i] = c
            break
        if np.sign(Drag(c)) == np.sign(Drag(a)):
            a = c
        if np.sign(Drag(c)) == np.sign(Drag(b)):
            b = c

#Landing point
print("("+str(Cs[0])+","+str(Drag(Cs[0]))+")")

#Plotting
ts = np.linspace(t0,tf,points)

fig,ax = p.subplots(1,1)
ax.plot(ts,Drag(ts),"-")
ax.plot(Cs[0],Drag(Cs[0]),"rx",label="Landing Point: t="+str(round(Cs[0],3)))
ax.legend()
ax.set_title("Position over Time with Landing Point")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Position [m]")