import numpy as np
import matplotlib.pyplot as plt


fs = 500
t = np.arange(-10, 10, 1/fs)
B = 10 # if we increase this frequency, the frequency of 20 will also pass from this filter. 
A = 0.01

y = 2*np.sinc(2*B*t)
m_t = np.sin(10*np.pi*t) + np.sin(40*np.pi*t)

y_t = np.convolve(y, m_t)[10*fs:30*fs]

y_f = np.fft.fft(y_t)
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