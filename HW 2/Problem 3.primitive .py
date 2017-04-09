#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 14:15:28 2017

@author: scott
"""

from __future__ import division,print_function
from numpy import sin , sqrt
def factorial(a):                       #define factorial 
    result = 1
    for n in range(2, a + 1):
        result *= n
    return result  
def f(x):                               #define f(x)
    return sin(sqrt(100*x))**2
def fPrime(x):                          #use talyor expansion to find the fprime with error of O(x^6)
    return 5*(20 
            - 20**3*x/factorial(3)
            +  20**5*x**2/factorial(5)
            -20**7*x**3/factorial(7)
            + 20**9*x**4/factorial(9)
            - 20**11*x**5/factorial(11))
def err(h, a, b):
    return h**2*(fPrime(a)-fPrime(b))/12    #find the error
a,b,I=0,1,0                                 #input range of integration and inital integral
print ("iteration","steps","error")
for n in range(30):                         #iterate with different n till error is less
    N = 2**n
    h = (b-a)/N
    error = err(h, a, b) 
    print(n,"      ", h, "   ",error)       #record error and steps 
    if error < 1e-6:
        I = h*(f(a)/2 + f(b)/2) 
        for k in range(1,N):
            I += h*f(a+k*h) 
        break
print("fianl answer=",I)                    #print out final answer