#Ryan Branagan
#Collaborators: N/A
#Branagan_hw11_p2.py
#4/10/19

import numpy as np
import pylab as p
#%%
#Import Data
Dat = np.loadtxt("C:\\Users\\ryan-\\Documents\\251\\Homework 11\\Lesson16_Data.txt")
tax = Dat[:,0]
aot = Dat[:,1]

#Plot Original Signal
fig1, og = p.subplots(1,1)
og.plot(tax,aot,'r-')
og.set_title("Signal Over Time")
og.set_xlabel("Time [s]")
og.set_ylabel("Signal Amplitude")

#Fast Transform
Aof = np.fft.fft(aot)/len(tax)
freq = np.fft.fftfreq(len(tax),(tax[1]-tax[0]))

#Plot Transform
fig2, ax = p.subplots(1,1)
ax.plot(freq,np.abs(np.real(Aof)),'b-',label="Real Component")
ax.plot(freq,np.abs(np.imag(Aof)),'g-',label="Complex Component")
ax.set_title("Fast Fourier Transform of the Signal")
ax.set_xlabel("Frequency [1/s]")
ax.set_ylabel("Fast Fourier Transform")
ax.legend()