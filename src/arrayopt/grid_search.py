import numpy as np
from models import array_config, op_set
import matplotlib.pyplot as plt
from backends import *

def main():
    # following two lines can be initialized/combined later
    array = array_config(2, 4, 11, FOVL=70, angle_step = 0.1)
    op = op_set()  # you can provide the frequency of operation

    rxP = np.zeros((1, array.nTx*array.nRx))
    S = np.zeros((array.nTx*array.nRx, 2))
    for b1 in range(1, 9):
        for b2 in range(b1+1, 10):
            for b3 in range(b2+1, round(array.L/2)-2):
                a1 = array.L - b3
                S = np.array([[0, b1, b2, b3, a1, a1+b1, a1+b2, a1+b3]])
                rxP = S*0.5*op.wvlngth

                SM = steering_matrix(rxP, array.FOV, op.wvlngth)

                # for angle in array.FOV:
                SV = steering_vector(rxP, 0, op.wvlngth)
                A = np.matmul(SV.T, SM)/(array.nTx*array.nRx)
                vals, indices = local_max(abs(A[0]))
                print(abs(A[0]))
                plt.plot(array.FOV[0],20*np.log10(abs(A[0])))
                plt.plot(array.FOV[0][indices],20*np.log10(vals),'ro')
                plt.ylim([-30,0])
                plt.show()
                print(indices,vals)



if __name__ == "__main__":
    main()
