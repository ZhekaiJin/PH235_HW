#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 11:35:43 2017

@author: scott
"""
from math import sin,pi
from numpy import empty,array,arange
from pylab import plot,show

a=1
b=3
x0=0
y0=0
t=0
A = 0.0
B = 20.0
N = 1          # Number of "big steps"
H = (b-a)/N  
#print("H=",H) 
   # Size of "big steps"
delta = 1e-10     # Required position accuracy per unit time
def f(r):
    x = r[0]
    y = r[1]
    fx = 1-(b+1)*x+a*x**2*y
    fy = b*x-a*x**2*y
    return array([fx,fy],float)

tpoints = []
xpoints = []
ypoints = []
r = array([x0,y0],float)

def step(r,t,H):
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)
    R1 = empty([1,2],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))
    error = 2*H*delta
    while error>H*delta:
        if n>8:                 #break from the loop if n is greater then 8
            return [r,0]
        n += 1
        h = H/n
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)
        R2 = R1
        R1 = empty([n,2],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
            R1[m] = R1[m-1] + epsilon
        error = abs(epsilon[0])
    r = R1[n-1]
    return [r,1]

while t<20:
    v=step(r,t,H)
    h=H
    while v[1]==0:#check if n is bigger then 8 
        h=h/2 
        v=step(v[0],t+h,h)
        #print (h)
    A=v[0]
    xpoints.append(A[0])
    ypoints.append(A[1])
    tpoints.append(t)
    t+=h
        
# Plot the results
#print (tpoints)
plot(tpoints,xpoints)
plot(tpoints,ypoints)
show()
