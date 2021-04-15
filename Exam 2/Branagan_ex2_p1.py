#Ryan Branagan
#Collaborators: Mason Lovejoy-Johnson, Steven Boswell, Jack Featherstone, and Grant Sherril
#Branagan_ex2_p1.py
#3/21/19

import numpy as np
import pylab as p
from scipy.integrate import odeint
#%%
def deriv(s,t,ma,mb,kl,km,kr,B,w):
    xa = s[0]
    va = s[1]
    xb = s[2]
    vb = s[3]
    deriv = [va,((-1*(kl*xa+km*(xa-xb))-B*va+(0.1*np.sin(w*t)))/(ma)),vb,((-1*(kr*xb+km*(xb-xa))-B*vb)/(mb))]
    return deriv

def DiffEq(si,t0,tf,points,deriv,params):
    ma = params[0]
    mb = params[1]
    kl = params[2]
    km = params[3]
    kr = params[4]
    B = params[5]
    w = params[6]
    t = np.linspace(t0,tf,points)
    s = odeint(deriv,si,t,args=(ma,mb,kl,km,kr,B,w))
    return t,s
#%%
#1
#Initial conditions
si = [0.,0.,0.,0.]
t0 = 0
tf = 200
points = 2001

#Getting Points
ws = np.linspace(0,2,21)
for i,w in enumerate(ws):
    params = [1,1,1,1,1,0.1,w]
    t,solns = DiffEq(si,t0,tf,points,deriv,params)
    xa = solns[:,0]
    va = solns[:,1]
    xb = solns[:,2]
    vb = solns[:,3]
    
    #Plotting
    i,pos = p.subplots(1,1)
    pos.plot(t,xa,"r-",label="Mass A")
    pos.plot(t,xb,"b-",label="Mass B")
    pos.set_ylim([-0.55,0.55])
    pos.set_title('Position of Both Masses Over Time')
    pos.legend()
    pos.set_xlabel('Time [s]')
    pos.set_ylabel('Position [m]')
    pos.annotate('Omega='+str(round(w,2)),xy=(10,10),xycoords='figure pixels')