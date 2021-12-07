import numpy as np
import matplotlib.pyplot as plt

u = np.random.rand(10**6)
v = np.random.rand(10**6)*0.7358
x = v/u
accept = (u <= np.sqrt(np.exp(-x)))
x_accept = x[accept]
u_accept = u[accept]
v_accept = v[accept]
plt.clf()
plt.plot(u_accept, v_accept, '.')
plt.title('accepted (u,v)')
plt.xlabel('u')
plt.ylabel('v')
plt.show()

bin_vals, bin_edges = np.histogram(x_accept, bins=100, density=False)
bin_centers = 0.5*(bin_edges[:-1]+bin_edges[1:])
func = np.exp(-bin_centers)
plt.clf()
plt.bar(bin_centers, bin_vals/bin_vals.sum(), width = bin_centers[1]-bin_centers[0], edgecolor='green', label='sample')
plt.plot(bin_centers, func/func.sum(), c='r', label='PDF')
plt.text(5, 0.08, f"efficiency: {np.mean(accept)*100:2.0f}%") #efficiency of this generator is its acceptance rate
plt.xlim([0,6])
plt.xlabel("x")
plt.ylabel("p(x)")
plt.legend()
plt.show()