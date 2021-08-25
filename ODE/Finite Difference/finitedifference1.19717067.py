"""
Smayan Gupta 
19/17067
Physics(H) 
Semester 4
Section-A
"""

import numpy as np
#defining function
def f(x):
    f=0.5*x**5 - 0.2*x**3 + 0.1*x - 0.2
    #print(f)
    return f
#forward method and derivative of a function
def derivative(x,h):
    value=(f(x+h)-f(x))/h
    print(value)
#double derivative of function
def dd(x,h):
    ddy=(f(x+h)-2*f(x)+f(x-h))/h*h
    print(ddy)
d1=0.09405
d2=-0.118
print("The analytical value of the first differentiation f' is ",d1)
print('''The analytical value of the second differentiation f" is ''',d2)
#values for h=0.1
print('Value of first and second derivative for h=0.1')
derivative(0.1,0.1)
dd(0.1,0.1)

#values of h=0.01
print('Value of first and second derivative for h=0.01')
derivative(0.1,0.01)
dd(0.1,0.01)

#values of h=0.001
print('Value of first and second derivative for h=0.001')
derivative(0.1,0.001)
dd(0.1,0.001)



