#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 02:34:36 2017

@author: scott
"""
from __future__ import division,print_function
from pylab import imshow,gray,show
from numpy import linspace,zeros
a=zeros((100,100))    #create a 100 by 100 matrix
d=-1                  #set iterator to 0 allow the calculation starts at a[0][0]
for x in linspace(-2,2,100):
    d+=1            #record iteration
    e=-1            #initialize x iterator
    for y in linspace(-2,2,100):
        e+=1
        c=x + 1j*y          #define the complex for every point in the matrix
        z=0
        for n in range(1000):
            z=z**2 + c      #iterate to determine if it is a point in the required set
        if abs(z)<2:
            a[d][e]=1       #give value 1 to points in the matrix
imshow(a.T,origin="lower")  #transpose to x-y form
gray()
show()
