import numpy as np
from arrayopt.backends import local_max, local_min


def test_local_max():

    input = np.array([1,2,3,4,3,2,1,0,1,2,3,4,5,4,3,2,1,0])

    act_vals, act_indices = local_max(input)

    des_vals = [4,5]
    des_indices = [3,12]

    assert act_vals == des_vals
    assert act_indices == des_indices


def test_local_min():
    
    input = np.array([5,4,3,2,1,2,3,4,5,4,3,4,5,6])

    act_vals, act_indices = local_min(input)

    des_vals = [1,3]
    des_indices = [4,10]

    assert act_vals == des_vals
    assert act_indices == des_indices