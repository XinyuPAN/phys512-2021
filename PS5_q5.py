#random walk
import numpy as np
import matplotlib.pyplot as plt

#we should generate N trajectories of random walk samples to see the proporties
Ntraj = 100 #generate 100 trajectories
Nstep = 1000 #1,000 steps in each trajectories
RW = np.zeros((Ntraj, Nstep))
RW_ft = np.zeros((Ntraj, Nstep), dtype='complex')
for i in range(Ntraj):
    RW[i,:] = np.cumsum(np.random.randn(Nstep))
    RW_ft[i,:] = np.fft.fft(RW[i, :]) #calculate power spectrum

RW_power = np.mean(np.abs(RW_ft)**2/Nstep**2, axis=0)
k = np.arange(1, 15)
expect_power = RW_power[1]/k**2 
plt.title('Power spectrum')
plt.plot(k, RW_power[1:15], 'r*', label='got')
plt.plot(k, expect_power, label='1/k**2')
plt.xlabel('k')
plt.ylabel('Power')
plt.savefig('./ps_randomwalk.png')
plt.show()





