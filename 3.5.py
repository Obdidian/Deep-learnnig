import numpy as np
import matplotlib.pylab as mat

# a= np.array([0.3,2.9,4.0])

# exp_a=np.exp(a)
# print(exp_a)
#
# sum_exp_a=np.sum(exp_a)
# print(sum_exp_a)
# y=exp_a/sum_exp_a
# print(y)
# 소프트맥스 함수


#def sofemax_mayoverflow(a):
#    exp_a=np.exp(a)
#    sum_exp_a=np.sum(exp_a)
#    y=exp_a/sum_exp_a
#    return y

def softmax(a):
    c=np.max(a)
    exp_a=np.exp(a-c)
    sum_exp_a=np.sum(exp_a)
    y=exp_a/sum_exp_a
    return y

x=np.arange(0,1,0.01)
y=softmax(x)

mat.plot(x,y)
mat.show()
#소프트맥스 함수 =>> 0~1 사이의 숫자로 나오고, 함숫값들의 총합이 1이다!
# 즉, 소프트맥스 함수의 출력은 확률로 해석할수있음!

