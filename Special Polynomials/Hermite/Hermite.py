# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 10:04:44 2021

@author: Smayan GUpta
19/17067
Seection-A
Semester-4
Bsc Physics Hons
"""

import sympy as sp
import numpy as np

import matplotlib.pyplot as plt
#defining a recursive function for hermite polynomials
def hermite(n,x):
    if n==0:
        return x*0+1
    elif n==1:
        return 2*x
    else: 
        return ((2*x)*hermite(n-1, x) -2*(n-1)*hermite(n-2, x))
#plotting to check validity of hermite polynomials
'''X=np.linspace(-2,2,100)
for i in range(0,5):
    plt.plot(X,hermite(i,X))'''
    
#declaring a global sigma variable
global s
s=1000

#defining a function for gauss hermite  
def gausshermite(f,n):
     # making a symbol x
    x=sp.Symbol('x')
    #all roots of the given hermite polynomial
    r=sp.Poly(hermite(n,x)).nroots() 
    print(r)
    #creating an empty array for weights
    w=[0]*len(r) 
    #dummy variable y
    y=sp.Symbol('y') 
     #shifting to variable t
    t=(y-2)/(np.sqrt(2)*s)
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
        w[j]=sp.integrate(l*sp.exp(-t**2),(y,-sp.oo,sp.oo)).evalf() #weights after integrating
    print(w)
    integral=0
    for i in range(0,len(r)):
        integral+=w[i]*f(r[i]) #summing the weights with function value at roots
    print(integral)


global pi
pi=np.pi
#function to integrate
def f(x):
    z=(x-2)/(np.sqrt(2)*s)
    return np.exp(-z**2)*(x+3)/(np.sqrt(2*pi*s**2))

#gausshermite(f,2)

'''OUTPUT
for s=1 : 5.00000000000000
for s=0.01 : 5.00000000000000
for s=0.1 : 5.00000000000000
'''
l=sp.Symbol('l')
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
a=1000000000000
print(simpson(f,-a,a,1000000))
#print(sp.limit(simpson(f,-l,l,100)),l,sp.oo)
