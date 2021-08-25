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
#creating function
f = lambda x : 0.1*x**5 - 0.2*x**3 + 0.1*x - 0.2
#derivative of function
df = lambda x: 0.5*x**4 - 0.6*x**2 + 0.1  
#stepsize  
h=0.01
#descritization of x axis over [-1,1]
x = np.linspace(-1,1) 
#theoretical plot 
plt.plot(x,df(x),'-k')

#Forward differences approximation
dff =(f(x+h)-f(x))/h    
plt.plot(x,dff,'-b')

#Backward differences approximation
dfb = (f(x)-f(x-h))/h
plt.plot(x,dfb,'-g')

#Central difference approximation
dfc = (f(x+h)-f(x-h))/(2*h)
plt.plot(x,dfc,'-r')
#plot
plt.legend(["Theoretical","Forward",'Backward',"Central"])
plt.grid()

'''OUTPUT:The analytical value of the first 
differentiation f' is  0.09405
The analytical value of the second 
differentiation f" is  -0.
'''
