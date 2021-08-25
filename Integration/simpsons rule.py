'''
Smayan Gupta
19/17067
Section-A
Semester 4
Bsc Physics Hons
'''
import math
#a=initial point
#b=final point

def func(x):
    return 1/(1+x)#x**(1/2)

#Simpsons 1/3 rule function

def simpson(function,a,b,n):
    h=(b-a)/n #step size
    i=a
    sum=0
    counter=0
    while i<=b:
        if(i==a):
            sum+= function(a)
        elif(i==b):
            sum+= function(b)
            break
        elif(counter%2!=0):
            sum+= 4*function(i)
        elif(counter%2==0):
            sum+= 2*function(i)
        counter+=1
        i+=h
    return sum*h/3 
        
#print(simpson(0,8,1000))

print(simpson(func,0,1,100))  #answer value for simpson 1/3 rule
#output: 0.6914805142057002

#simpson 3/8 rule function
def simpson_38(func,a,b,n):
    i=a
    sum38=0
    counter=0
    h=(b-a)/n
    while i<=b:
        if  i==a:
            sum38+=func(a)
        elif  i==b:
            sum38+=func(b)
        elif(counter%3==0):
            sum38+=2*func(i)
        else:
            sum38+=3*func(i)
        
        i+=h
        counter+=1
    return sum38*3*h/8

print(simpson_38(func,0,1,100)) #answer value for simpson 3/8rule
#output:0.6900190615487781
            
        

#trapezoidal rule function
def trap(a,b,n):
    h=(b-a)/n
    sum=0
    while a<=b:
        sum+= (func(a)+func(a+h))*h/2
        a+=h
    print(sum)
    return sum
        
trap(0,1,100) #answer value for trapezoidal rule
#output: 0.6931534304818242

print(math.log(2)) #exact solution
#output:0.6931471805599453
# trapezoidal rule gives most accurate while simpson 3/8 gives least accurate
























