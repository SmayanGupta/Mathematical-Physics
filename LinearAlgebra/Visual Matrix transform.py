# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 13:39:39 2021

@author: smaya
"""

from matplotlib import pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#assigning vairable to figure
fig = plt.figure()

#limit of axis
l=-8
axis = plt.axes(xlim =(-l,l),
				ylim =(-l, l))

# point one and two to draw lines form
p1=[-9,9]
p2=[0,0]

'''
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1,line2,
'''
#number of frames 
n=200

#function that creates a range of values between 
#initial identity matrix and final transformation matrix
#each of these individual values create 1 frame for animation
def newmat(A1):
    e=[1,0,0,1]
    Coef=[]
    for i in range(4):
        a1=np.linspace(e[i],A1[i],n)
        Coef.append(a1)
    return Coef
     

# function for making rotational matrix
def rot(angle):
    return [np.sin(angle),np.cos(angle)]

#angle to rotate matrix by
angle=np.pi/3

# function to create a graphic vector space
def vspace(i):
    vectorspace=[]
    for j in range(-10,10,2):
        p1=[-11,11]
        p2=[j,j]
        line1, = axis.plot(p1, p2, lw = 2,color='blue')
        line2, = axis.plot(p2, p1, lw = 2,color='black')
        #change array value below to obtain any transformation
        #[a,b,c,d]=[[a,b]
        #           [c,d]]
        Ai=newmat([3,1,0,2])
        #remove comment below to obtain only transformation matrix
        #transformed by the angle stated above
        Ai=newmat([rot(angle)[1],-rot(angle)[0],rot(angle)[0],rot(angle)[1]])
        A=np.array([[Ai[0][i],Ai[1][i]],[Ai[2][i],Ai[3][i]]])
        # Making two arrays X1 X2 for x and y axis and transforming them
        #using equation AX=B. plotting vectors from B to plot transformed axis.
        #line 1
        X1=np.array([p1,p2])
        B1=np.dot(A,X1)
        line1.set_data(B1[0,:],B1[1,:])
        vectorspace.append(line1)
        
        #line 2
        X2=np.array([p2,p1])
        B2=np.dot(A,X2)
        line2.set_data(B2[0,:],B2[1,:])
        vectorspace.append(line2)
    return vectorspace


#function iterated over to create a animation
#each return value here creates one frame
def update(i):
    '''
    '''
    final=vspace(i)
    return final



anim = FuncAnimation(fig, update, 
					frames = n, interval = 20, blit = True)





'''def points(i,j):
    angle=np.pi/3
    Ai=newmat([1,1,0,1])
    #Ai=newmat([rot(angle)[1],-rot(angle)[0],rot(angle)[0],rot(angle)[1]])
    #for j in range(-8,8,2):
    p1=[-9,9]
    p2=[j,j]
    A=np.array([[Ai[0][i],Ai[1][i]],[Ai[2][i],Ai[3][i]]])
    X1=np.array([p1,p2])
    B1=np.dot(A,X1)
    line1.set_data(B1[0,:],B1[1,:])
    X2=np.array([p2,p1])
    B2=np.dot(A,X2)
    line2.set_data(B2[0,:],B2[1,:])
    return line1,line2'''
