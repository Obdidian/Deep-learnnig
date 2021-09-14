import numpy as np
import matplotlib.pylab as mat

def nummerical_diff(f,x):
    h=1e-4
    return (f(x+h)-f(x-h))/(2*h)

def funcion_1(x):#예시 함수
    return 0.01*x**2 + 0.1*x

x=np.arange(0.0,20.0,0.1)
y=funcion_1(x)
mat.xlabel("x")
mat.ylabel("f(x)")
mat.plot(x,y)
mat.show()

print((nummerical_diff(funcion_1,5)))
print((nummerical_diff(funcion_1,10)))
