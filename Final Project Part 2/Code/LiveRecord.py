import numpy as np
import matplotlib.pyplot as plt
import wavio
import sounddevice as sd
import sys

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
                
    return np.unique(notes).tolist()


recordDuration = 1 # seconds
sampleRate = 44000 # samples/sec

while True:
    recordData = sd.rec(int(recordDuration*sampleRate), samplerate=sampleRate, channels=2)
    sd.wait()

    #print(sd.query_devices())

    #print(recordData)
    #data = wavio.read("Wav/A2.wav")
    #print(data.rate)
    #sd.play(data.data.flatten(), data.rate)
    #sd.play(recordData, sampleRate)
    #print(max(recordData.flatten()))

    # Since we want to filter based on volume, we can set a tolerance
    # I don't know what units this is in, I just messed around with it
    # until things looked good
    volumeTolerance = .05

    if max(recordData.flatten()) < volumeTolerance:
        continue
    
    fArr = abs(np.fft.fftfreq(len(recordData.flatten()), 1.0/sampleRate))
    fftArr = abs(np.fft.fft(recordData.flatten()))**2

    fftArr /= max(fftArr)

    #plt.plot(fArr, np.real(fftArr))
    #plt.show()
    
    sys.stdout.write("\r                                                                                ")
    sys.stdout.write("\r" + str(identifyNotes(fArr, fftArr, tolerance=.35)))