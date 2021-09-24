import numpy as np

# use polynomial.chebyshev.chebfit to model y=log2(x), x range from 0.5 to 1
x = np.linspace(0.5, 1, 100)
deg = 0
cheb_fit = np.polynomial.chebyshev.chebfit(x, np.log2(x), deg, full=True)
while cheb_fit[1][0][0] >= 10**(-6):
    deg = deg+1
    cheb_fit = np.polynomial.chebyshev.chebfit(x, np.log2(x), deg, full=True)
cheb_coe = cheb_fit[0]
cheb_resid = cheb_fit[1][0][0]
cheb_degree = deg # deg = 4

# routine mylog2: this function should be able to take the natural log of any positive number
N = 1000
y1, y2 = np.frexp(N) # N = y1*2**y2
y1_e, y2_e = np.frexp(np.exp(1)) # break up Euler's number into mantissa and exponent
#lnN = log2(N)/log2(e)=(y2*log2(y1))/(y2_e*log2(y1_e))
fit_lnN = (y2*np.polynomial.chebyshev.chebval(y1, cheb_coe))/(y2_e*np.polynomial.chebyshev.chebval(y1_e, cheb_coe)) 

