#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:24:55 2017

@author: scott
"""

from numpy import arange,array
from pylab import plot,xlabel,ylabel,show,figure

def f(A):         #create a array as operand of RK4 as [x,y,z] for each iteration
    x,y,z=A[0],A[1],A[2]
    fx=10*(y-x)
    fy=28*x-y-x*z
    fz=x*y-(8/3)*z
    return array([fx,fy,fz]) #turn into array to allow elementwise operation    
h = 0.001    #iteration step for RK4
T = arange(0,50,h)  #reqiure time step
A =[]  #creat a list of array
r=array([0.0,1.0,0.0])
for t in T:
    A.append(r)
    k1 = h*f(r)      #RK4 with x y z increment together  as a array
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    dA=(k1+2*k2+2*k3+k4)/6   
    r= r+ dA             #increment r(the array) for the it to be append on the list for next iteration
X=[]
Y=[]
Z=[]
for i in range(len(A)):     #take out each array in the list  and assign it to new X,Y,Z
    xyz=A[i]
    X.append(xyz[0])
    Y.append(xyz[1])
    Z.append(xyz[2])
figure(num=1);    #create two figures 
plot(T,Y)     #Y with T
xlabel('t')
ylabel('y')
figure(num=2);   #Y with X
plot(X,Y)
xlabel('x')
ylabel('y')
show()
