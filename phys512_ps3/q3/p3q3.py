import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

data = np.loadtxt("/Users/panxinyu/Desktop/dish_zenith.txt")
x, y, z = data[:,0], data[:,1], data[:,2]

## z = m0*(x**2+y**2)+m1*x+m2*y+m3
## z = A*m, z(475*1), A(475*4), m(4*1)
## calculate A
A = np.zeros((len(z), 4))
A[:, 0] = x**2 + y**2
A[:, 1] = x
A[:, 2] = y
A[:, 3] = 1

## calculate m: m = ((A.T*N.inv*A).inv)*(A.T*N.inv*z)
lhs = np.linalg.inv(A.T @ A)
rhs = A.T @ z
m = lhs @ rhs
 
## from m, we know (a, x0, y0, z0) = (m0, -m1/2a, -m2/2a, m3-a*x0**2-a*y0**2)
a = m[0]
x0 = -m[1] / (2*a)
y0 = -m[2] / (2*a)
z0 = m[3] - a * x0**2 - a* y0**2


print("assume no noise:")
print(f"m0 = {m[0]}, m1 = {m[1]}, m2 = {m[2]}, m3 = {m[3]}")
print(f"a = {m[0]}, x0 = {x0}, y0 = {y0}, z0 = {z0}")
print("it's my best fit parameter assuming there's no noise in data (x,y,z)")
##output:
##assume no noise:
##m0 = 0.00016670445477401342, m1 = 0.0004535990279793565, m2 = -0.019411558852636, m3 = -1512.3118166739073
##a = 0.00016670445477401342, x0 = -1.3604886221974717, y0 = 58.22147608157965, z0 = -1512.8772100367883
##it's my best fit parameter assuming there's no noise in data (x,y,z)


plt.clf()
fig = plt.figure(figsize=(10,10))
ax = p3.Axes3D(fig)
## add the paraboloid we fitted, use meshgrid
n_para = 100
x_para = np.linspace(np.min(x), np.max(x), n_para)
y_para = np.linspace(np.min(y), np.max(y), n_para)
x_fit, y_fit = np.meshgrid(x_para, y_para)
z_fit = m[0]*(x_fit**2+y_fit**2) + m[1]*x_fit + m[2]*y_fit + m[3]
ax.plot_wireframe(x_fit, y_fit, z_fit, color='y')
## plot (x,y,z)
ax.scatter3D(x, y, z, color='b')

plt.show() 