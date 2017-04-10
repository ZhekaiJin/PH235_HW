#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 17:05:52 2017

@author: scott
"""

from pylab import scatter,xlabel,ylabel,show,xlim,ylim
from numpy import linspace
def Operation(r,x,n):      #Define an function do the recursive operation n times
    i=0
    xPrime=0
    while i<n:
        xPrime=r*x*(1-x)
        x=xPrime
        i+=1
    return xPrime        

for r in linspace(1,4,301):     #start loop from 1 to 4 with step 0,01
    x1=Operation(r,0.5,1001)    #do the operation 10001 times first
    X=[x1]                      #store the 10001th result in a list
    R=[r]                       # correspond r with x 
    i=0
    while i<999:                                #run the rest 999 times and store values in lists
        X.append(Operation(r,X[len(X)-1],1))
        R.append(r)
        i+=1
    scatter(R,X)     #plot x with r for each r
xlabel("r")          #add specification 
ylabel("X(iteration)")
xlim(1,4)
ylim(0,1)
show()

#fix points looks like a single value of x corresponding to a single value of r
#limited cycle is like two or more values of x corresponding to a single r
#chaos is like huge adn random large numbers of x corresponding to a given r
#happend around 3.56
