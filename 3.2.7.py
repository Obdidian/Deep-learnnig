import numpy as np
import matplotlib.pyplot as mat

def relu(x):
    return np.maximum(0,x)
x=np.arange(-5.0,5.0,0.1)
y=relu(x)
mat.plot(x,y)
mat.ylim(-1.0,5.0)
mat.show()
