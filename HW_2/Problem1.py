#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:09:32 2017

@author: scott
"""

from __future__ import division,print_function
from pylab import imshow,gray,show
from numpy import ogrid
x,y=ogrid[-2:2:100j,-2:2:100j] #creat a 100 by 100 grid from -2 to 2 respectively on x and y axis
c=x + 1j*y #use x value and y value to form a complex number
z=0        #set inital z to 0
for n in range(1000):  #iterate 1000times to determine a new z with every c
    z=z**2 + c
a=abs(z)< 2             #get rid of the non-Manderlbrot set points
imshow(a.T,origin="lower")  #take the transpose and get the famous pattern
gray()
show()