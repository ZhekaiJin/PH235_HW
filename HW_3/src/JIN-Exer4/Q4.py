#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 16:07:59 2017

@author: scott
"""


from __future__ import division,print_function  
from numpy import arange 
from math import floor
from matplotlib.pyplot import plot,show,ylim
#define Vin first
def isOdd(x):           #is Odd from question 3
    if x%2==1:
        return 1
    else:
        return 0
def x(t):     #   define Vin as x
    if isOdd(floor(2*t))==0:
        return 1
    else:
        return -1
        
def f(t,y):  #define the dy/dt
    #RC=1
    #RC=0.1
    RC=0.01
    return(x(t)-y)/RC
h=0.01   #declare steps (this proved to generate a resonable gragh with good timing )
def RK4(t,y):    #use RK4
    F1=h*f(t,y)
    F2=h*f(t+h/2,y+F1/2)
    F3=h*f(t+h/2,y+F2/2)
    F4=h*f(t+h,y+F3)
    dy=(F1+2*F2+2*F3+F4)/6
    return dy
tpoints = arange(0,10,h)
ypoints=[]         
y=0.0
for t in tpoints:    #get the y(t+h) for each t
    ypoints.append(y)
    y+=RK4(t,y)
    
plot(tpoints,ypoints)   #plot the two lists
ylim(-2,2)     #set limit to make graph readable
show()

