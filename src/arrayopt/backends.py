import numpy as np


def steering_matrix(Pos, FOV, wvlngth):
    # returns a broadside 0 degrees steering matrix for given array
    # Pos : position of the antenna elements of the array
    SM = np.exp(-1j*(2*np.pi/wvlngth)*np.matmul(Pos.T, np.sin(FOV*np.pi/180)))
    return SM


def steering_vector(Pos, scan_angle, wvlngth):
    # returns a steering vector in specified scan angle
    # Pos : position of the antenna elements of the array
    SV = np.exp(1j*Pos.T*np.sin(scan_angle*np.pi/180)*2*np.pi/wvlngth)
    return SV


def local_max(input_array):
    # will return indices of the local max and the amplitudes/values
    # input_array : should be a np 1 dimensional array
    vals = []
    indices = []
    for i in range(1, len(input_array)-1):
        if input_array[i-1] < input_array[i] and input_array[i] > input_array[i+1]:
            vals.append(input_array[i])
            indices.append(i)

    return vals, indices

def local_min(input_array):
    # will return indices of the local min and the amplitudes/values
    # input_array : should be a np 1 dimensional array
    vals = []
    indices = []
    for i in range(1, len(input_array)-1):
        if input_array[i-1] > input_array[i] and input_array[i] < input_array[i+1]:
            vals.append(input_array[i])
            indices.append(i)

    return vals, indices
