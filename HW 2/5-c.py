#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:01:24 2017

@author: scott
"""
from __future__ import division,print_function
from numpy import loadtxt,sqrt,gradient
from math import sin,cos,pi
from pylab import imshow,gray,show

data=loadtxt("stm.txt",float)                  
dy,dx=gradient(data,2)  #2 increase gradient postion at the border 
I=(cos(pi/4)*dx+sin(pi/4)*dy)/sqrt(dx**2+dy**2+1)   #sub value in the reqired function 

imshow(I)
gray()
show()
