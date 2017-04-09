#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 21:15:27 2017

@author: scott
"""


from numpy import linspace,ogrid,gradient,sqrt
from pylab import imshow,show,subplots,jet
from math import pi

x,y = ogrid[-0.5:0.5:100j,-0.5:0.5:100j]   #same as Q1
c=x+1j*y
P1=-0.05
P2=0.05
q1,q2=1,-1
e0=1
r1=abs(c-P1)
r2=abs(c-P2)
factor=4*pi*8.8854187817e-12
p=q1/(factor*r1)+q2/(factor*r2)
gy,gx=gradient(p)
dy,dx=-gy,-gx      #use numpy gradient to find partial dx,dy
m=sqrt(gy**2+gx**2)    #take the magnitude
fig, arrow = subplots()   #plot them on the same graph with arrows
xx=linspace(-0.5,0.5,100)
yy=linspace(-0.5,0.5,100)
arrow.streamplot(xx, yy, dx, dy,linewidth=1,color="w",density=3)
arrow.set(aspect=1,title='Electrical field')
imshow(m,origin="lower",extent=(-0.5,0.5,-0.5,0.5))
jet()         
show()
