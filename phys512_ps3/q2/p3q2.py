import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def decays(t, n):

    ## Half lives, unit: yr
    T = np.array([
    4.5e9,       ##U238
    0.066,       ##Th234
    2.23e-6,     ##Pa234
    2.4e5,       ##U234
    7.7e4,       ##Th230
    1.6e3,       ##Ra226
    1.05e-2,     ##Rn222
    5.57e-6,     ##Po218
    3.06e-3,     ##Pb214
    3.79e-5,     ##Bi214
    0.5e-11,     ##Po214
    22.3,        ##Pb210
    1.37e-2,     ##Bi210
    0.379,       ##Po210 ##and Pb206 is stable
    ])

    k = np.log(2)/T  ##k: decay rate, constant; dn/dt  = -k * n; T is half-life time
    dndt = np.zeros(len(T)+1)
    dndt[:-1] = -k * n[:-1]
    dndt[1:] = dndt[1:] + k*n[:-1]  

    return dndt

if __name__ == '__main__':
    
    ## Half lives, unit: yr
    T = np.array([
    4.5e9,       ##U238
    0.066,       ##Th234
    2.23e-6,     ##Pa234
    2.4e5,       ##U234
    7.7e4,       ##Th230
    1.6e3,       ##Ra226
    1.05e-2,     ##Rn222
    5.57e-6,     ##Po218
    3.06e-3,     ##Pb214
    3.79e-5,     ##Bi214
    0.5e-11,     ##Po214
    22.3,        ##Pb210
    1.37e-2,     ##Bi210
    0.379,       ##Po210 ##and Pb206 is stable
    ])

    
    ## number of atoms of each porducts at t=0
    n0 = np.zeros(len(T)+1)    ## Pb206 doesn't have half life, len(T)+1!
    n0[0] = 1e4     ##at t=0, there're 10,000 U-238 atoms
    
    ## observe it for 1e10^e yr, 2 half-lives of U-238 
    t_begin=0
    t_end=1e10
    ## U238 decays logarithmically, use log10-scale for t
    t_teval = 10**np.linspace(0,np.log10(t_end),1000)

    ## because we know the initial condition and it's a stiff system, choose BDF
    N_end = solve_ivp(decays,[t_begin,t_end],n0, method='BDF',t_eval=t_teval).y

    ## theoratical value of N(Pb206)/N(U238) is exp(k(U238)*t)-1
    k_U238 = np.log(2)/T[0]
    Pb_U_t = (np.exp(k_U238*t_teval)-1)

    plt.clf()
    plt.title('Pb206/U238, log')
    plt.plot(t_teval, Pb_U_t,'g+', label="Theoretical ratio")
    plt.plot(t_teval, N_end[-1,:]/N_end[0,:],'r',label="Calculated ratio") 
    plt.legend()
    plt.xscale('log')
    plt.xlabel('T (yr)')
    plt.ylabel('Pb206/U238')
    plt.show()

    plt.clf()
    plt.title('Th230/U234, full range, log')
    plt.plot(t_teval, N_end[4,:]/N_end[3,:],label="Calculated ratio")
    plt.legend()
    plt.xscale('log')
    plt.xlabel('T (yr)')
    plt.ylabel('Th230/U234')
    plt.show()

    plt.clf()
    plt.title('Th230/U234, interesting range, linear')
    plt.plot(t_teval[0:660], N_end[4,0:660]/N_end[3,0:660], label="Calculated ratio")
    plt.text( 1.6e6,0.2,"Reach average after 1.5 million years.")
    plt.legend()
    plt.xlabel('T (yr)')
    plt.ylabel('Th230/U234')
    plt.show()
