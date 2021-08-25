# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:23:02 2021

@author: Smayan GUpta
19/17067
Seection-A
Semester-4
Bsc Physics Hons
"""
import numpy as np
import math

'''Question : Evaluate the integral of function 2*x/1+x**4 
in limits (1,2) using Gauss one point,two point and three point rules
Compare with the exact solution.
'''


'''since given integral is not in standard limits we substitute
x = ((b-a)*t+a+b)/2  where a = 1 and b = 2 
after which the function becomes 8*(t+3)/(16+(3+t)**4)'''



#Defining the function to be integrated
def f(t):
    return 8*(t+3)/(16+(t+3)**4)

exact = math.atan(4) - math.pi/4
print("Exact value of integral is ",exact)

#defining function to calculate error
def error(i):
    return abs((i-exact)/exact)*100
    
#GAUSS ONE POINT FORMULA
print("Gauss one point formula ")
w1 = 2

onepoint = 2*f(0)

print("Value of integral using the gauss one point formula is ",onepoint)

print("Perentage error for Gauss one point formula is ",error(onepoint))

print('''
      ''')

#GAUSS TWO POINT FORMULA
print("Gauss 2 point formulae ")

#making an array of weights
w2=[1]*2
#making array of roots
roots2=[1/np.sqrt(3),-1/np.sqrt(3)]
twopoint=0
for i in range(0,2):
    twopoint+= w2[i]*f(roots2[i])
    
print("Value of integral using the gauss two point formula is ",twopoint)

print("Percentage error in Gauss two point formula is ",error(twopoint))

print('''
      ''')
      
#GAUSS 3 POINT FORMULA

print("Gauss 3 point formulae ")

#declaring array of weights
w3=[5/9,8/9,5/9]
#declaring array of roots
roots3=[np.sqrt(3/5),0,-1*np.sqrt(3/5)]

threepoint=0
for i in range(0,3):
    threepoint+=w3[i]*f(roots3[i])


    
print("Value of integral using gauss three point formula is ",threepoint)

print("Percentage error in Gauss three point formula is",error(threepoint))


