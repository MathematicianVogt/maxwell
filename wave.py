import pylab 
import matplotlib.animation as manimation
import matplotlib.pyplot as plt
import numpy as np
import math
import time

#initial conidition for u
def f(x):
    #return math.sin((x*2.0*math.pi))
    return math.sin(2*math.pi*x)
#initial condition for u_t
def g(x):
    #return 0.0
    return -2*math.pi*math.cos(2*math.pi*x)
#left boundary condition
def left_boundary(t):
    #return 0.0
    return math.sin(-2*math.pi*t)
#right boundary condition
def right_boundary(t,b):
    #return .5*(math.sin(math.pi*2.0*(b+t)) + math.sin(math.pi*2.0*(b-t)))
    return math.sin(2*math.pi*(b-t))


#variables
a=0
b=1
c=1.0
t_0=0
t_1=1.0

n_t=1000
n_x=100

delta_x=float(b-a)/n_x
delta_t=float(t_1-t_0)/n_t
x_list=[]
t_list=[]
print delta_x
print delta_t

for i in range(0,n_x+1):
    x_list.append(a+i*delta_x)

for i in range(0,n_t+1):
    t_list.append(t_0 + i*delta_t)



sol=[]

r=(c*delta_t)/delta_x

#set initial condition i.e when time=0
initial_step=[]
for x in x_list:
    initial_step.append(f(x))

sol.append(initial_step)


#move the solution forward in time. This solves the PDE.
for i in range(1,len(t_list)):
    last_sol=sol[-1]
    new_sol=[]
    for j in range(0,len(x_list)):
        if (j==0):
            new_sol.append(left_boundary(t_list[i]))
        elif(j==len(x_list)-1):
            new_sol.append(right_boundary(t_list[i],b))
        elif(i==1):
            this_sol = ((r**2)/2.0)*(last_sol[j+1]+last_sol[j-1]) + (1-(r**2))*last_sol[j] + (delta_t*g(x_list[j]))
            new_sol.append(this_sol)
        else:
            last_last_sol=sol[-2]
            this_sol =(r**2)*(last_sol[j+1]+last_sol[j-1]) + 2.0*(1-(r**2))*last_sol[j] - last_last_sol[j] 
            new_sol.append(this_sol)
    sol.append(new_sol)


#generate true solution

truesol=[]
for i in range(0,len(t_list)):
    currentsol=[]
    for j in range(0,len(x_list)):
        #ans=.5*(math.sin(2.0*math.pi*(t_list[i]+x_list[j]))+math.sin(2.0*math.pi*(x_list[j]-t_list[i])))
        #ans=x_list[j]+t_list[i]
        ans=math.sin(2*math.pi*(x_list[j]-t_list[i]))
        currentsol.append(ans)
    truesol.append(currentsol)
maxerr=0
pos=None
for j in range(0,len(x_list)):
            er=math.fabs(truesol[i][j]-sol[i][j])
            if er>maxerr:
                maxerr=er
                pos=j

print str(maxerr)
print str(pos)
print str(x_list[pos])



#Lets make a movie of our solution. 
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Finite Difference Solution', artist='Matplotlib',
                comment='Movie support!')
writer = FFMpegWriter(fps=15, metadata=metadata)

fig = plt.figure()
l, = plt.plot([], [], 'k-o')

plt.xlim(0, 1)
plt.ylim(-5, 5)

x0, y0 = 0, 0

with writer.saving(fig, "wave_FD_Solution_sin.mp4", 100):
    maxerr=0
    for i in range(0,len(t_list)):
        
        a1=fig.add_subplot(411)
        a2=fig.add_subplot(412)
        a3=fig.add_subplot(413)
        a4=fig.add_subplot(414)
        xmin=0
        xmax=1
        ymin=-1
        ymax=1
        errmin=-1
        errmax=1


        a1.set_title("Exact Solution - Wave Equation")
        a2.set_title("Finite Difference Solution - Wave Equation")
        a3.set_title("Exact and Numerical Solution")
        a4.set_title("Error")
        a1.set_xlim(xmin,xmax)
        a1.set_ylim(ymin,ymax)
        a2.set_xlim(xmin,xmax)
        a2.set_ylim(ymin,ymax)
        a3.set_xlim(xmin,xmax)
        a3.set_ylim(ymin,ymax)
        #a4.set_xlim(xmin,xmax)
        #a4.set_ylim(errmin,errmax)
        a4.autoscale_view(True,True,True)
        a1.plot(x_list,truesol[i], '-r')
        a2.plot(x_list,sol[i], '-b')
        a3.plot(x_list,sol[i], '-b')
        a3.plot(x_list,truesol[i], '-r')

        errorList=[]
        for j in range(0,len(x_list)):
            er=math.fabs(truesol[i][j]-sol[i][j])
            if er>maxerr:
                maxerr=er
            errorList.append(er)
        a4.plot(x_list,errorList, '-g')


        plt.tight_layout()
 
        
        writer.grab_frame()
        fig.clf()
        print str(t_list[i])
    print str(maxerr)





