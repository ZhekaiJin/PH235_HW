#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:45:12 2017

@author: scott
"""


from __future__ import division,print_function
a1=15.67
a2=17.23
a3=0.75
a4=93.2
Bamax1=0.0
Amax=0.0
for Z in range(1,101):
    Bamax=-100.0
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
        if Ba > Bamax:
            Bamax=Ba
            Amax = A
    if Bamax>Bamax1: # record the biggest Bamax and record what Z value it is 
        Bamax1=Bamax
        Zmax=Z
    print("the most stable value of A is :",Amax)
print("maximum binding energy occurs with Z of value :",Zmax)