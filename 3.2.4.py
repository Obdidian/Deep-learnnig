import numpy as np
import matplotlib.pyplot as mat
def sigmoid(x):
    return 1/(1+ np.exp(-x))
def step_function(x):
    return np.array(x>0, dtype=np.int)

x= np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

x= np.arange(-5.0,5.0,0.1)
y1= sigmoid(x)
y2= step_function(x)
mat.plot(x,y1, label="sigmoid")
mat.plot(x, y2,linestyle="--", label="step-function")
mat.ylim(-0.1,1.1)
mat.legend()
mat.show()