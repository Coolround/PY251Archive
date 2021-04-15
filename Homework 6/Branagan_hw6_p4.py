#Ryan Branagan
#Collaborators: N/A
#Branagan_hw6_p4.py
#2/20/19

import numpy as np
#%%
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