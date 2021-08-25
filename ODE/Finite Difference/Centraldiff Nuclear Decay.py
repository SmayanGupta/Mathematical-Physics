'''Smayan Gupta
19/17067
Section-A
Bsc Physics Hons'''
import numpy as np
import matplotlib.pyplot as plt
N0=8000
T_h=3
lam=0.693/T_h
ti=0
tf=15
N=lambda t:N0*np.exp(-lam*t)

'''
central difference:y'(x)=(y(x+h)-y(x-h))/(2*h)
'''

n=100
h=(tf-ti)/n
t=ti

#making 3 matrices
A=-1
B=2*h*lam
C=1
X=np.ones(n-2)*A
Y=np.ones(n-1)*B
Z=np.ones(n-2)*C    

    
#adding diagonals to make tri-diagonal matrix
M=np.diag(X,-1)+np.diag(Y,0)+np.diag(Z,1)
#print(M)

#constant matrix=0
D=np.zeros(n-1)
D[0]=N0
print(D)
#least oscillation with no second value
'''giving boundary value using function 
because without it answer oscillates'''
D[n-2]=-N(tf)
'''can remove comment here to do same with 
half life but answer still oscillates'''
#D[n//5-1]=-4000


#print(D)
#solution matrix
sol=np.linalg.solve(M,D)
#time axis discretization 
T=[]
for i in range(n):
    t=t+h
    T.append(t)
#print(T)
T=np.delete(T,(0))
#print('values of N',dol)
plt.plot(T,sol)
      
