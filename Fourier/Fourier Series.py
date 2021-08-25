# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 11:42:54 2021

@author: smaya
"""
'''
Smayan GUpta
19/17067
Section A
Semester 4
'''
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def f(c,i,x):
    if (i==0) and (c==0):
        return x*(2-x)
    if c==1:
        return f(0,0,x)*sp.cos((i*np.pi*x)/l)
    if c==2:
        return f(0,0,x)*sp.sin((i*np.pi*x)/l)

#limits
l=2
    
n=5
x=sp.Symbol('x')
a0= (1/l)*sp.integrate(f(0,0,x),(x,-l,l))
#print(a0)
a=[]
b=[]
#sum=a0
for i in range(1,n):
        an=(1/l)*sp.integrate(f(1,i,x),(x,-l,l)).evalf()
        a.append(an)
        bn=(1/l)*sp.integrate(f(2,i,x),(x,-l,l)).evalf()
        b.append(bn)
        #sum+=an*sp.cos((i*np.pi*x)/l) + bn*sp.sin((i*np.pi*x)/l)
def sum(x):
    sum1=a0
    for i in range(1,n):
        sum1+=a[i-1]*sp.cos((i*np.pi*x)/l) + b[i-1]*sp.sin((i*np.pi*x)/l)
    return sum1
#print(sum(x))
#print(a)
#print(b)

X=np.linspace(-2,2,100)
plt.plot(X,f(0,0,X),label="Function")
f=[]
for i in X:
    f.append(sum(i))
    
plt.plot(X,f,label="for n= "+str(n))
plt.legend()
plt.show()
