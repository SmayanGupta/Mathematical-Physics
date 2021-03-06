# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:37:15 2021

@author: smaya
"""

import sympy as sp
import numpy as np

import matplotlib.pyplot as plt
#defining a recursive function for laguerre polynomials
def hermite(n,x):
    if n==0:
        return x*0+1
    elif n==1:
        return 2*x
    else: 
        return ((2*x)*hermite(n-1, x) -2*(n-1)*hermite(n-2, x))
'''X=np.linspace(-2,2,100)
for i in range(0,5):
    plt.plot(X,hermite(i,X))'''
    
    
global s
s=0.1

#defining a function for gauss hermite  
def gausshermite(f,n):
     # making a symbol x
    x=sp.Symbol('x')
    #all roots of the given hermite polynomial
    r=sp.Poly(hermite(n,x)).nroots() 
    for i in (0,len(r)-1):
        r[i]=round(r[i],4)
    #print(r)
    #creating an empty array for weights
    w=[0]*len(r) 
    #dummy variable y
    y=sp.Symbol('y') 
    #shifting to variable t
    #t=(y-2)/(np.sqrt(2)*s)
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
        #rounding off to get a more exact guess
        w[j]=round(sp.integrate(l*sp.exp(-y**2),(y,-sp.oo,sp.oo)).evalf(),4)
        #can remove this comment to get exact answer due to more decimal points
        #w[j]=sp.integrate(l*sp.exp(-t**2),(y,-sp.oo,sp.oo)).evalf() #weights after integrating
    #print(w)
    integral=0

    for i in range(0,len(r)):
        #print(w[i])
        #print(f(r[i]))
        integral+=w[i]*f(r[i]) #summing the weights with function value at roots
    print("for s=",s,":",integral/(np.sqrt(pi)))
      

        
'''s=1
t=(x-2)/(sp.sqrt(2)*s)  '''
global pi
pi=np.pi
def f(x):
    return (x*np.sqrt(2)*s+5)
#gausshermite(f,2)


'''OUTPUT 
for exact solution
for s=1 : 5.00000000000000
for s=0.01 : 5.00000000000000
for s=0.1 : 5.00000000000000
for solution with less decimal places
for s= 1 : 4.99984781391702
for s= 0.1 : 4.99984781391702
for s= 0.01 : 4.99984781391702
for s= 1000000000000000 : 4.93665885604287 (different result)
'''

def simpson(function,a,b,n):
    h=(b-a)/n #step size
    i=a
    sum=0
    counter=0
    while i<=b:
        if(i==a):
            sum+= function(a)
        elif(i==b):
            sum+= function(b)
            break
        elif(counter%2!=0):
            sum+= 4*function(i)
        elif(counter%2==0):
            sum+= 2*function(i)
        counter+=1
        i+=h
    return sum*h/3 
def g(x):
     return (np.exp(-float(x)**2)*(x*np.sqrt(2)*s+5))/(np.sqrt(pi))
a=1000
print(simpson(g,-a,a,10000))

'''
 OUTPUT 
 for simpsons
 for s=1:4.036824541588584
 for s=0.1: 4.036824541588584
 for s=0.01: 5.000000000000003
'''

