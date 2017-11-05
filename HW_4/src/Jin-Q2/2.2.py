#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:59:04 2017

@author: scott
"""
#from vpython import *
from __future__ import division,print_function  
from numpy import arange,gradient,array,vectorize,linspace
from math import floor,sin,pi,cos
from matplotlib.pyplot import plot,show,ylim,xlabel

l=0.4
g=9.81
m=1

def f(r,t):   #RK4 for 4 simutaneous equations
    theta1 = r[0]
    theta2 = r[1]
    omega1 = r[2]
    omega2 = r[3]
    ft1 = omega1
    ft2 = omega2
    fo1= -(omega1**2*sin(2*theta1-2*theta2)+2*omega2**2*sin(theta1-theta2)+g/l*(sin(theta1-2*theta2)+3*sin(theta1)))/(3-cos(2*theta1-2*theta2))
    fo2=(4*omega1**2*sin(theta1-theta2)+omega2**2*sin(2*theta1-2*theta2)+2*g/l*(sin(2*theta1-theta2)-sin(theta2)))/(3-cos(2*theta1-2*theta2))
    return array([ft1,ft2,fo1,fo2],float)
a = 0.0
b = 100.0
N = 100000
h = (b-a)/N
tpoints = arange(a,b,h)
theta1points = []
theta2points = []
omega1points = []
omega2points = []
points=[]
r = array([pi/2,pi/2,0,0],float)
for t in tpoints:
    theta1points.append(r[0])
    theta2points.append(r[1])
    omega1points.append(r[2])
    omega2points.append(r[3])
    #points.append(r)  # for animation
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

def T (omega1points,omega2points,theta1points,theta2points): #use the formula derived to compute E
    return m*l**2*(omega1points**2+0.5*omega2points**2+omega2points*omega1points*cos(theta1points-theta2points))
T= vectorize(T)  #allow elemenwise
def V(theta1points,theta2points):
    return -m*g*l*(2*cos(theta1points)+cos(theta2points))
V= vectorize(V)
E=T(omega1points,omega2points,theta1points,theta2points)+V(theta1points,theta2points)
plot(tpoints,E)
xlabel("t")
show()

