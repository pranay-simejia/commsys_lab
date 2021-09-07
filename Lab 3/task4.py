import numpy as np
import matplotlib.pyplot as plt


fs = 500
t = np.arange(-10, 10, 1/fs)
B = 10
A = 0.01
# Fs = 5*B
# t = np.arange(-15, 15, 1/Fs)
fm = 5
h = 2*np.sinc(2*B*t) # [ 25 ]

T = 10
m_t = np.ones(t.size)*(t <= T/2).astype(int)*(t >= -T/2).astype(int)

y_t = np.convolve(h, m_t)[10*fs:30*fs]

y_f = np.fft.fft(y_t)/fs
y_f_abs = np.abs(y_f)
freq = np.fft.fftfreq(y_t.size, d=1/fs)
fig, axs=plt.subplots(2)
axs[0].plot(t,y_t)
plt.title('Time Domain')
plt.xlabel('time')
plt.ylabel('Amplitude')
axs[1].plot(freq, y_f_abs)
plt.title('Freq Domain')
plt.xlabel('Freq')
plt.ylabel('Amplitude')
plt.show()