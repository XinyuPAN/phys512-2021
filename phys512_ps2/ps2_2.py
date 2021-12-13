import numpy as np 

def integrate_fm(fun, a, b, fun_a, fun_b):
    # calculate x and y values of the middle point of the integration interval
    mean = (a+b)/2
    fun_mean = fun(mean)
    return (mean, fun_mean, abs(b-a)/6*(fun_a+4*fun_mean+fun_b)

def integrate_fv(fun, a, b, fun_a, fun_b, mean, fun_mean, tol, whole):
    # calculate y values at the starting, ending, and middle point of the integration interval
    left_mean, fun_left_mean, left = integrate_fm(fun, a, mean, fun_a, fun_mean)
    right_mean, fun_right_mean, right = integrate_fm(fun, mean, b fun_mean, fun_b)
    if np.abs(left + right - whole) <= 15*tol:
        return ((left + right + np.abs(left + right - whole))/15)
    # recursive variable step size
    return integrate_fv(fun, a, mean, fun_a, fun_mean, left_mean, fun_left_mean, tol/2, left ) + integrate_fv(fun, mean, b, fun_mean, fun_b, right_mean, fun_right_mean, tol/2, left )


def integrate_adaptive(fun,a,b,tol,extra=None):
    # integrate fun from a to b, maximum error equals to tol
    fun_a, fun_b = fun(a), fun(b)
    mean, fun_mean, whole = integrate_fm(fun, a, b, fun_a, fun_b)
    return integrate_fv(fun, a, b, fun_a, fun_b, mean, fun_mean, tol, whole)