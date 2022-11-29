import numpy as np
from dataclasses import dataclass, field

@dataclass
class array_config:
    nTx : int
    nRx : int
    L : int
    FOVL : int = field(default_factory= int)
    FOV : list[int] = field(default_factory=list)
    angle_step: float = 1.0
    def __post_init__(self)-> list:
        vals = np.arange(-self.FOVL,self.FOVL,self.angle_step) 
        self.FOV = np.array([vals])

@dataclass
class op_set: # frequency/wavelength of operation
    frequency : float = 77e9
    c : float = field(init=False,default=299792458) 
    wvlngth : float = field(default=1)
    def __post_init__(self):
        self.wvlngth = self.c/self.frequency


