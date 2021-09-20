# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 10:49:01 2021

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
    return (x)*diff(f,x,x)+ (1-x)*diff(f,x)
n=6
b=[]
for i in range(n):
    b.append(x**i)
#print(b)
def Reverse(lst):
    return [ele for ele in reversed(lst)]

laguerre=np.zeros((n,n))
#def optrans():
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
    laguerre[:,i]=fcoef

values,vectors= np.linalg.eig(laguerre)
for i in range(n):
    print('{} is the {}th eigenvalue and associated eigenvector is \n'.format(values[i],i),vectors.T[i])



x1=np.linspace(0,8,100)

for j in range(n):
    lag1=[]
    for i in range(100):
        lag1.append(-np.dot(vectors.T[j]*values[j],b).subs(x,x1[i]))

    plt.plot(x1,lag1)