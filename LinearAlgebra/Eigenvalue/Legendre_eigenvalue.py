# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 08:40:02 2021

@author: smaya
"""
'''Smayan Gupta
19/17067
Section-A
Bsc Physics Hons'''

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

global x
x=Symbol('x')

def Lop(f):
    return (1-x**2)*diff(f,x,x) -2*x*diff(f,x)
n=6
b=[]
for i in range(n):
    b.append(x**i)
#print(b)
def Reverse(lst):
    return [ele for ele in reversed(lst)]

legendre=np.zeros((n,n))

for i in range(1,n):
    pol=Lop(b[i]).expand()
    #print(pol)
    pol=Poly(pol)
    #print(pol)
    coef=pol.all_coeffs()
    coef=Reverse(coef)
    less=len(b)-len(coef)
    fcoef=coef+[0]*less
    #print(fcoef)
    legendre[:,i]=fcoef

values,vectors= np.linalg.eig(legendre)
values[0]=1
for i in range(n):
    print('{} is the {}th eigenvalue and associated eigenvector is \n'.format(values[i],i),vectors.T[i])


x1=np.linspace(-1,1,100)
for j in range(n):
    leg1=[]
    for i in range(100):
        leg1.append(-np.dot(vectors.T[j]*values[j],b).subs(x,x1[i]))
        
    
    plt.plot(x1,leg1)
