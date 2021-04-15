#Ryan Branagan
#Collaborators: N/A
#Branagan_hw6_p3.py
#2/20/19

import numpy as np
import pylab as p

def Error(Exp,Exact):
    return np.abs(Exp-Exact)/np.abs(Exact)
#%%
#Because of studying for many tests I'm just going to copy the code given
#since in the problem statement it says to add to the exisiting code
tau = 0.7        # mean lifetime
N0 = 100.0 # initial number of nuclei

tmin = 0.0
tmax = 4.0

nts=1000

# Create an array to hold the times
t_array = np.linspace(tmin, tmax, nts, endpoint=False)  
dt = t_array[1] - t_array[0]  #  This is an easy way to define dt that is not error prone

# Empty array to hold the number of nuclei
N_array = np.zeros( len(t_array) )

# Empty array for Euler comparison
#N_euler = np.zeros( len(t_array) )


# Do the simple Euler solution
# Set the initial condition
#N_euler[0] = N0
#for it in range(0, len(t_array)-1 ):
#    N_euler[it+1] = N_euler[it] + dt * (-1./tau * N_euler[it])
    
# The above should have been familiar from Lesson 8.

# Do the RK2 solution
N_array[0] = N0
for it in range(0, len(t_array)-1 ):
    t  = t_array[it]         # Don't necessarily need it but nice to have
    th = t_array[it] + dt/2  # Note: we don't need this for this particular ODE
    
    N_h           = N_array[it] + dt/2 * (-1./tau * N_array[it])
    N_array[it+1] = N_array[it] + dt * (-1./tau * N_h)
    
    
# Make a plot (note the label for the curve)
#p.plot(t_array, N_euler, 'o', label="Euler Method with nts="+str(nts))
#p.plot(t_array, N_array, 'o', label="RK2 Method with nts="+str(nts))
#p.plot(t_array, N0*np.exp(-t_array/tau),'k:',label="Analytic result")

# Add a legend (based on the labels)
#p.legend()

# Add a horizontal axis
#p.axhline(0.0, color='k', linestyle=':')

# Show the plot
#p.show()

#This is done by hand and really shouldn't be but I don't have much time
#Errors = np.zeros(4)
#Errors[3] = N_array[nts-1]
ntss = [20,50,100,1000]
RK2 = [4.809580927780527371e-01,3.747309716807022961e-01,3.503722925771156071e-01,3.317511822565062940e-01]
Errors2 = Error(RK2,(N0*np.exp(-tmax/tau)))

#Plotting
fig1, ax = p.subplots(1,1)
ax.plot(np.log10(ntss),np.log10(Errors2),'o-')
ax.set_title('Error vs Resolution')
ax.set_xlabel('Resolution')
ax.set_ylabel('Error')

#You would need 1000 points for Euler's method to be as accurate