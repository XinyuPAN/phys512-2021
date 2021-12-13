import numpy as np

def ndiff(fun,x,full):
    f = fun
    eps = 2**(-52) 
    dx = 1 #try dx = 1

    f3 = (f(x+dx)-3*f(x)+3*f(x-dx)-f(x-2*dx))/(dx**2) #third derivative
    h = (eps*f(x)/f3)**(1/3)

    while h < dx:
        dx = h
        f3 = (f(x+dx)-3*f(x)+3*f(x-dx)-f(x-2*dx))/(dx**2)
        h = (eps*f(x)/f3)**(1/3)

    dx = h
    deriv = (f(x+dx)-f(x-dx))/(2*dx)
    est_error = (f(x)**(2/3))*(f3**(1/3))
    
    
    if full == False:
        print("full==False, numerical derivative is ")
        return deriv
    if full == True:
        x = np.zeros(3)
        x[0] = deriv
        x[1] = dx
        x[2] = est_error
        print("full==True, numerical derivative, dx and estimated error are ")
        return x

ndiff(np.cos, 10, True)