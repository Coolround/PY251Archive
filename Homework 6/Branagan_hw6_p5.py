#Ryan Branagan
#Collaborators: N/A
#Branagan_hw6_p5.py
#2/20/19

import numpy as np
import pylab as p
#%%
tau = 0.7        # mean lifetime
N0 = 100.0       # initial number of nuclei
tmin = 0.0       # start time
tmax = 4.0       # end time
nts=5           # number of points

# This function calculates the RHS of the differential equation
# for the decay problem: just -(1/tau) * N
def decay_deriv(N,t):
    # The derivative in principle may depend on N and t -- in this
    # case, it only depends on N
    return -(1./tau) * N

# This function runs an Euler solver.  We have to tell it the initial
# value, the min/max time range, the number of time points,
# and how to compute the derivative (we pass in a function
# for this).
def Euler_solver(N_initial, tmin, tmax, nts, deriv):
    N = np.zeros(nts+1)
    t = np.linspace(tmin, tmax, nts+1)
    
    # Note: a way of defining dt that is less error-prone
    dt = t[1] - t[0]
    N[0] = N_initial
    for it in range(0,nts):
        N[it+1] = N[it] + dt * deriv(N[it], t[it])
    return t, N

def RK2_solver(N_initial, tmin, tmax, nts, deriv):
    N = np.zeros(nts+1)
    t = np.linspace(tmin, tmax, nts+1)
    dt = t[1] - t[0]
    
    # Note: a way of defining dt that is less error-prone
    N[0] = N_initial
    for it in range(0, len(t)-1 ):
        #th = t[it] + dt/2  # Note: we don't need this for this particular ODE
        
        N_h           = N[it] + dt/2 * (-1./tau * N[it])
        N[it+1] = N[it] + dt * (-1./tau * N_h)
    return t, N

from scipy.integrate import odeint
def diffeq_solver_from_scipy(N_initial, tmin, tmax, nts, deriv):
    t = np.linspace(tmin, tmax, nts)

    # Note that the order of arguments matches the documentation
    N = odeint(deriv, N_initial, t)

    return t,N

ts,NE = Euler_solver(N0,tmin,tmax,nts,decay_deriv)
NRK = RK2_solver(N0,tmin,tmax,nts,decay_deriv)[1]
NSP0 = diffeq_solver_from_scipy(N0,tmin,tmax,nts+1,decay_deriv)[1]
NSP = np.zeros(nts+1)
for i in range(nts+1):
    NSP[i] = NSP0[i]
Na = N0*np.exp(-ts/tau)

#print(NE)
#print(NRK)
#print(NSP)

fig,ax = p.subplots(1,1)
ax.plot(ts,NE,'o-',label="Euler Method")
ax.plot(ts,NRK,'o-',label="RK2 Method")
ax.plot(ts,NSP,'o-',label="Scipy Method")
ax.plot(ts,Na,'k--',label="Analytical Result")
ax.set_title('Number of Particles Over Time')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Number of Particles')
ax.legend()