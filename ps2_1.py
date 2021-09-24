import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def fun(Z): # Z: distance from the shell centre; 
    Q = 1 # Q: the total amount of electricity of the shell
    R = 1 # R: radius of the shell
    # set Q&R as 1 to simplify calculation
    int_lim = [-1, 1] # limitation of integration, from -1 to 1
    epsilon = 8.85e-12 # epsilon: vacuum permittivity
    sigma = Q/(4*np.pi*(R**2)) # sigma: electricity density 
    const = (2*np.pi*(R**2)*sigma)/(4*np.pi*epsilon) # constant coefficient of the integration
    u = np.linspace(int_lim[0], int_lim[1], 100)
    int_fun = (Z-R*u)/(R**2+Z**2-2*R*Z*u)**(3/2)
    e_field = integrate.quad(const*int_fun, int_lim[0], int_lim[1])
    return (e_field)


Z = np.linspace(0,3,150)

plt.clf()
plt.plot(Z, fun(Z))
plt.ylabel('E')
plt.title("electric field from an infinitessimally thin spherical shell of charge Q=1 with radius R=1")
plt.xlabel('Z (distance from the shell)')
plt.legend()
plt.show()