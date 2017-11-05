#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:37:31 2017

@author: scott
"""
from __future__ import division,print_function  
from numpy import linspace,meshgrid,gradient,sqrt,arange,exp
from pylab import imshow,show,subplots,jet,spectral,contourf,figure,colorbar
from math import pi
from random import random

z=random()
X=[]
Sum=0
for i in arange(0,1000000,1):
   
    z=random()
    X.append(z)
    Sum+=1/(exp(z**2)+1)  #feed in the random to enforce nonlinear random and calculate the approximation 
    
print("the approximation for the integral would be", 2*Sum/1000000)
