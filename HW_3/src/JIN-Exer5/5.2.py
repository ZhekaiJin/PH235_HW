#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:32:04 2017

@author: scott
"""

from numpy import arange
from pylab import plot,xlabel,ylabel,show,figure
    
h=0.01

def fx(x,y):    #define function for x
   return 10*(y-x)
   
def fy(x,y,z):     #define function for y
   return 28*x-y-x*z

def fz(x,y,z):      #define function for z
   return x*y-(8/3)*z
    
X=[]
Y=[]
Z=[]
x,y,z=0.0,1.0,0.0    #create three lists for x,y,z and set inital values
T=arange(0,50,h)
for t in T:
    X.append(x)    #do the same with x with fx (only x change)
    Fx1=h*fx(x,y)
    Fx2=h*fx(x+Fx1/2,y)
    Fx3=h*fx(x+Fx2/2,y)
    Fx4=h*fx(x+Fx3,y)
    dx=(Fx1+2*Fx2+2*Fx3+Fx4)/6
    x+=dx
    
    Y.append(y)    #do the same with y with fy(only y change)
    Fy1=h*fy(x,y,z)
    Fy2=h*fy(x,y+Fy1/2,z)
    Fy3=h*fy(x,y+Fy2/2,z)
    Fy4=h*fy(x,y+Fy3,z)
    dy=(Fy1+2*Fy2+2*Fy3+Fy4)/6
    y+=dy
    
    Z.append(z)    #do the same with z with fz(only z change)
    Fz1=h*fz(x,y,z)
    Fz2=h*fz(x,y,z+Fz1/2)
    Fz3=h*fz(x,y,z+Fz2/2)
    Fz4=h*fz(x,y,z+Fz3/2)
    dz=(Fz1+2*Fz2+2*Fz3+Fz4)/6
    z+=dz
    
figure(num=1);    #create two figures 
plot(T,Y)
xlabel('t')
ylabel('y')
figure(num=2)
plot(X,Y)
xlabel('x')
ylabel('y')
show()
    
  


