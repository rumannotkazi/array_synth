import numpy as np
import matplotlib.pyplot as plt
# from arrayopt.backends import local_max
from arrayopt.backends import *
from arrayopt.models import array_config, op_set
a = np.array([[-2, -1, 0, 1]])
b = np.array([[0, 1, 2, 3]])
# a = np.arange(-2,2,1)
# b = np.arange(0,4,1)
# c = np.matmul(a.T,b)

c = np.array([[1,2,3,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0]])
vals = []
indices = []
j=0
for i in range(1,len(c[0])-1) :
    if c[0][i-1]< c[0][i] and c[0][i] > c[0][i+1]:
        vals.append(c[0][i])
        indices.append(i)
        j=j+1


array = array_config(2, 4, 11, FOVL=30, angle_step = 0.1)

print(array.FOV[0])     
