import numpy as np
from arrayopt.backends import steering_vector
from arrayopt.models import array_config, op_set
import matplotlib.pyplot as plt
from arrayopt.backends import *

def main():
    # following two lines can be initialized/combined later
    array = array_config(2, 4, 11, FOVL=15, angle_step = 0.1)
    op = op_set()  # you can provide the frequency of operation
    bestSLL=1
    rxP = np.zeros((1, array.nTx*array.nRx))
    S = np.zeros((array.nTx*array.nRx, 2))
    for b1 in range(1, 13):
        for b2 in range(b1+1, 14):
            for b3 in range(b2+1, round(array.L/2)):
                a1 = array.L - b3
                S = np.array([[0, b1, b2, b3, a1, a1+b1, a1+b2, a1+b3]])
                rxP = S*0.5*op.wvlngth
                print(S)
                SM = steering_matrix(rxP, array.FOV, op.wvlngth)
                val = []
                for angle in array.FOV[0]:
                    SV = steering_vector(rxP, angle, op.wvlngth)
                    A = np.matmul(SV.T, SM)/(array.nTx*array.nRx)
                    peaks = local_peaks(abs(A[0]))
                    val.append(list(peaks.values())[1])
                ec = max(val)
                if max(val) < bestSLL:
                    bestSLL = max(val)
                    b1opt, b2opt, b3opt = b1, b2, b3
                    a1opt = a1


                    # print(vals)

    # Storing the final configuration
    Txopt = [0,a1opt]
    Rxopt = [0, b1opt, b2opt, b3opt]
    bestSLLdB=20*np.log10(bestSLL)

    print(Txopt, Rxopt)
    print(bestSLLdB)

    S = np.array([[0, b1opt, b2opt, b3opt, a1opt, a1opt+b1opt, a1opt+b2opt, a1opt+b3opt]])
    rxP = S*0.5*op.wvlngth
    SM = steering_matrix(rxP, array.FOV, op.wvlngth)    
    SV = steering_vector(rxP, 0, op.wvlngth)
    A = np.matmul(SV.T, SM)/(array.nTx*array.nRx)    
    plt.figure(1)
    plt.plot(array.FOV[0],20*np.log10(abs(A[0])))
    # plt.plot(array.FOV[0][indices],20*np.log10(vals),'ro')
    plt.ylim([-30,0])
    plt.show()

if __name__ == "__main__":
    main()
