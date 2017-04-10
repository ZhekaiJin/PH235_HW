#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 23:53:23 2017

@author: scott
"""

from __future__ import division,print_function  
from numpy import arange,array,sqrt
from matplotlib.pyplot import plot,show
import time 
start_time = time.time()  #clock the start time
G=6.673e-11  #setting up the constants 
M=1.989e30

def f(r):     #setting up the function iterate in RungeKutta 
    x = r[0]    #since non of the function is related to t the operand t can be ignored 
    y = r[1]
    q = r[2]
    w = r[3]
    fx = q
    fy = w
    r=sqrt(x**2+y**2)
    fq= -G*M*x/r**3
    fw= -G*M*y/r**3
    return array([fx,fy,fq,fw],float)

a = 0.0     #setting up the t array to simulate the change
b = 3e9
h = 1e3
tpoints = arange(a,b,h)
xpoints,ypoints=[],[]      #create two empty list to record x,y postion at every t 
r = array([4e12,0.0,0.0,500],float)
for t in tpoints:          # do the Runge Kutta
    xpoints.append(r[0])   # append the postion of x and y into the list
    ypoints.append(r[1])
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1+2*k2+2*k3+k4)/6
plot(xpoints,ypoints)       # Plot the trajectory should be an ecclpise
show()
print("--- %s seconds ---" % (time.time() - start_time)) #print the time
