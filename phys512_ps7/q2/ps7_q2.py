import numpy as np
import matplotlib.pyplot as plt

#which of lorentzians, gaussians, and power laws could you use for the bounding distribution?
#make a plot to compare those functions

x = np.linspace(0,10,1000)
plt.clf()
plt.plot(x, np.exp(-x), label='exp')
plt.plot(x, 1/(1+x**2), label='lorentzian')
plt.plot(x, np.exp(-0.5*x**2), label='gaussian')
plt.legend()
plt.show()


#from the plot we can see that: if we scale the lorentzians a liitle bit up, 
#we could lorentizians and exponential for the bounding distribution

#use tan() to generate random numbers
# y = tanx, non-negative deviations x:[0,pi/2] and y:[0,infinity]
x = np.pi/2*np.random.rand(10**6)
y = np.tan(x)
r = np.exp(-y)/(1.05/(1+y**2)) #1.05: scale the lorentzian up
pr = np.random.rand(10**6)
accept = pr<r
y_accept = y[accept]

bin_vals, bin_edges = np.histogram(y_accept, bins=100, density=False)
bin_centers = 0.5*(bin_edges[:-1]+bin_edges[1:])
g = np.exp(-bin_centers)

plt.clf()
plt.bar(bin_centers, bin_vals/bin_vals.sum(), width = bin_centers[1] - bin_centers[0],edgecolor='green', label='sample')
plt.plot(bin_centers, g/g.sum(), c='r', label='PDF')
plt.xlim([0,6])
plt.legend()
plt.text(5, 0.08, f"efficiency: {np.mean(accept)*100:2.0f}%") #efficiency of this generator is its acceptance rate
plt.show()




