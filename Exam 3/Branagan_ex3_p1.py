#Ryan Branagan
#Collaborators: Jack Featherstone, John Paul Habeeb, Mason Lovejoy-Johnson, and Grant Sherril
#Branagan_ex3_p1.py
#4/17/19

import numpy as np
import pylab as p
import wavio as wav
from scipy.signal import spectrogram
#%%
Bells = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\bells.wav")
BellDat = Bells.data.flatten()
BellDat = BellDat.astype(float)
BellRate = Bells.rate

Cello = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\cello.wav")
CelloDat = Cello.data.flatten()
CelloDat = CelloDat.astype(float)
CelloRate = Cello.rate

Clar = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\clarinet.wav")
ClarDat = Clar.data.flatten()
ClarDat = ClarDat.astype(float)
ClarRate = Clar.rate

Flute = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\flute.wav")
FluteDat = Flute.data.flatten()
FluteDat = FluteDat.astype(float)
FluteRate = Flute.rate

Oboe = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\oboe.wav")
OboeDat = Oboe.data.flatten()
OboeDat = OboeDat.astype(float)
OboeRate = Oboe.rate

Sax = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\sax-alto.wav")
SaxDat = Sax.data.flatten()
SaxDat = SaxDat.astype(float)
SaxRate = Sax.rate

Trumpet = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\trumpet.wav")
TrumpetDat = Trumpet.data.flatten()
TrumpetDat = TrumpetDat.astype(float)
TrumpetRate = Trumpet.rate

Violin = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\violin.wav")
ViolinDat = Violin.data.flatten()
ViolinDat = ViolinDat.astype(float)
ViolinRate = Violin.rate

Xylo = wav.read("C:\\Users\\ryan-\\Documents\\251\\Exam 3\\Data\\xylophone.wav")
XyloDat = Xylo.data.flatten()
XyloDat = XyloDat.astype(float)
XyloRate = Xylo.rate
#%%
def Transform(Data,Rate):
    dt = (1/Rate)
    A = np.abs(np.fft.fft(Data))
    A = A/max(A)
    B = ((np.abs(A))**2)
    C = np.abs(np.fft.fftfreq(len(Data),dt))
    return A,B,C
#%%
BellSig,BellPower,BellFreq = Transform(BellDat,BellRate)
CelloSig,CelloPower,CelloFreq = Transform(CelloDat,CelloRate)
ClarSig,ClarPower,ClarFreq = Transform(ClarDat,ClarRate)
FluteSig,FlutePower,FluteFreq = Transform(FluteDat,FluteRate)
OboeSig,OboePower,OboeFreq = Transform(OboeDat,OboeRate)
SaxSig,SaxPower,SaxFreq = Transform(SaxDat,SaxRate)
TrumpetSig,TrumpetPower,TrumpetFreq = Transform(TrumpetDat,TrumpetRate)
ViolinSig,ViolinPower,ViolinFreq = Transform(ViolinDat,ViolinRate)
XyloSig,XyloPower,XyloFreq = Transform(XyloDat,XyloRate)
#%%
fig1,((Bellax,Celloax,Clarax),(Fluteax,Oboeax,Saxax),(Trumpetax,Violinax,Xyloax)) = p.subplots(3,3,figsize=(12,16))

Bellax.axvline(261.6,color='k',linestyle='--')
Bellax.plot(BellFreq,BellPower,'r')
Bellax.set_title("Bells Power Spectrum")
Bellax.set_xlim(0,((8*261.6)+10))

Celloax.axvline(261.6,color='k',linestyle='--')
Celloax.plot(CelloFreq,CelloPower,'orange')
Celloax.set_title("Cello Power Spectrum")
Celloax.set_xlim(0,((8*261.6)+10))

Clarax.axvline(261.6,color='k',linestyle='--')
Clarax.plot(ClarFreq,ClarPower,'yellow')
Clarax.set_title("Clarinet Power Spectrum")
Clarax.set_xlim(0,((8*261.6)+10))

Fluteax.axvline(261.6,color='k',linestyle='--')
Fluteax.plot(FluteFreq,FlutePower,'g')
Fluteax.set_title("Flute Power Spectrum")
Fluteax.set_xlim(0,((8*261.6)+10))

Oboeax.axvline(261.6,color='k',linestyle='--')
Oboeax.plot(OboeFreq,OboePower,'b')
Oboeax.set_title("Oboe Power Spectrum")
Oboeax.set_xlim(0,((8*261.6)+10))

Saxax.axvline(261.6,color='k',linestyle='--')
Saxax.plot(SaxFreq,SaxPower,'indigo')
Saxax.set_title("Sax Power Spectrum")
Saxax.set_xlim(0,((8*261.6)+10))

Trumpetax.axvline(261.6,color='k',linestyle='--')
Trumpetax.plot(TrumpetFreq,TrumpetPower,'violet')
Trumpetax.set_title("Trumpet Power Spectrum")
Trumpetax.set_xlim(0,((8*261.6)+10))

Violinax.axvline(261.6,color='k',linestyle='--')
Violinax.plot(ViolinFreq,ViolinPower,'m')
Violinax.set_title("Violin Power Spectrum")
Violinax.set_xlabel("Frequency")
Violinax.set_xlim(0,((8*261.6)+10))

Xyloax.axvline(261.6,color='k',linestyle='--')
Xyloax.plot(XyloFreq,XyloPower,'gray')
Xyloax.set_title("Xylophone Power Spectrum")
Xyloax.set_xlim(0,((8*261.6)+10))
#%%
f,t,Sxx = spectrogram(OboeDat,OboeRate)
p.pcolormesh(t, f, Sxx)
p.ylabel('Frequency [Hz]')
p.ylim(0,2000)
p.xlabel('Time [sec]')
p.show()