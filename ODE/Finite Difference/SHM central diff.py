'''Smayan Gupta
19/17067
Section-A
Bsc Physics Hons'''
import numpy as np
import matplotlib.pyplot as plt

n=1000
h=1/n
#making 3 matrices
a=1
b=(h*h-2)
c=1
X=np.ones(n)*a
Y=np.ones(n+1)*b
Z=np.ones(n)*c    

    
#adding diagonals to make tri-diagonal matrix
M=np.diag(X,-1)+np.diag(Y,0)+np.diag(Z,1)
M[0][0]=1
M[0][1]=0
M[n][n-1]=0
M[n][n]=1
#print(M)

#constant matrix=0
B=np.zeros(n+1)
B[0]=1
B[n]=1
#print(B)


#solution matrix
sol=np.linalg.solve(M,B)
#print(sol)
#time axis discretization 
T=np.linspace(0, np.pi/2,n+1)

#print(T)

plt.plot(T,sol)
plt.show()
