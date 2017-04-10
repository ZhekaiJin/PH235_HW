#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:45:13 2017

@author: scott
"""

from __future__ import division,print_function
a1=15.67                                      #declare constant 
a2=17.23
a3=0.75
a4=93.2
A = int(input("Enter postive integer A: "))    #ask the user to input A and Z
Z = int(input("Enter postive integer Z: "))
while A < 0 or Z < 0 :                         # in case its not postive
    print("A and Z must be postive integer.")
    A = int(input("Enter postive integer A: "))
    Z = int(input("Enter postive integer Z: "))    
if A%2==0:                #set a5 with A and Z values
    if Z%2==0:
        a5=12.0
    else :
        a5=-12.0
else:
    a5=0
B=a1*A-a2*A**(2/3)-a3*Z**2/A**(1/3)-a4*(A-2*Z)**2/A+a5/A**(1/2)  #Compute B
print("the binding enegry is :",B,"MeV")
        
        
        
        
