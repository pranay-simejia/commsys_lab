import matplotlib.pyplot as plt
import numpy as np

# Analog Signal

step_size = 1e-4
t=np.arange(0,0.1,step_size)
theeta = 2*(np.pi)*7*10*t
m=np.sin(theeta)

plt.plot(t,m)
plt.show()

# Digital Signal
sampling_interval=np.arange(145)
# Scaling sampling
dt = 1e-4

x=np.sin(2*np.pi*7*10*sampling_interval*dt)

plt.stem(sampling_interval,x)
plt.show()