import numpy as np
import matplotlib.pylab as plt
def step_function_only_int(x):
    if x>0:
        return 1
    else:
        return 0

def step_function(x):
    return np.array(x>0, dtype=np.int) #astype = 원하는 자료형으로 바꿔줌

x= np.arange(-5.0,5.0,0.1)
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)#y축의 범위
plt.show()

