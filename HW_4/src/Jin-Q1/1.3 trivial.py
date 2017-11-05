#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 01:55:30 2017

@author: scott
"""

from __future__ import division,print_function  
from numpy import arange,gradient,array,vectorize,linspace,sqrt
from math import floor,sin,pi,cos,inf
from matplotlib.pyplot import plot,show,ylim,xlabel,scatter
G=6.673e-11
M=1.989e30
T=0.1  # not defined
def f(r):
    x = r[0]
    y = r[1]
    q = r[2]
    w = r[3]
    fx = q
    fy = w
    r=sqrt(x**2+y**2)
    fq= -G*M*x/r**3
    fw= -G*M*y/r**3
    return array([fx,fy,fq,fw],float)
    
def RK4(r,h): 
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    return (k1+2*k2+2*k3+k4)/6+r

def Adaptive(r,h):
    r1=RK4(r,h)
    R1=RK4(r1,h)
    x1 = R1[0]
    y1 = R1[1]
    q1 = R1[2]
    w1 = R1[3]
    R2=RK4(r,2*h)
    x2 = R2[0]
    y2 = R2[1]
    deltax=(x1-x2)/30
    deltay=(y1-y2)/30
    pho=h*T/sqrt(deltax**2+deltay**2)
    return pho,x1,y1,q1,w1
         
a = 0.0
b = 16e8
h = 3e4
t=a
xpoints = []
ypoints = []
r = array([4e12,0.0,0.0,500],float)
while t<b:
    pho,x1,y1,q1,w1=Adaptive(r,h)     
    if pho >1:
        h=h*pho**(1/4)
        r=RK4(r,2*h)
    else :
        while pho<1:
            h=h*pho**(1/4)
            pho,x1,y1,q1,w1=Adaptive(r,h)
        r=[x1,y1,q1,w1]
    xpoints.append(x1)
    ypoints.append(y1)
    t+=2*h
plot(xpoints,ypoints)
show()
