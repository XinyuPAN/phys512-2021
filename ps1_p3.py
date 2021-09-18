import numpy as np
import scipy.interpolate as intp
import matplotlib.pyplot as plt

def lakeshore(V,data):
    Ts = np.zeros(len(data))
    Vs = np.zeros(len(data))
    for i in range(len(data)):
        Ts[i] = data[i][0]
        Vs[i] = data[i][1]
    plot_Vs = np.linspace(min(Vs)-3, max(Vs)+3, 2000)
    interpolation = intp.CubicSpline(Vs, Ts)
    plot_Ts = interpolation(plot_Vs)
    plt.plot(Vs, Ts, '*')
    plt.plot(plot_Vs, plot_Ts, linestyle='--')
    plt.show()
    

    #estimate errors, bootstrap sampling
    interpolated_Ts = []
    rng = np.random.default_rng(seed=12345)
    n_resamples = 13 #times of resample
    n_samples = 31 # number of resample points
    for i in range(n_resamples):
        indices = list(range(Vs.size))
        to_interp = rng.choice(indices, size = n_samples, replace=False)
        to_interp.sort()
        new_interpolation = intp.CubicSpline(Vs[to_interp], Ts[to_interp])
        interpolated_Tsi = new_interpolation(V)
        interpolated_Ts.append(interpolated_Tsi)

    interpolated_Ts = np.array(interpolated_Ts)
    stds = np.std(interpolated_Ts, axis = 0)
    mean = np.mean(interpolated_Ts, axis = 0)
    return(stds, mean)
        


V_input = [1,3,13,131]
data = np.loadtxt('lakeshore.txt')
result = lakeshore(V_input, data)
print(f'for V_input: {V_input}, predicted temperature are: {result[0]}, and estimated errors are: {result[1]}')



