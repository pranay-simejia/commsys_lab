import numpy as np
import matplotlib.pyplot as plt

B = 10
A = 0.01
Fs = 5*B
t = np.arange(-15, 15, 1/Fs)

y = 2*np.sinc(2*B*t)
hf = np.fft.fft(y)/Fs
N=len(hf)
freq_axis = np.linspace(-Fs/2, Fs/2, N)  ###extremely important to sample freq
hf_abs= abs(hf)
hf_abs_sorted=np.fft.fftshift(hf_abs)   ##### for increasing freq samples
fig, axs=plt.subplots(2)
axs[0].plot(t,y)
plt.title('Time Domain')
plt.xlabel('time')
plt.ylabel('Amplitude')
axs[1].plot(freq_axis,hf_abs_sorted)
plt.title('Freq Domain')
plt.xlabel('Freq')
plt.ylabel('Amplitude')
plt.show()