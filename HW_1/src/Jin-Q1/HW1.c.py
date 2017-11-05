#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:30:37 2017

@author: scott
"""

from __future__ import division,print_function
a1=15.67
a2=17.23
a3=0.75
a4=93.2
Z = int(input("Enter postive integer Z: "))
Bamax=-100.0     #B might be negative, thus Bamax inital should be set to be lower than the lowest possible Ba
while Z < 0 :
    print(" Z must be postive integer.")
    Z = int(input("Enter postive integer Z: "))
for A in range (Z,3*Z+1):
    if A%2==0: 
        if Z%2==0:
            a5=12.0
        else :
            a5=-12.0
    else:
        a5=0
    B=a1*A-a2*A**(2/3)-a3*Z**2/A**(1/3)-a4*(A-2*Z)**2/A+a5/A**(1/2)
    Ba=B/A
    if Ba > Bamax:      #record the newest Bamax and record A 
        Bamax=Ba
        Amax = A
print("the most stable binding enegry per nucleon is :",Bamax,"MeV where A is",Amax)