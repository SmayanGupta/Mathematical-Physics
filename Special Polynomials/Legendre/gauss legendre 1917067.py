# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 10:01:47 2021
@author: Smayan GUpta
19/17067
Seection-A
Semester-4
Bsc Physics Hons
"""
import sympy as sp
import random
#defining a recursive function for legendre polynomials
def legendre(n,x):
    
    if n==0:
        return x*0+1
    elif n==1:
        return x
    else: 
        return ((2*n-1)*x*legendre(n-1, x) -(n-1)*legendre(n-2, x))/n
#defining a function for gauss legendre    
def gausslegendre(f,n):
     # making a symbol x
    x=sp.Symbol('x')
     #all roots of the given legendre polynomial
    r=sp.Poly(legendre(n,x)).nroots()
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
        w[j]=sp.integrate(l,(y,-1,1)) #weights after integrating
    integral=0
    for i in range(0,len(r)):
        integral+=w[i]*f(r[i]) #summing the weights with function value at roots
    print(integral)
    
#print(w)
#creating random integers for mth and nth order legendre polynomials
m=random.randint(0,10)
n=random.randint(0,10)
'''this helps us in giving random integers to test value for legendre polynomials
 orthogonality.For every time we run this program we will get different values 
 of m and n and check their orthognality'''
#remove comment to check condition where m=n 
#m=n 
print('order of first legendre polynomial',m)
print('order of second legendre polynomial',n)
#print(m)
#function to integrate
def f(x):
    return legendre(m,x)*legendre(n, x)

gausslegendre(f,10)

''' OUTPUT
for m not equal to n:
order of first legendre polynomial 0
order of second legendre polynomial 5
-2.04697370165263e-15
for m=n=2:
order of first legendre polynomial 2
order of second legendre polynomial 2
0.399999999999992
which is nearly equal to 4

    
'''
    
        
        
        