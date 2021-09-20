# -*- coding: utf-8 -*-
"""

'''Smayan Gupta
19/17067
Section-A
Bsc Physics Hons'''
"""

import numpy as np

def qr(A):
    #A=np.array([[1,-2,8],[7,-7,6],[5,7,-8]])
    n=np.shape(A)[0]
    Q=np.zeros((n,n))
    Q[:,0]=A[:,0]/np.linalg.norm(A[:,0])
    np.zeros((n,n))
        
    def mi(i,k):
        sum=0
        for j in range(k):
            sum= sum -np.dot(A[:,i],Q[:,j])*Q[:,j]
            
        return sum
            
    #print(Q)
    for i in range(1,n):
        z=A[:,i]+ mi(i,i) 
        Q[:,i]=z/np.linalg.norm(z)
    #print(Q)
    
    R=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i>j:
                R[i][j]=0
            else:
                R[i][j]=np.dot(A[:,j],Q[:,i])
    return Q,R
#print(R)
#for i in range(7):
 #   print(np.dot(R,Q))
 
A=np.array([[1,-2,8],[7,-7,6],[5,7,-8]])
B=np.array([[0,2],[2,3]])
C=np.array([[4,-2,3,-7],[1,2,6,8],[8,5,1,5],[-5,8,-5,3]])

e1=np.linalg.eigvals(A)
print('Eigenvalues by inbuilt',e1)
for i in range(157):
    Q,R=qr(A)
    A=np.dot(R,Q)

print('Matrix After iteration',A)
print('Eigenvalues are ',np.sort(np.diag(A)))


#For second question 
e2=np.linalg.eigvals(C)
print('Eigenvalues by inbuilt',e2)
for i in range(100):
    Q,R=qr(C)
    C=np.dot(R,Q)

print('Matrix After iteration',C)
print('Eigenvalues are ',np.sort(np.diag(C)))

'''OUTPUT
Eigenvalues by inbuilt [  5.8191119   -6.76795297 -13.05115892]
Matrix After iteration [[-1.30511589e+01 -6.26889108e+00  3.56030603e+00]
 [ 3.75439101e-44 -6.76795297e+00  6.24701734e+00]
 [ 3.79866416e-54  1.01503486e-09  5.81911190e+00]]
Eigenvalues are  [-13.05115892  -6.76795297   5.8191119 ]
Eigenvalues by inbuilt [-5.64826955+2.98745334j -5.64826955-2.98745334j  8.49506633+0.j
 12.80147277+0.j        ]
Matrix After iteration [[ 1.28014728e+01  2.41965127e-01  1.64863119e+00  4.68078685e+00]
 [-1.13720733e-17  8.49506633e+00 -7.98482590e+00 -2.27157330e+00]
 [ 1.55553657e-29  7.47098998e-12 -5.80402344e+00  4.91800194e+00]
 [-5.57966744e-30  4.99502014e-13 -1.81966922e+00 -5.49251566e+00]]
Eigenvalues are  [-5.80402344 -5.49251566  8.49506633 12.80147277]

'''










