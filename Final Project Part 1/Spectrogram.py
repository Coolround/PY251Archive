#251 Group Project
#4/30/19

import numpy as np
import pylab as p
import matplotlib as m
import wavio
from scipy.signal import spectrogram
#%%
#Read in data based on a list of strings containing the names of files we want to read in
def ReadData(folder,strlist):
    Wavs = [wavio.read("C:\\Users\\ryan-\\Documents\\251\\Final Project\\"+folder+"\\"+string+".wav") for string in strlist]
    Out = []
    for wa in Wavs:
        thing1 = wa.data.flatten()
        thing1 = thing1.astype(float)
        thing2 = wa.rate
        thingray = [thing1,thing2]
        Out.append(thingray)
    return Out

#Manys lists that I used throughout the process
Ones = ['A0','A0#','B0','C1','C1#','D1','D1#','E1','F1','F1#','G1','G1#','A1','A1#','B1']
Twos = ['C2','C2#','D2','D2#','E2','F2','F2#','G2','G2#','A2','A2#','B2']
Threes = ['C3','C3#','D3','D3#','E3','F3','F3#','G3','G3#','A3','A3#','B3']
Fours = ['C4','C4#','D4','D4#','E4','F4','F4#','G4','G4#','A4','A4#','B4']
Fives = ['C5','C5#','D5','D5#','E5','F5','F5#','G5','G5#','A5','A5#','B5']
Sixes = ['C6','C6#','D6','D6#','E6','F6','F6#','G6','G6#','A6','A6#','B6']
Sevens = ['C7','C7#','D7','D7#','E7','F7','F7#','G7','G7#','A7','A7#','B7','C8']
All = Ones+Twos+Threes+Fours+Fives+Sixes+Sevens
strs2 = ['Imagine (Song)','Not a Fan (Song)','Phone in a Pool (Song)']
test = ['Ghost Lights','Volcano','VolcanoPiano','VolcanoM','Imagine (Song)','Boes','A0','AKey','C8','G5','Notes']
test2 = ['Ghost Lights','Ghost Lights Cut']
strs4 = ['Volcano','VolcanoPiano','VolcanoM']

#This is just so I can be lazy
listofstrings = test2
volume = 100
limit = 2500

#Turn my process for making a spectrogram into a definition
def Spectro(Folder,ListofStrings,PercentVolume,FrequencyLimit):
    #Read in the data we want
    Stuff = ReadData(Folder,ListofStrings)
    #Loop through each one and plot its Spectrogram
    for i in range(len(Stuff)):
        p.figure(i)
        f,t,Sxx = spectrogram(Stuff[i][0],Stuff[i][1],nperseg=3000)
        Sxx[749:len(Sxx)] = 0
        #m.colors.Normalize(0,(1*(10**0))) This is something I messed with to try and normalize the data
        #print(np.where(Sxx == np.amax(Sxx))) This is from when we discovered that there were crazy frequencies at very high frequencies
        Sxx = (Sxx/np.amax(Sxx))*100
        p.pcolormesh(t, f, Sxx,vmin=0,vmax=PercentVolume)
        #,cmap='magma' I experimented with different color maps to better display the data but couldn't find anything
        p.title(ListofStrings[i])
        p.ylabel('Frequency [Hz]')
        #p.ylim(0,FrequencyLimit)
        p.xlabel('Time [sec]')
        p.show()

Spectro('Data',listofstrings,volume,limit)
#Spectro('Data\\JPs Notes',Fives,20,2500)