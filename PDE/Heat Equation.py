# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:48:48 2021

@author: smaya
"""
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#Partial differential equation
c=10
rho=10
k=1
alpha=1.2
global p
p=np.pi
tf=20
ti=0
xf=1
xi=0
n=10
def f(x):
    return  np.sin(p*x)
x=np.linspace(xi,xf,n)
t=np.linspace(ti,tf,n)
dx=(xf-xi)/n
dt=(tf-ti)/n
r=(k*dt)/(c*rho*dx**2)
#r=alpha**2*dt/dx**2
print(r)
u=np.zeros((n,n))
#print(u)
for i in range(1,n-1):
    u[0][i]= f(x[i])

#print(u)
for j in range(1,n):
    for i in range(1,n-1):
        u[j][i]=(1-2*r)*u[j-1][i]+ r*(u[j-1][i+1]+u[j-1][i-1])

#print(u)
hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')

X, Y = np.meshgrid(x, t)  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, u,)




'''
plt.style.use('seaborn-pastel')
fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    x = np.linspace(0, 4, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,frames=200, interval=1, blit=True)
plt.show()'''
