#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 18:58:56 2017

@author: scott
"""
from __future__ import division,print_function
from math import sqrt
r = [2]    # create a prime number list
for n in range(3,10001):
    isPrime = True     #create boolean structure to avoid repetition
    for x in r:
        if x > int(sqrt(n)):     #get rid of number bigger than sqrt(n) 
            break                #int to avoid error
        if n%x ==0:         #get rid of numbers that can be divided by prime numbers 
            isPrime=False
    if isPrime==True:      #confirm the prime number and add to the list
        r.append(n)

print(r)