#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 14:26:37 2017

@author: scott
"""

from numpy import array,sqrt
from pylab import plot,show,scatter
import time 
start_time = time.time()  #clock the start time
G=6.67408e-11 
M=1.989e30   
T=0.1 

def f(r):
    x,y,q,w = r[0],r[1],r[2],r[3]
    fx = q
    fy = w
    r=sqrt(x**2+y**2)
    fq= -G*M*x/r**3
    fw= -G*M*y/r**3
    return array([fx,fy,fq,fw],float)
   
def RK4(r,h):   #define Rk4
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    return r+(k1+2*k2+2*k3+k4)/6

def Adaptive(r,h):   #define how to fine the pho with return the first approxmiation
    r1=RK4(r,h)
    R1=RK4(r1,h)
    R2=RK4(r,2*h)
    deltax=(R1[0]-R2[0])/30  #x1=R1[0],x2=R2[0],y1=R1[1],y2=R2[1]
    deltay=(R1[1]-R2[1])/30
    pho=h*T/sqrt(deltax**2+deltay**2)
    return pho,R1
t,b=0,15e8
h=5e5
x,y=[],[]
r=array([4e12,0.0,0.0,500.0])
while t<b:                          #iterate with t and keep lower the step if pho>1
    pho,R1=Adaptive(r,h)
    if pho>1:
        x.append(R1[0])
        y.append(R1[1])
        t+=2*h
        r=R1
    h=h*pho**(1/4)    
#plot(x,y)    #use for 2.3    
scatter(x,y)
show()
print("--- %s seconds ---" % (time.time() - start_time)) #print the time