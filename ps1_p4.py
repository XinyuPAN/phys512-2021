import numpy as np
import scipy.interpolate as intp
import matplotlib.pyplot as plt
import math

fun = np.cos
xmin = -math.pi/2
xmax = math.pi/2
x = np.linspace(xmin, xmax, 7)
y = fun(x)
xx = np.linspace(x[0], x[-1],1001) 

#"true" function, y=cosx
yy_true = fun(xx) 
plt.clf()
plt.plot(x, y, '*')
plt.plot(xx, yy_true)

#polynomoial
pp = np.polyfit(x, y, 9)
yy_poly = np.polyval(pp, xx)
plt.plot(xx, yy_poly)
print('polynomial: mean error is '+repr(np.mean(np.abs(yy_poly-yy_true))))

#spline
spln = intp.splrep(x, y)
yy_spln = intp.splev(xx, spln)
plt.plot(xx, yy_spln)
print('spline: mean error is '+repr(np.mean(np.abs(yy_spln-yy_true))))

#ratoinal function
#p(x)/q(x)=y(x)  q(x)=1+ax+bx^2+...
#matrix: [1 x x**2 x**3 ... -yx -yx**2 -yx**3 ...][p;q]=y
def rat_eval(p, q, x):
    top = 0
    for i in range(len(p)):
        top = top+p[i]*x**i
    bot = 1
    for i in range(len(q)):
        bot = bot+q[i]*x**(i+1)
    return top/bot

def rat_fit(x, y, n, m):
    assert(len(x) == n+m-1)
    assert(len(y) == len(x))
    mat = np.zeros([n+m-1, n+m-1])
    for i in range(n):
        mat[:,i ]=x**i
    for i in range(1, m):
        mat[:, i-1+n] = -y*x**i
    pars = np.dot(np.linalg.inv(mat), y)
    p = pars[:n]
    q = pars[n:]
    return p,q

#[1 x x^2 x^3 -yx -yx^2 -yx^3 -yx^4][p;q] = y
# interpolation orders are n=4, m=5
n=4
m=5
p, q=rat_fit(x, y, n, m)
yy_interp = rat_eval(p, q, xx)
plt.plot(xx, yy_interp)
print('rational function: mean error is '+repr(np.mean(np.abs(yy_interp-yy_true))))