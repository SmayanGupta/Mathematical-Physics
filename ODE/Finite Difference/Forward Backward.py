'''Smayan Gupta
19/17067
Section-A
Bsc Physics Hons'''
import matplotlib.pyplot as plt
import numpy as np
#stepsize
h=0.01
#initial number of atoms
y0=8000
b0=8000
b=[]
y=[]
#points on the x axis
x=np.arange(0,16,h)
#forward difference
for i in x-1:
    
    y1=(1-0.231*h)*y0
    if i==14:
        print('value using forward difference is:',y1)
    y.append(y1)
    y0=y1

#backward difference
for i in x-1:
    
    b1=b0/(1+0.231*h)
    if i==14:
        print('value using backward difference is:',b1)
    b.append(b1)
    b0=b1

#print(len(y))
#plot comparing the two results
plt.plot(x,b,'r',linewidth=5,alpha=0.5)
plt.plot(x,y,'b')
plt.show()
#print(y)
#print(x)

'''OUTPUT:
    value using forward difference is: 248.60763724016581
value using backward difference is: 250.60685766529534
actual value:246'''



