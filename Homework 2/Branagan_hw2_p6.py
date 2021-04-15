#Ryan Branagan
#Collaborators: N/A
#Branagan_hw2_p6.py
#1/17/19

import numpy as np
import pylab as p

#Input values
a = 0.1
b = 2.
points = 1000

#Define our function of sin(1/x)
def sinoinv(x):
    y = np.sin(x**(-1))
    return y

#Create an array of x values
xarray = np.linspace(a,b,points)

#Method with loop
output1 = np.zeros(points)
for i,x in enumerate(xarray):
    output1[i] = sinoinv(x)

#Method without loop
output2 = sinoinv(xarray)

#Plotting
p.plot(xarray,output1,label="With a for loop")
p.plot(xarray,output2,label="Without a for loop")
p.legend()
p.show()