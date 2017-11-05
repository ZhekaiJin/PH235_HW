#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 4:34:14 2017

@author: scott
"""


from math import cos,exp,pi
from numpy import linspace,arange,random
from matplotlib.pyplot import plot,show
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x0=2
Tmin=1e-3
Tmax=10.0
tau=1e4
def f(x):
	return x**2-cos(4*pi*x)     #test case 1
	#return cos(x)+cos(2**(0.5)*x)+cos(3**(0.5)*x)    #test case 2
	
X=arange(-50,50,0.001)
#  X=arange(0,50,0.001)  # for test case 2
Y=[]
for i in X:
	Y.append(f(i))
U=[]
u=0
t=0
XF=[]
x=x0
T=Tmax
R=[]
while T>Tmin:

	t+=1           #exp cooling schudule from salesman
	T =Tmax*exp(-t/tau)
	xnew = random.normal(x,1)    #use  gaussian distribution with x as mean and s.d 1
	BOOL=False
	del_E= f(xnew)-f(x)    #define the difference in energy foe anneal
	if del_E < 0: #and xnew <50 and xnew > 0: (for test case 2)
		BOOL=True     #acceptance condition
	else:
		if random.random()<exp(-del_E/T): # and xnew <50 and xnew > 0: (for test case 2)
			BOOL=True     
	if BOOL==True:
		x=xnew       #accept the new x and put them in to list with iteration numbers
		u+=1
		U.append(u)
		XF.append(x)
		R.append([u,x])
plot(X,Y)
show()
plot(XF,U,".")
show()

'''
def Calculation(i):
   return R[i]
       
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-1.5, 1.5), ylim=(-1.5, 1.5))

ax.grid()
line, = ax.plot([], 'o-', lw=0.5)

def init():
    """initialize animation"""
    line.set_data([])
    return line


def animate(i):
    """perform animation step"""
    global c
    c+=1
    x=Calculation(c);
    line.set_data(x)
    return line

ani = animation.FuncAnimation(fig, animate, frames=300, interval=1, blit=True, init_func=init)
plt.show()
''' 
#animation part work on vpython 
