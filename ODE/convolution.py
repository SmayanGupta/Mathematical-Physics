# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:54:53 2021

@author: smaya
"""

import matplotlib.pyplot as plt
import numpy as np
from sympy import *


n=100
x=np.linspace(1/n,50,n)

def f1(t):
    return (cos(t))

def f2(t):
    return sin(t)
y=[f1(t) for t in x]
z=[f2(t) for t in x]
plt.grid(True)


t=Symbol('t')
u=Symbol('u')

print(integrate(f1(u-t)*f2(u),(u,0,t)))

con1=[]
def con(t):
    return t*sin(t)/2

for i in range(0,n):
    con1.append(con(x[i]))
    
plt.plot(x,y)
plt.plot(x,z)
plt.plot(x,con1)


