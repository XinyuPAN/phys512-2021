import numpy as np

eps = 2**(-52) #double precision
h1 = eps**(1/3)
h2 = 100*eps**(1/3)
x1 = 15
x2 = 1500

deriv_c1 = (np.exp(x1+h1)-np.exp(x1-h1))/(2*h1)
deriv_a1 = np.exp(x1)
deriv_c2 = (np.exp(0.01*(x2+h2))-np.exp(0.01*(x2-h2)))/(2*h2)
deriv_a2 = np.exp(x2)

print(deriv_c1, deriv_a1)
print(deriv_c2, deriv_a2)




