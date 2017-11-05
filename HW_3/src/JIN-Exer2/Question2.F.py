#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 13:28:27 2017

@author: scott
"""

G=6.674e-11   #set up the constant
M=5.974e24
m=7.348e22
R=3.844e8
w=2.662e-6
h=1e-6
 
def function(r):    #define the function
    y=G*M/r**2-G*m/(R-r)**2-w**2*r
    return y

def Prime(r):      #define the gradient
    xPrime=(function(r+h/2)-function(r-h/2))/h
    return xPrime

def Improve(x):   #define how get the next x
    xNext=x-function(x)/Prime(x)
    return xNext

def L_point(r):   #compute Lagrange point until target accuracy
    for i in range(100):
        if abs(function(r)/Prime(r))<1e-4:
            print("iteration number=",i+1)
            print("final value=",r,"m")
            break;
        r=Improve(r)

L_point(1e7)
    



    