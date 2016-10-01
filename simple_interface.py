from pde import *
import math
import numpy as np
a=0
b=1
c=0
d=1
t0=0.0
t1=10.0
n=101
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

def ex_real(x,y,t,u,e):
	#return x + 2*u*y +t
	return 2*math.sin(2*math.pi*(-e*x +e*u*y+t))
def ey_real(x,y,t,u,e):
	#return u*x+y+t
	return math.sin(2*math.pi*(-e*u*x +e*y+t))

def ez_real(x,y,t,u,e):
	#return u*x-u*y +t
	return math.sin(2*math.pi*(u*x -u*y+t))

def hx_real(x,y,t,u,e):
	#return x+e*y +t
	return math.sin(2*math.pi*(u*x-e*u*y+t))

def hy_real(x,y,t,u,e):
	#return 2*e*x+y+t
	return math.sin(2*math.pi*(e*u*x-u*y+t))
def hz_real(x,y,t,u,e):
	#return -e*x+e*y+t
	return math.sin(2*math.pi*(-e*x+e*y+t))



interface_x = .5
interface_pos=None
for i in range(0,len(x_list)-1):
	if(x_list[i]<interface_x<x_list[i+1]):
		interface_pos=i
		print x_list[i]
		print x_list[i+1]
		print interface_pos


'''
solListE=[]
solListH=[]
for n in range(0,len(t_list)):
	print t_list[n]
	currentSolE=np.zeros((len(y_list),len(x_list)))
	currentSolH=np.zeros((len(y_list),len(x_list)))
	for i in range(0,len(y_list)):
		for j in range(0,len(x_list)):
			currentSolH[i,j] = math.sqrt(hx_real(x_list[j],y_list[i],t_list[n],u,e)**2 +hy_real(x_list[j],y_list[i],t_list[n],u,e)**2 + hz_real(x_list[j],y_list[i],t_list[n],u,e)**2)
			currentSolE[i,j] = math.sqrt(ex_real(x_list[j],y_list[i],t_list[n],u,e)**2 +ey_real(x_list[j],y_list[i],t_list[n],u,e)**2 + ez_real(x_list[j],y_list[i],t_list[n],u,e)**2)
			
	solListE.append(currentSolE)
	solListH.append(currentSolH)
print 'makeing movies now'
makeMovieMax(x_list,y_list,t_list,solListE,'E field','x','y')
makeMovieMax(x_list,y_list,t_list,solListH,'H field','x','y')
'''






