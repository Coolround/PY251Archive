#Ryan Branagan
#Collaborators: Jack Featherstone, Grant Sherrill, JP Habeeb, Emma Stone, Crosson Nipper, Sally Lord
#Branagan_ex1_p2.py
#2/9/19

import numpy as np
import pylab as p

#Parameters
a = -2
b = 2
points = 1000

#Part a
def func(t):
    if np.abs(t) < 1:
        return np.exp(-2*((np.arctanh(t))**2))
    else:
        return 0

ts = np.linspace(a,b,points)

ans = np.array([])
for t in ts:
    ans = np.append(ans,func(t))

fig1, ax = p.subplots(1,1)
ax.plot(ts,ans,'o')
ax.set_xlabel('t')
ax.set_ylabel('f(t)')
ax.set_title('f(t) vs t')
p.show()
#%%
#Part B

#Define Integration Technique
#I don't need Simpson's Rule but here it is
def simp3(f,a,b,N):
    h = (b-a)/N
    
    #Left
    xl = np.array([])
    for A in range(N):
        xl = np.append(xl,(a+A*h))
    Left = np.sum(f(xl)*h)
    
    #Right
    xr = np.array([])
    for B in range(N):
        xr = np.append(xr,(a+(B+1)*h))
    Right = np.sum(f(xr)*h)
    
    #Trap
    Trap = (Left+Right)/2
    
    #Mid
    xm = np.array([])
    for C in range(N):
        xm = np.append(xm,(a+(C+1/2)*h))
    Mid = np.sum(f(xm)*h)
    
    return (Trap/3)+(2*Mid/3)

def DiffEqs(f,a,b,dt,strr):
    if strr == 'No':
        alist = np.array([f(a)])
        blist = np.array([0])
        ts = np.linspace(a,b,(1/dt))
        for i,t in enumerate(ts):
            y = alist[i]+f(t)*dt
            alist = np.append(alist,y)
            z = blist[i]+alist[i]*dt
            blist = np.append(blist,z)
        alist = np.delete(alist,len(ts))
        blist = np.delete(blist,len(ts))
        return ts, alist, blist
    if strr == 'Yes':
        alist = np.array([f(a)])
        ts = np.linspace(a,b,(1/dt))
        for i,t in enumerate(ts):
            y = alist[i]+f(t)*dt
            alist = np.append(alist,y)
        alist = np.delete(alist,len(ts))
        return ts, alist

#Define Derivative Technique
def D5PS(f,x,h):
    return (f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)

def D23PS(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)
#%%
#Case 1
f = func
a = -2
b = 2
h = 10**-3

#T values
ts = np.linspace(a,b,(1/h))

#Getting points
position = np.array([])
velocity = np.array([])
acceleration = np.array([])
for t in ts:
    velocity = np.append(velocity,D5PS(func,t,h))
    acceleration = np.append(acceleration,D23PS(func,t,h))
    position = np.append(position,func(t))

#Plotting
fig2, (pos,vel,accel) = p.subplots(3,1)

pos.plot(ts,position,'o')
pos.axhline(0, color='k', linestyle='--')
pos.set_ylabel('Position [m]')
pos.set_title('Case 1: Position, Velocity, Acceleration vs Time')

vel.plot(ts,velocity,'o')
vel.set_ylabel('Velocity [m/s]')
vel.axhline(0, color='k', linestyle='--')

accel.plot(ts,acceleration,'o')
accel.set_ylabel('Acceleration [m/s^2]')
accel.set_xlabel('Time [s]')
accel.axhline(0, color='k', linestyle='--')

p.show()
#%%
#Case 2
f = func
a = -2
b = 2
dt = 10**-3
strr = 'Yes'

#Getting points
ts,position = DiffEqs(f,a,b,dt,strr)

velocity = np.array([])
acceleration = np.array([])
for t in ts:
    acceleration = np.append(acceleration,D5PS(f,t,dt))
    velocity = np.append(velocity,func(t))

#Plotting
fig3, (pos,vel,accel) = p.subplots(3,1)

pos.plot(ts,position,'o')
pos.axhline(0, color='k', linestyle='--')
pos.set_ylabel('Position [m]')
pos.set_title('Case 2: Position, Velocity, Acceleration vs Time')

vel.plot(ts,velocity,'o')
vel.set_ylabel('Velocity [m/s]')
vel.axhline(0, color='k', linestyle='--')

accel.plot(ts,acceleration,'o')
accel.set_ylabel('Acceleration [m/s^2]')
accel.set_xlabel('Time [s]')
accel.axhline(0, color='k', linestyle='--')

p.show()
#%%
#Case 3
f = func
a = -2
b = 2
dt = 10**-3
strr = "No"

#Getting points
ts,velocity,position = DiffEqs(f,a,b,dt,strr)

acceleration = np.array([])
for t in ts:
    acceleration = np.append(acceleration,func(t))

#Plotting
fig4, (pos,vel,accel) = p.subplots(3,1)

pos.plot(ts,position,'o')
pos.axhline(0, color='k', linestyle='--')
pos.set_ylabel('Position [m]')
pos.set_title('Case 3: Position, Velocity, Acceleration vs Time')

vel.plot(ts,velocity,'o')
vel.set_ylabel('Velocity [m/s]')
vel.axhline(0, color='k', linestyle='--')

accel.plot(ts,acceleration,'o')
accel.set_ylabel('Acceleration [m/s^2]')
accel.set_xlabel('Time [s]')
accel.axhline(0, color='k', linestyle='--')

p.show()