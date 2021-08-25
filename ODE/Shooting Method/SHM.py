'''Smayan Gupta
19/17067
Section-A
Bsc Physics Hons'''

import numpy as np
import matplotlib.pyplot as plt
#initial and boundary conditions
yf=1
xi=0
xf=np.pi/2
X=np.linspace(xi,xf,159)
#defining a function for eulers method
def euler(g):
    xi=0
    xf=np.pi/2
    yi=1
    h=0.01
    Y=[yi]
    z0=g
    Z=[z0]
    #np.append(X,xf)    
    #print(len(X)
    while xi<=xf:
        y1= yi+ z0*h
        Y.append(y1)
        z1=z0- yi*h
        Z.append(z1)
        yi=y1
        z0=z1
        xi=xi+h
    return Y
#print(len(Z))
#print(X)
#guessing the initial slope
g1=4
g2=-4
Y1=euler(g1)
Y2=euler(g2)
plt.plot(X,Y1,'r',label='guess 1')
plt.plot(X,Y2,'g',label='guess 2')
         
#interpolation method
'''g=best guess
g2=guess 2
g1=guess 1
Y2=solution matrix for guess 2
Y1=solution matrix for guess 1
yf=final boundary value'''
g=g1 + ((g2-g1)*(yf-Y1[-1]))/(Y2[-1]-Y1[-1])
print(g)
plt.plot(X,euler(g),label='best guess')
plt.plot(xf,1,'ro',label='boundary value') 
plt.legend(loc='best')
