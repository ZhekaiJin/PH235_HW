#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:28:31 2017

@author: scott
"""

#adpative trapezoidal rule

from __future__ import division,print_function
from math import sin, sqrt
def f(x):                     #define the function f
    return sin(sqrt(100*x))**2
def isOdd(x):          #define the function determine input is odd or not
    if x%2==1:
        return 1
    else:
        return 0
N1=1                            # find I1 with 1 slice and 1 step 
h1=1/N1
a,b,s=0,1,0
I1=h1*(0.5*(f(0.0)+f(1.0))+s)
print ("step_L","estimate      ","error")
print(h1,I1)                    #print out the stops and value
for n in range(1,1000):
    N=2**n                      #everytime slice is doubled 
    h=(b-a)/N
    s=0
    for n in range(1,N):        #odd the odd terms according to EQN 5.34
        if isOdd(n):
            s+=f(0+n*h)
        Ii=0.5*I1+h*s
    error=abs(Ii-I1)/3         #find the error of each iteration
    I1=Ii                      #replace I1 with Ii to start new iteration
    print(h,Ii,error)
    if error<1e-6:
        break                  #if the error threshold is reached, stop the iteration
print("final estimate=",Ii)