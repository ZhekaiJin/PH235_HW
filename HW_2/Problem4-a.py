#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 22:29:02 2017

@author: scott
"""

from __future__ import division,print_function
from numpy import ogrid
from math import pi
from pylab import imshow,spectral,show
x,y=ogrid[-0.5:0.5:100j,-0.5:0.5:100j]  # create meshgrid with 100 by 100 points 
c=x+1j*y            #set its coordinate into complex domain 
P1=0.05             #set intial point of two charge 
P2=-0.05           
r1=abs(c-P1)       #magnitude of  
r2=abs(c-P2)       #magnitude of 
q1=1               #set two charges value
q2=-1
factor=8.8854187817e-12*pi*4    #set the coefficient in the denominator 
phi=q1/(factor*r1)+q2/(factor*r2)   #get the potential
imshow(phi,origin='lower',extent=[0,1,0,1])
spectral()        
show()


