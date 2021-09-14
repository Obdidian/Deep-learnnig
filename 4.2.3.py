import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train, t_train),(x_text,t_text)=\
    load_mnist(normalize=True,one_hot_label=True)

print(x_train.shape) #(60000, 784)
print(t_train.shape) #(60000, 10)

print()

train_size=x_train.shape[0]
batch_size=10
batch_mask=np.random.choice(train_size,batch_size)
x_batch=x_train[batch_mask]
t_batch=t_train[batch_mask] #np.random.choice() =>> 지정한 수중 무작위로 원하는 수 꺼냄

print(np.random.choice(60000,10))