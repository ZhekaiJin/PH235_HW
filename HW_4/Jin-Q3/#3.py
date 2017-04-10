#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 17:07:25 2017

@author: scott
"""

from __future__ import division,print_function
from numpy import loadtxt,fft
from pylab import plot,show
from math import floor
data=loadtxt("dow.txt",float)  #load in the data
a=len(data)
L=range(a)
plot(L,data)                   # plot the data with proper x-axis
#show()
#2
c=fft.rfft(data)               #fft the data
#3
L2=len(c)
#[floor(0.1*L2):L2-1]=0       #only keep the first 10% of the data
c[floor(0.02*L2):L2-1]=0      #only keep the first 2% of the data
#4
z=fft.irfft(c)                 #inverse fft and plot
plot(L,z)
show()