import numpy as np
import matplotlib.pyplot as plt

#place a window to reduce spectral leakage

N = 100 #100 samples
n = np.arange(N)
k = 1.5 # non-interger frequency sin wave
y = np.sin(2*np.pi*k*n/N)

window = 0.5-0.5*np.cos(2*np.pi*n/N)
yfft = np.fft.rfft(y*window)
plt.plot(np.abs(yfft),'y--*',label='windowed')
plt.plot(np.abs(np.fft.fft(y))[:N//2],'.',label='no window')
plt.title('place a window to reduce spectral leakage')
plt.savefig('./window.png')
plt.legend()
plt.show()

