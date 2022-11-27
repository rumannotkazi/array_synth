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
        self.FOV = np.arange(-self.FOVL,self.FOVL,self.angle_step) 