import numpy as np

from arrayopt.backends import local_peaks, local_troughs


def test_local_max():

    input = np.array([1,2,3,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0])

    act_peaks = local_peaks(input,rev=False)

    des_vals = [4,5]
    des_indices = [3,12]

    assert list(act_peaks.values()) == des_vals
    assert list(act_peaks.keys()) == des_indices


def test_local_min():
    
    input = np.array([5,4,3,2,1,2,3,4,5,4,3,4,5,6])

    act_troughs = local_troughs(input,rev=False)

    des_vals = [1,3]
    des_indices = [4,10]

    assert list(act_troughs.values()) == des_vals
    assert list(act_troughs.keys()) == des_indices