from vpython import *
from math import cos,sin,pi
from numpy import arange,empty

c1=1000        #input scaling constant
c2=50
Sun=sphere(pos=vector(0,0,0),radius=20,color=color.magenta)   #input radius ,orbit, period and color
sunR=695500
radiusin=[2440,6052,6371,3386,69173,57316]
radiusout=[x/sunR*c1 for x in radiusin]
orbit=[57.9,108.2,149.6,227.6,778.5,1433.4]
T=[88.0,224.7,365.3,687.0,4331.6,10759.2]
C=[color.blue,color.red,color.yellow,color.orange,color.white,color.cyan]
b=empty(6,sphere)                                               #creat a array of sphere
for n in range(6):                  #set up each sphere
    b[n]=sphere()
    b[n].pos=vector(orbit[n],0,0)
    b[n].color=C[n]
    b[n].radius=radiusout[n]
for t in arange(0,100*pi,0.1):     #the animation part
    rate(30)
    for n in range(6):
        w=2*pi*c2/T[n]
        x = orbit[n]*cos(w*t)
        y = orbit[n]*sin(w*t)
        b[n].pos = vector(x,y,0)