import matplotlib
import pyaudio
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use('Qt5Agg')

# define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# initialize pyaudio
p = pyaudio.PyAudio()

# open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# initialize plot
fig = plt.gcf()
fig.show()
fig.canvas.draw()

# start audio stream
while True:
    data = stream.read(CHUNK)
    data = np.frombuffer(data, dtype=np.int16)

    fft_data = np.fft.rfft(data) # rfft removes the mirrored part that fft generates
    fft_freq = np.fft.rfftfreq(len(data), d=1/RATE) # rfftfreq needs the signal data, not the fft data
    plt.plot(fft_freq, np.absolute(fft_data)) # fft_data is a complex number, so the magnitude is computed here
    plt.xlim(np.amin(fft_freq), np.amax(fft_freq))
    fig.canvas.draw()
    plt.pause(0.005)
    fig.canvas.flush_events()
    fig.clear()
