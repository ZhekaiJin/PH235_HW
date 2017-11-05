#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 20:35:07 2017

@author: scott
"""
from __future__ import division,print_function
from numpy import eye,zeros,matmul,ones,copy
from scipy import linalg

# Question 1 

N=10000  #set the size of A
V=5
A=eye(N) #create identity matrix with main diagonal as 1
B=eye(N,k=1) #create identity matrix with up 1 diagonal as 1
C=eye(N,k=2) #create identity matrix with up 2 diagonal as 1
D=eye(N,k=-1)#create identity matrix with down 1 diagonal as 1
E=eye(N,k=-2)#create identity matrix with down 2 diagonal as 1
F=4*A-(B+C+D+E)
F[0,0]=3
F[N-1,N-1]=3
W=zeros([N,1])
W[0,0],W[1,0]=V,V
print(F)  # F is the required A
print(W)  # W is the RHS of the equation

# Question 2

Ai = linalg.inv(F)   #use LinearAlgebra package ti find the inverse
v =matmul(Ai,W)      #then do the vector multiplication
print(v)             #get v

#Question 3
up=2              #change the matrix A to Aa as requred for banded 
down=2
M=up+down+1
Aa=-1*ones([M,N])     #set all of them to -1 since they are dontcares annd -1 except the middle row
Aa[up,:]=4              #set the middle row
Aa[up,0]=3
Aa[up,N-1]=3
print(Aa)

def banded(Aa,va,up,down):    #get from moodle

    # Copy the inputs and determine the size of the system
    A = copy(Aa)
    v = copy(va)
    N = len(v)

    # Gaussian elimination
    for m in range(N):

        # Normalization factor
        div = A[up,m]

        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]

        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]

    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]

    return v
print("finalasnwer is")
print(banded(Aa,W,2,2))   #use banded to find the solution