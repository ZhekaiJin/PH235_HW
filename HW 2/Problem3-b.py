#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 19:32:25 2017

@author: scott
"""
#Romberg method

from __future__ import division,print_function   #same as 3.a
from math import sin, sqrt
from numpy import empty
def f(x):
	y=(sin(sqrt(100*x)))**2
	return y
def isOdd(x):           #
    if x%2==1:
        return 1
    else:
        return 0
def main():
    n=10 
    N=1
    h1=1/N
    a,b,s=0,1,0
    I1=h1*(0.5*(f(a)+f(b))+s)
    z=empty((n,n))       #create a n by n matrix
    for i in range(n):
        N=2**(i+1)    #N=2*N
        h=1/N
        s=0
        z[i][0]=I1
        for k in range(1,N):
            if isOdd(k):
                s+=f(0+k*h)
        Ii=0.5*I1+h*s
        I1=Ii       
        if i==0:                    #printout the first row
            print(z[0][0])         
        for m in range(1,i+1):      #find value from last column same row and last column last row
            z[i][m]=z[i][m-1]+(z[i][m-1]-z[i-1][m-1])/(4**m-1)  
            error=abs((z[i][m-1]-z[i-1][m-1])/(4**m-1))     #find the error
            if m == i:                      #printout the corresponding row 
                print (z[i][0:m+1])
            if error<1e-6:              #when error reached the threshold , print last row and print the final estimate
                print(z[i][0:m+1])      
                print("final anwer=",z[i][m],"row number=",i+1,"cloumn number=",m+1)   
                return z   #terminate funtion (avoid double break)
main()   #run the main


          