import time
import numpy as np
from matplotlib import pyplot as plt
import camb
from scipy import stats

def get_spectrum(pars,lmax=3000):
    H0=pars[0]
    ombh2=pars[1]
    omch2=pars[2]
    tau=pars[3]
    As=pars[4]
    ns=pars[5]
    pars=camb.CAMBparams()
    pars.set_cosmology(H0=H0,ombh2=ombh2,omch2=omch2,mnu=0.06,omk=0,tau=tau)
    pars.InitPower.set_params(As=As,ns=ns,r=0)
    pars.set_for_lmax(lmax,lens_potential_accuracy=0)
    results=camb.get_results(pars)
    powers=results.get_cmb_power_spectra(pars,CMB_unit='muK')
    cmb=powers['total']
    tt=cmb[2:,0]   # monopole and dipole removed
    return tt[2:]

if __name__ == '__main__':
    
    pars=np.asarray([60,0.02,0.1,0.05,2.00e-9,1.0])
    planck=np.loadtxt('/Users/panxinyu/Desktop/COM_PowerSpect_CMB-TT-full_R3.01.txt',skiprows=1)
    ell=planck[:,0]
    spec=planck[:,1]
    spec_errs=0.5*(planck[:,2]+planck[:,3])
    
    ## assumed errors are Gaussian and uncorrelated, however, this assumption should be tested!
    ## calculate chisquare, if chisquare is very large and the probability of errors being random is very small, then this assumption is bad
    ## set confidence level at 99.9%

    model=get_spectrum(pars)
    model=model[:len(spec)]
    resid=spec-model
    chisq=np.sum( (resid/spec_errs)**2)
    df = len(resid)-len(pars)

    print(f"\nrelevant critical value of chisquare = {stats.chi2.isf(0.001, df):6.2f}")
    ##relevant critical value of chisquare is 2725.27
    ##thus, if chisqure which we calculated out > 2725.27, the model is bad

    print(f"\nchisq = {chisq:6.2f}, degrees of freedom = {df}")
    ##chisq = 14151.63, and 2501 degrees of freedom
    ##bad model


    planck_binned=np.loadtxt('/Users/panxinyu/Desktop/COM_PowerSpect_CMB-TT-binned_R3.01.txt',skiprows=1)
    errs_binned=0.5*(planck_binned[:,2]+planck_binned[:,3]);
    plt.clf()
    plt.plot(ell,model)
    plt.errorbar(planck_binned[:,0],planck_binned[:,1],errs_binned,fmt='.')
    plt.title("spectrum with parameters") #pars=np.asarray([60,0.02,0.1,0.05,2.00e-9,1.0])
    plt.show()


    ##new set of parameters
    pars=np.asarray([69, 0.022, 0.12, 0.06, 2.1e-9, 0.95])
    model=get_spectrum(pars)
    model=model[:len(spec)]
    resid=spec-model
    chisq=np.sum( (resid/spec_errs)**2)
    df = len(resid)-len(pars)

    print(f"\nchisq = {chisq:6.2f}, degrees of freedom = {df}")
    ##chisq = 3506.74, and 2501 degrees of freedom
    ##still bad model

    planck_binned=np.loadtxt('/Users/panxinyu/Desktop/COM_PowerSpect_CMB-TT-binned_R3.01.txt',skiprows=1)
    errs_binned=0.5*(planck_binned[:,2]+planck_binned[:,3]);
    plt.clf()
    plt.plot(ell,model)
    plt.errorbar(planck_binned[:,0],planck_binned[:,1],errs_binned,fmt='.')
    plt.title("spectrum with better parameters")
    plt.show()