import os
import numpy as np
from numpy.linalg import *
# x->-0.2,0.2
# y->0
# z->0.7,1.3
kpts = []
for i in range(-20, 21, 1):
    for k in range(70, 131, 1):
        kpts.append([round(0.01*i,2), 0.0, round(0.01*k, 2)])
kpts = np.array(kpts)
np.savetxt('kpts.dat', kpts, fmt='%.3f')
