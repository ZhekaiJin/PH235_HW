# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:58:30 2017

@author: scott
"""
from numpy import linspace,meshgrid,gradient,zeros,sqrt
from math import sin,pi
from pylab import imshow,jet,show,subplots
'''
    From problem a and b I have been using graph from - 0.5 to 0.5 but in this problem because my idea is to use Reiman' sum for the double integral,
    which means I have to add up all the functions calculated with coordinate other than the coordinates of that points ( in this case 999 points in total) to
    generate that points' potential" because I am doing the 100 times 100 grid by Question's requirement and it is rather easier to set my grid from - 50 to 50
    rather than -0.5 to 0.5. Thus my step for each iteration will just be 1 (h=1) and Integral+=h*y (simple ca1se in Question 2)will just be Integral+=h*f(f is my function)
    Also my function can't be using ogrid but mesh grid because I will have to have 2 dimensional array with indexes which I can use to add value of integration to.'''
 
miu=8.854187817e-12  
factor=4*pi*miu 
factor2=2*pi/10  #in the sigma function L=10      
N=100
x=linspace(-50,50,100)
y=linspace(-50,50,100)
xv,yv = meshgrid(x, y,sparse=False,indexing='ij')  #generate 2-d array with index which can be refered ti 
Grid=zeros([100,100])
def Function(x,y):     #define the function of charge density 
    return 100e4*sin(factor2*x)*sin(factor2*y)

def Phi(xx,yy):     #define Riemann's sum method which can be used to calculate potential at each point in the grid with h=1 from -50 to 50 
    p=0
    h=(50-(-50))/N
    for i in x:
        for j in y:
            if xx!=i and yy!=j:
                p+=h*Function(i,j)/(factor*sqrt((xx-i)**2+(yy-j)**2))
    return p


for m in range(10):    # use range since its start with 0 match the matrix index
    for n in range(10):
        Grid[m][n]=Phi(xv[m][m],yv[m][n])   #use the index generate by meshgrid to calculate the potential and give the value to the point in the grid
        print ("calculating at point=",m,n)  #since the calculation takes time ,this show the steps
        
gy,gx=gradient(Grid)   # do the same thing in question 2 to find out gradient
dy,dx=-gy,-gx         # use grardient method to find gradient 
m=sqrt(dy**2+dx**2)  #find the magnitude like question 2 and use same method to give a arrow drawing 
fig, arrow = subplots()
arrow.streamplot(x, y, dx, dy,linewidth=1,color="w",density=3)
arrow.set(aspect=1,title='Electrical field')
imshow(m,origin="lower",extent=(-50,50,-50,50))
jet()         
show()

