from pyedflib import highlevel
import numpy as np
import matplotlib.pyplot as plt

# read an edf file
signals, signal_headers, header = highlevel.read_edf('MIT EEG Data\chb01_01.edf')
print(signal_headers[0]['sample_rate']) # prints 256

##t = np.linspace(-2*np.pi, 2*np.pi, 500);
##signals = np.stack((np.sin(t), np.sin(2*t), np.sin(3*t)))

dft = np.fft.fft(signals, axis=1)

plt.subplot(1,2,1)
plt.plot(np.transpose(signals))#[0:3,:1000]))
plt.title('Raw signals')
plt.subplot(1,2,2)
plt.plot(np.transpose(dft))#[0:3,:1000]))
plt.title('Fourier transform')
plt.show()
