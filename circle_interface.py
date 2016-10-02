from pde import *
import math
import numpy as np
import pylab as plt
a=0
b=1
c=0
d=1
t0=0.0
t1=10.0
n=100
n_time=100
spatial_step_x=(b-a)/float(n)
spatial_step_y=(d-c)/float(n)
e_plus = 1.0
e_minus=1.2
u_plus=1.0
u_minus=1.0
c_max = math.sqrt(1.0/min(e_plus,e_minus)*min(u_plus,u_minus))

e=1.0
u=1.0
dummy_dt = (t1-t0)/float(n_time)
print dummy_dt

stab = math.sqrt(spatial_step_x**2 + spatial_step_y**2)*(1.0/(dummy_dt*c_max))
while(stab<=1):
	n_time=n_time*2
	dummy_dt = (t1-t0)/float(n_time)
	stab = math.sqrt(spatial_step_x**2 + spatial_step_y**2)*(1.0/(dummy_dt*c_max))

spatial_step_t=dummy_dt
print spatial_step_t
x_list=onedinterval(a,b,spatial_step_x,n)
y_list=onedinterval(c,d,spatial_step_y,n)
t_list=onedinterval(t0,t1,spatial_step_t,n_time)


curve_time0=0
curve_timef=2*math.pi
curve_n=1000
curve_dt = (curve_timef-curve_time0)/float(curve_n)
x_t1=[]
y_t1=[]

x_t2=[]
y_t2=[]

x_t3=[]
y_t3=[]

x_params=[]
y_params=[]
for i in range(0,curve_n):
	curent_curve_time = curve_time0 + i*curve_dt
	x_t1.append(.7 + .1*math.cos(curent_curve_time)) 
	y_t1.append(.7 + .1*math.sin(curent_curve_time)) 

	x_t2.append(.2 + .1*math.cos(curent_curve_time)) 
	y_t2.append(.7 + .1*math.sin(curent_curve_time)) 

	x_t3.append(.4 + .1*math.cos(curent_curve_time)) 
	y_t3.append(.4 + .1*math.sin(curent_curve_time)) 


x_params.append(x_t1)
x_params.append(x_t2)
x_params.append(x_t3)

y_params.append(y_t1)
y_params.append(y_t2)
y_params.append(y_t3)



lower_x=[]
lower_y=[]
upper_x=[]
upper_y=[]



	
for i in range(0,len(y_list)-1):
	for j in range(0,len(x_list)-1):
		
		for z in range(0,len(x_params)):

			for k in range(0,len(x_t1)):	
				if x_list[j] < x_params[z][k] < x_list[j+1] and y_list[i] < y_params[z][k] < y_list[i+1] :
				

					lower_x.append(x_list[j])
					lower_y.append(y_list[i])
				
					upper_x.append(x_list[j+1])
					upper_y.append(y_list[i+1])


plt.plot(x_t1,y_t1)
plt.plot(x_t2,y_t2)
plt.plot(x_t3,y_t3)
plt.plot(lower_x,lower_y, 'o')
plt.plot(upper_x,upper_y , 'o')
plt.xlim([0,1])
plt.ylim([0,1])
plt.show()
















