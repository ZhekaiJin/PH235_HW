#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:36:08 2017

@author: scott
"""

from __future__ import division,print_function   
from math import pi,sqrt
from numpy import empty,e
from matplotlib.pyplot import plot, show
h=6.62607004e-34        #set up the constant
c=299792458
F1=390e-9
F2=750e-9 
def f(x):       #define the integration function
	y=(15/pi**4)*x**3/(e**x-1)
	return y
def isOdd(x):           #define function determine whether odd/even
    if x%2==1:
        return 1
    else:
        return 0
def Romberg(T):     #use HW2.3's Romberg method but change it into a function of T
    n=10 
    N=1
    k=1.38064852e-23
    LB=h*c/(F2*k*T)
    UB=h*c/(F1*k*T)
    h1=(UB-LB)/N
    a,b,s=LB,UB,0
    I1=h1*(0.5*(f(a)+f(b))+s)
    z=empty((n,n))       #create a n by n matrix
    for i in range(n):
        N=2**(i+1)
        h2=1/N
        s=0
        z[i][0]=I1
        for k in range(1,N):
            if isOdd(k):
                s+=f(0+k*h2)
        Ii=0.5*I1+h2*s
        I1=Ii       
        for m in range(1,i+1):      #find value from last column same row and last column last row
            z[i][m]=z[i][m-1]+(z[i][m-1]-z[i-1][m-1])/(4**m-1)
    return z[9][9]   #terminate funtion (avoid double break)  and cancel the limiting factor to assure its a smooth curve
F=[]
Temp=[]
for T in range(300,10001):    #create two corresponding list one of T and one of Integration of T
    F.append(Romberg(T))
    Temp.append(T)
plot(Temp,F)      #plot the graph
show()

#2
def goldensearch(a,b):        #use golden serach method
    gr = (sqrt(5) + 1) / 2    #compute the golden ratio 
    c = b-(b-a)/gr
    d = a+(b-a)/gr            #get two intermediate points c, d
    while abs(c-d)>1e-4:      #compute till c and d is very close
        if Romberg(c)>Romberg(d):
            b=d               #shorten the search range
        else:
            a=c
    
        c= b-(b-a)/gr
        d= a+(b-a)/gr
    return(b+a)/2            #give the approximate value
print("Maximumvalue happend at",goldensearch(4000,7000),"with efficency=",Romberg(goldensearch(4000,7000)))
    