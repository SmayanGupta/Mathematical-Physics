#Eulers method
import numpy as np
from matplotlib import pyplot as plt

def f1(z,t):
    return z[t]
def f2(y,t):
    return -y[t]
guess=4

y0=1
h=0.01
n=int(1//h)
Y=[y0]
Z=[guess]
t0=0
X=[t0]

while t0<=5:
    y1=y0+ f1(y0,t0)*h
    Y.append(y1)
    y0=y1
    t0=t0+h
    X.append(t0)

#X=np.linspace(0,5,n+1)
plt.plot(X,Y)
plt.show()    
    
