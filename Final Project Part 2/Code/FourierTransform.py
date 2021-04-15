
#get_ipython().system('pip install wavio')


# In[4]:


import wavio
import numpy as np
import matplotlib.pyplot as plt
import os # This lets us deal with filesystems (to read in wav files)
from scipy.signal import spectrogram


# In[5]:


# Grab all of the files in the "Wav" directory
allFiles = os.listdir("Wav/")

# Now we only take the files which have a the extension ".wav"
wavFiles = ["Wav/" + str(i) for i in allFiles if i[-3:len(i)] == "wav"]
wavFiles.sort()

# Now our array of data, which is blank at first (empty Wav objects)
readData = [wavio.Wav(0, 0, 0) for i in range(len(wavFiles))]
# Read in the data
for i in range(len(wavFiles)):
    readData[i] = wavio.read(wavFiles[i])
    
# Create a dictionary
# This means that we access each individual set of data using the file name instead
# of an index like a regular array
wavData = dict(zip(wavFiles, readData))

# And we also want to read in the background noise
background = wavio.read("background.wav")
avgBackground = np.average(background.data.flatten())


# In[10]:


# Now create an array of empty strings where we will put the notes
strNotes = ["" for i in range(len(wavData))]    

# And an index since wav in our for loop is a string (since wavData is a dictionary)
i = 0

for wav in wavData:
    # Grab all of the data from the Wav object
    data = wavData[wav].data.flatten() - avgBackground

    # And the sampling rate (aka inverse of the time interval)
    dt = 1 / wavData[wav].rate

    # Now do the actual fourier transform and get the power spectrum
    fArr = abs(np.fft.fftfreq(len(data), dt))
    fftArr = abs(np.fft.fft(data))**2

    #plt.plot(fArr, np.real(fftArr))
    #plt.xlim([0, 2000])
    #plt.title(wav)
    #plt.show()
    
    plt.figure(i)
    f, t, Sxx = spectrogram(data, wavData[wav].rate)
    plt.pcolormesh(t, f, Sxx)
    plt.show()
    
    # We use the method identifyNotes to look at the maximums on the power spectrum
    #f = identifyNotes(fArr, fftArr, tolerance=.5)
    
    # Store the final string with the file name, and any notes being playing
    #strNotes[i] = str(wav) + ": " + str(f)
    
    # Increase our index, since the for loop doesn't do this for us
    i += 1
    
# Print
for i in range(len(strNotes)):
    print(strNotes[i])


# In[7]:


# This gives an estimate of the dominant frequencies in the sound
# file given the fourier transform
def identifyNotes(freq, data, tolerance = 1.0):
    
    # Open the file
    # Instead of manually typing each frequency note pair, I took the source code
    # for the following website and parse it below
    # https://www.seventhstring.com/resources/notefrequencies.html
    file = open("frequencies.txt")

    lines = file.read()
    #print(lines)

    # Here we are removing the html table formatting to just leave the data
    lines = lines.replace("tr", "")
    lines = lines.replace("td", "")
    lines = lines.replace("th", "")
    lines = lines.replace("<", "")
    lines = lines.replace(">", "")
    lines = lines.replace("\t", "")
    lines = lines.replace(" ", "")

    # Now split it into lines
    arr = lines.split("\n")  

    # And remove some blank lines
    while "" in arr:
        arr.remove("")

    # And remove all of the / lines too
    while "/" in arr:
        arr.remove("/")

    # Split the first line, since it contains the note headers
    notes = arr[0].split("/")    

    keys = []
    freqs = []
    for i in range(len(arr)-1):
        for j in range(1, len(notes)-1):
            keys.append(notes[j] + str(i))
            freqs.append(float(arr[i+1].split("/")[j]))

    # Create a dictionary with our frequencies and keys
    frequencies = dict(zip(freqs, keys))

    # Now search for frequencies who have a maximum that is comparable to the absolute maximum
    # Having a lower tolerance with mean more notes will be detected as being played
    fArr = freq[np.where(data > tolerance * max(data))]
    
    
    notes = []
    
    # Now look for notes by comparing the detected frequencies to the dictionary we created above
    # We say that if the frequency is within 10 Hz of the frequency for that note, it is being played
    for i in range(len(fArr)):
        for j in frequencies:
            if abs(fArr[i] - j) < 5.0:
                notes.append(frequencies[j])
                
    return np.unique(notes)