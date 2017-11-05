from vpython import *
from math import sqrt,sin,cos,pi
from numpy import arange,array,zeros
from pylab import plot,xlabel,ylabel,show,figure,scatter
l=0.4 
g=9.8 
a=0
b=100
m=1
 
def f(r,t):
    theta1 = r[0]
    theta2 = r[1]
    omega1 = r[2]
    omega2 = r[3]
    ft1 = omega1
    ft2 = omega2
    fo1= -(omega1**2*sin(2*theta1-2*theta2)+2*omega2**2*sin(theta1-theta2)+g/l*(sin(theta1-2*theta2)+3*sin(theta1)))/(3-cos(2*theta1-2*theta2))
    fo2=(4*omega1**2*sin(theta1-theta2)+omega2**2*sin(2*theta1-2*theta2)+2*g/l*(sin(2*theta1-theta2)-sin(theta2)))/(3-cos(2*theta1-2*theta2))
    return array([ft1,ft2,fo1,fo2],float)

def RK4(a,b,N):
    h = (a-b)/N
    T = arange(a,b,h)
    points = []
    r=array([0.0,0.0,pi/2,pi/2])
    for t in T:
        points.append(r) #animation part
        k1 = h*f(r,t)
        k2 = h*f(r+0.5*k1,t+0.5*h)
        k3 = h*f(r+0.5*k2,t+0.5*h)
        k4 = h*f(r+k3,t+h)
        sum=(k1+2*k2+2*k3+k4)/6
        r =r + sum
    return points
#above is just part 2 but with every r in every time step to a whole list
 
#animation
p=RK4(a,b,100000)  #get r's list and set the initial condition
stick1=cylinder(pos=vector(0,0,0),axis=vector(l,0,0), radius=0.01)
stick2=cylinder(pos=vector(l,0,0),axis=vector(l,0,0), radius=0.01)
ball1=sphere(pos=vector(l,0,0),radius=0.05,color=color.white)
ball2=sphere(pos=vector(2*l,0,0),radius=0.05,color=color.white)

#make the parts moving
for i in range(len(p)):
    rate(450)
    a=p[i]
    theta1=a[0]
    theta2=a[1]
    x1=l*sin(theta1)
    y1=-l*cos(theta1)
    x2=x1+l*sin(theta2)
    y2=y1-l*cos(theta2)
    ball1.pos=vector(x1,y1,0)
    ball2.pos=vector(x2,y2,0)
    stick1.axis=vector(x1,y1,0)
    stick2.pos=vector(x1,y1,0)
    stick2.axis=vector(x2-x1,y2-y1,0)