'''
Smayan Gupta
19/17067
Section-A
Semester 4
Bsc Physics Hons
'''
import math

def f(x):
    return 1/(1+x)
def trap(a,b,n):
    h=(b-a)/n
    sum=0
    while a<=b:
        sum+= (f(a)+f(a+h))*h/2
        a+=h
    print(sum)
    return sum
        
trap(0,1,100)
print(math.log(2))
