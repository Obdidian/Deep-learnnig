import numpy as np

def sum_squares_error(y,t):
    print(0.5*np.sum((y-t)**2))


#ex - 1 정답이 2
t=[0,0,1,0,0,0,0,0,0,0]
 # ex -2 "2" 일 확률이 제일 높다고 추정함
y=[0.1,0.05,0.6,0.0,0.05,0.1,0.0,0.1,0.0,0.0]
sum_squares_error(np.array(y),np.array(t))

print()

#ex - 3 "7"일 확률이 제일 높다고 추정함
y=[0.1,0.05,0.1,0.0,0.05,0.1,0.0,0.6,0.0,0.0]
sum_squares_error(np.array(y),np.array(t))


