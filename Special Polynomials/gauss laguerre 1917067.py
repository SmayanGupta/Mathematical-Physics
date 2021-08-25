# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 08:17:43 2021

@author: Smayan GUpta
19/17067
Seection-A
Semester-4
Bsc Physics Hons
"""

import sympy as sp
import numpy as np

import matplotlib.pyplot as plt
#defining a recursive function for laguerre polynomials
def laguerre(n,x):
    if n==0:
        return x*0+1
    elif n==1:
        return -x + 1
    else: 
        return ((2*n-1-x)*laguerre(n-1, x) -(n-1)*laguerre(n-2, x))/n
    
#plotting laguerre polynomials to check validity
'''X=np.linspace(-5,15,100)
for i in range(0,4):
    plt.plot(X,laguerre(i,X))'''
    
    
#defining a function for gauss laguerre    
def gausslaguerre(f,n):
    # making a symbol x
    x=sp.Symbol('x') 
    #all roots of the given laguerre polynomial
    r=sp.Poly(laguerre(n,x)).nroots() 
    #print(r)
    #creating an empty array for weights
    w=[0]*len(r) 
    #dummy variable y
    y=sp.Symbol('y') 
    for j in range(0,len(r)):
        i=j-1
        #interpolation formula
        l=(y-r[i])/(r[j]-r[i])  
        i-=1
        #print(l)
        while r[i]!=r[j]:
            l*=(y-r[i])/(r[j]-r[i])
            #negative indexing for reverse iteration
            i-=1  
            #print(l)
        #print(l)
        w[j]=sp.integrate(l*sp.exp(-y),(y,0,sp.oo)) #weights after integrating
    #print(w)
    integral=0
    for i in range(0,len(r)):
        integral+=w[i]*f(r[i]) #summing the weights with function value at roots
    print(integral)

#function to integrate
def f(x):
    return sp.exp(x)/(2+x**2)
print('answer by gauss laguerre quadrature')
gausslaguerre(f,4)
print('exact solution',np.pi/(2*np.sqrt(2)))
    
''' OUTPUT
answer by gauss laguerre quadrature
1.03420451832852
exact solution 1.1107207345395915
'''