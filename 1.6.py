import numpy as np
import random

a = np.array([random.randint(0, 100) for i in range(0, 100, 1)]) 
c = a[:, 1] < 55

print(c)