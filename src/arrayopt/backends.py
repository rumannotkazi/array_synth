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


def local_peaks(input_array, rev=True):
    # Returns local peak indices and corresponding values in descending/asceding order based on the values/amplitudes
    # input_array : should be a np 1 dimensional array
    # rev : True -> descending order , False -> descending order
    ret_dict = {}
    sort_dict = {}
    for i in range(1, len(input_array)-1):
        if input_array[i-1] < input_array[i] and input_array[i] > input_array[i+1]:
            ret_dict[i]=input_array[i]
    
    sort_dict = dict(sorted(ret_dict.items(), key= lambda ret_dict:ret_dict[1], reverse=rev))
    return sort_dict

def local_troughs(input_array, rev=True):
    # Returns local troughs(minimums) indices and corresponding values in descending/asceding order based on the values/amplitudes
    # input_array : should be a np 1 dimensional array
    # rev : True -> descending order , False -> descending order
    ret_dict = {}
    sort_dict = {}
    for i in range(1, len(input_array)-1):
        if input_array[i-1] > input_array[i] and input_array[i] < input_array[i+1]:
            ret_dict[i]=input_array[i]

    sort_dict = dict(sorted(ret_dict.items(), key= lambda ret_dict:ret_dict[1], reverse=rev))    
    return sort_dict