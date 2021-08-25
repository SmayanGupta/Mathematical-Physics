# -*- coding: utf-8 -*-
"""
Smayan Gupta 
19/17067
Physics(H) 
Semester 4
Section-A
"""
import numpy as np
import matplotlib.pyplot as plt

#creating our function
f = lambda x : 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
#step size
h = 0.1
#discretization of x axis over [-1,1]
x = np.linspace(-1,1)  

#derivatives using central difference
dfc = (f(x+h)-f(x-h))/(2*h)
ddf = (f(x+h)-2*f(x)+f(x-h))/ h**2
#plots
plt.plot(x,f(x),'g',x,dfc,'b',x,ddf,'r')
plt.legend(["f(x)","f'(x)",'f"(x)'])
plt.grid()


