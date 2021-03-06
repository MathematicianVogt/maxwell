from pde import *
import math
import numpy as np
import pylab as plt
import scipy.interpolate as inter
import time

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
'''
x_list=onedinterval(a,b,spatial_step_x,n)
y_list=onedinterval(c,d,spatial_step_y,n)
t_list=onedinterval(t0,t1,spatial_step_t,n_time)
'''

x_list=onedinterval(a,b,n)
y_list=onedinterval(c,d,n)

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

interface_tuple_list=[]
interface_tuple_list.append((x_t1,y_t1))
interface_tuple_list.append((x_t2,y_t2))
interface_tuple_list.append((x_t3,y_t3))


def generate_paramterization(x_func,y_func,t_list):
	x_list=[]
	y_list=[]

	for i in t_list:
		x_list.append(x_func(i))
		y_list.append(y_func(i))

	return (x_list,y_list)



def interface_plot(x_list,y_list,interface_tuple_list):
	x_params=[]
	y_params=[]
	for tuplist in interface_tuple_list:
		x_params.append(tuplist[0])
		y_params.append(tuplist[1])



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

	xGridList=[]
	yGridList=[]

	for i in x_list:
		for j in y_list:
			xGridList.append(i)
			yGridList.append(j)



	#plt.plot(xGridList,yGridList, '-')
	#plt.plot(x_t,y_t)
	plt.plot(lower_x,lower_y , '*')
	plt.plot(upper_x,upper_y, '*')
	plt.xlim([0,1])
	plt.ylim([0,1])
	plt.show()

'''
plt.plot(x_t1,y_t1)
plt.plot(x_t2,y_t2)
plt.plot(x_t3,y_t3)
plt.plot(lower_x,lower_y, 'o')
plt.plot(upper_x,upper_y , 'o')
plt.xlim([0,1])
plt.ylim([0,1])
plt.show()
'''

def generate_spline_2d(xval,yval):
	tck, u = inter.splprep([xval, yval], s=0)
	out = inter.splev(u, tck)
	return (out[0],out[1])

t = np.arange(0, 1, .001)
x = np.cos(2*np.pi*t)
y = np.sin(2*np.pi*t)
v= generate_spline_2d(x,y)
#interface_plot(x_list,y_list,interface_tuple_list)
'''
plt.plot(v[0],v[1])
plt.title("interface plot")
plt.show()
'''
def generate_spline_2d_tangent(xval,yval):
	tck, u = inter.splprep([xval, yval], s=0)
	derv = inter.splev(u, tck,der=1)
	return (derv[0],derv[1])

def generate_spline_2d_normal(xval,yval):
	tck, u = inter.splprep([xval, yval], s=0)
	derv = inter.splev(u, tck,der=1)
	return (-derv[1],derv[0])

def generate_curveature(xval,yval):
	tck, u = inter.splprep([xval, yval], s=0)
	derv = inter.splev(u, tck,der=1)
	derv2 = inter.splev(u, tck,der=2)
	curv=[]
	for i in range(0,len(xval)):
		curv.append(math.fabs( (derv2[1][i]*derv[0][i] - derv2[0][i]*derv[1][i] ))/math.pow(derv[0][i]**2  +derv[1][i]**2,1.5) )
	return curv


a=generate_spline_2d_tangent(x,y)
b=generate_spline_2d_normal(x,y)
c=generate_curveature(x,y)
plt.plot(t,c)
plt.show()
print len(t)
print len(c)

'''
plt.plot(a[0],a[1])
plt.title("tangent of interface plot")
plt.show()
plt.plot(b[0],b[1])
plt.title("normal of interface plot")
plt.show()
'''
'''
for i in range(0,len(a[0])):
	print a[0][i]*b[0][i] + a[1][i]*b[1][i]


#interface_plot(x_list,y_list,interface_tuple_list)


'''








