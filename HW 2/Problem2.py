#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 20:35:07 2017

@author: scott
"""
from __future__ import division,print_function
from numpy import sqrt
import time
start_time = time.time()  #clock the start time
N=100           #define number of slices 
h = ((1-(-1))/N)   #calculate steps
A=0             #initialize Area
for n in range(N):
    x=-1+n*h
    y=sqrt(1-x**2)    #put the fuction in    
    A+=y*h            #acummulate each slice's value to find the area
print('Area Under the Curve =', A ,"for N =" ,N)   
print("--- %s seconds ---" % (time.time() - start_time)) #print the time
