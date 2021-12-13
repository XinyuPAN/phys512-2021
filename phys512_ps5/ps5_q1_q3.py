import numpy as np
import matplotlib.pyplot as plt

def wpconv(array, s):
    #"wrap around"convolution
    assert(len(array)==len(s)) #len(array) and len(s) should be the same!
    conv=np.zeros(len(array))
    for i in range(len(array)):
        k = 0
        for j in range(len(array)):
            k = k+array[j]*s[j-i]
        conv[i]=k
    return conv

def shift_array(array, shift_amount):
    s = np.zeros(len(array))
    s[shift_amount%len(array)]=1 #"wrap around", so the value of "shift_amount" can >len(array) and can <0
    return wpconv(array,s)

if __name__ == '__main__':

    x = np.linspace(0,100,1001)
    y = np.exp(-0.5*(x-5)**2) #gaussian starts at the centre of the array
    y_shifted = shift_array(y,len(x)//2)
   
    q = 3

    if q==1:
        #q1:shift a gaussian array by half of its length
        plt.plot(y, label='original gaussian(centre at 501)')
        plt.plot(y_shifted, label='shifted by half of its length(500)')
        plt.legend()
        plt.savefig('./gauss_shift.png')
        plt.show()

    if q==2:
        #q2:correlation of gaussian with itself
        assert(len(x)==len(y)) #!!!
        self_corr = np.fft.ifft(np.fft.fft(x)*np.conjugate(np.fft.fft(y)))
        plt.clf()
        plt.plot(np.abs(self_corr))
        plt.title('correlation of gaussian with itself')
        plt.savefig('./gauss_self_corr.png')
        plt.show()
    
    if q==3:
        #q3:correlaiton of gaussian with a shifted gaussian
        assert(len(x)==len(y))
        shifted_corr = np.fft.ifft(np.fft.fft(y_shifted)*np.conjugate(np.fft.fft(y)))
        plt.clf()
        plt.plot(np.abs(shifted_corr))
        plt.xlabel('shift amount')
        plt.xticks(np.arange(0,1001,100))
        plt.savefig('./gauss_shift_corr.png')
        plt.show()



    