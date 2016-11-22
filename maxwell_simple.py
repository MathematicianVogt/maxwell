from pde import *
import math
import numpy as np
import pylab as plt
import time
import scipy

def set_initial_condition(func,x,y,solList):
	lx=len(x)
	ly=len(y)
	IC=np.zeros((lx,ly))
	for i in range(0,ly):
		for j in range(0,lx):
			IC[i,j]=func(x[j],y[i])

	solList.append(IC)




#class variables to define domain. 
a=0
b=1
c=0
d=1
t0=0.0
t1=10.0
nx=100
ny=100
n_time=100
'''
For calculating CFL condition of interface problem.
spatial_step_x=(b-a)/float(nx)
spatial_step_y=(d-c)/float(ny)
'''
t=onedinterval(t0,t1,n_time)
x=onedinterval(a,b,nx)
y=onedinterval(c,d,ny)

(xm,ym)=scipy.meshgrid(x,y,indexing="xy")


Ex=[]
Ey=[]
Ex=[]

Hx=[]
Hy=[]
Hz=[]

ic_func=lambda x,y: x**2+y**2
set_initial_condition(ic_func,x,y,Ex)

print Ex


